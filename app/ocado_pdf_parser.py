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

        start_index = strings.index("(£)") + 1
        end_index = len(strings) - strings[-1::-1].index("Offers") - 1

        # Join string array from the start index to the end index
        orders = " ".join(strings[start_index:end_index])

        # Remove any starts
        orders = orders.replace("*", "")

        # Add new lines between orders
        orders = re.sub(r"(\.[0-9][0-9]) +([A-Z])", r"\1\n\2", orders)

        # Remove extra spaces
        orders = re.sub(r" +", " ", orders)

        # Remove everything that is not in big letters
        orders = re.sub(r"[A-Z](?<=[^\d])([A-Z]?[a-z|\'\-/]+ ){2,}", "", orders)

        # Remove days
        orders = re.sub(r"Monday |Tuesday |Wednesday |Thursday |Friday |Saturday |Sunday ", "", orders)

        # Remove leftovers
        orders = re.sub(r"\(£\) ?", "", orders)

        # Replace additional space after slash
        orders = orders.replace("/ ", "/")

        # Tab Separated Values transformation
        orders = re.sub(r"([a-zA-Z0-9\s]*)\s([0-9]*/[0-9]*)\s([0-9.]*)", r"\1\t\2\t\3", orders)

        return orders

    def save_to_ods(self):
        parsed_pdf = self.parse()

        file_name = os.path.basename(self.file_path)
        with ods.writer(open("./static/output/" + os.path.splitext(file_name)[0] + ".ods","wb")) as odsfile:
            f = StringIO(parsed_pdf)
            reader = csv.reader(f, delimiter='\t')
            for r, row in enumerate(reader):
                item, price = row
                odsfile.writerow([item, float(price)])
