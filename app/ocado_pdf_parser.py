import csv
import os
import re

from pdfreader import SimplePDFViewer
from xlsxwriter import Workbook

TEMP_FILE_NAME = "tmp.csv"


class OcadoPdfParser(SimplePDFViewer):
    def __init__(self, file_name: str):
        if not file_name.endswith(".pdf"):
            raise Exception("Only expected file format is PDF.")

        self.file_path = os.path.join(
            os.path.dirname(__file__),
            file_name
        )

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

    def save_to_xlsx(self):
        parsed_pdf = self.parse()
        parsed_pdf = parsed_pdf.replace("\t", ",")

        with open(TEMP_FILE_NAME, "w", encoding='utf8') as text_file:
            text_file.write(parsed_pdf)

        file_name = os.path.basename(self.file_path)
        workbook = Workbook(
            "../static/output/" + os.path.splitext(file_name)[0] + ".xlsx",
            {"constant_memory": True}
        )

        worksheet = workbook.add_worksheet()
        with open(TEMP_FILE_NAME, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)

        workbook.close()

        # Remove temp file
        os.remove(TEMP_FILE_NAME)
