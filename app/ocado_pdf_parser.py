import csv
import os
import re
from io import StringIO

from pdfreader import SimplePDFViewer
import odswriter as ods


class OcadoPdfParser(SimplePDFViewer):
    def __init__(self, file_name: str):
        if not file_name.endswith(".pdf"):
            raise Exception("Only expected file format is PDF.")

        self.file_path = file_name

        super().__init__(open(self.file_path, 'rb'))

    def parse(self):
        self.navigate(1)
        self.render()

        strings = self.canvas.strings

        has_delivery_cost = False
        has_coupons = False
        # Find "Picking, packing and delivery" (additional cost)
        try:
            start_index = strings.index("Picking,")
            end_index = strings.index("Offers") - 1
            delivery = " ".join(strings[start_index:end_index])
            delivery = re.sub(r" +", " ", delivery)
            delivery = re.sub(r"([a-zA-Z0-9\s]*)\s£([0-9.]*)", r"\1\t\2", delivery)
            has_delivery_cost = True
        except:
            has_delivery_cost = False

        # Find "Vouchers and extras" (cost reduction)
        try:
            start_index = strings.index("Vouchers")
            end_index = strings.index("Offers")
            coupons = " ".join(strings[start_index:end_index])
            coupons = re.sub(r" +", " ", coupons)
            coupons = re.sub(r"([a-zA-Z0-9\s]*)\s-£([0-9.]*)", r"\1\t-\2", coupons)
            has_coupons = True
        except:
            has_coupons = False

        start_index = strings.index("(£)") + 1
        end_index = len(strings) - strings[-1::-1].index("Offers") - 1

        # Join string array from the start index to the end index
        items = " ".join(strings[start_index:end_index])

        # Remove any stars
        items = items.replace("*", "")

        # Add new lines between items
        items = re.sub(r"(\.[0-9][0-9]) +([A-Z])", r"\1\n\2", items)

        # Remove extra spaces
        items = re.sub(r" +", " ", items)

        # Remove everything that is not in big letters
        items = re.sub(r"[A-Z](?<=[^\d])([A-Z]?[a-z|\'\-/]+ ){2,}", "", items)

        # Remove days
        items = re.sub(r"Monday |Tuesday |Wednesday |Thursday |Friday |Saturday |Sunday ", "", items)

        # Remove leftovers
        items = re.sub(r"\(£\) ?", "", items)

        # Replace additional space after slash
        items = items.replace("/ ", "/")

        # Tab Separated Values transformation
        items = re.sub(r"([a-zA-Z0-9\s]*)\s([0-9]*/[0-9]*)\s([0-9.]*)", r"\1\t\3", items)

        if has_delivery_cost == True:
            items = items + '\n' + delivery
        if has_coupons == True:
            items = items + '\n' + coupons

        return items

    def save_to_ods(self):
        parsed_pdf = self.parse()

        file_name = os.path.basename(self.file_path)
        with ods.writer(open("./static/output/" + os.path.splitext(file_name)[0] + ".ods","wb")) as odsfile:
            f = StringIO(parsed_pdf)
            reader = csv.reader(f, delimiter='\t')
            for r, row in enumerate(reader):
                item, price = row
                odsfile.writerow([item, float(price)])
