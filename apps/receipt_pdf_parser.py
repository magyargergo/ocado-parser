import csv
import os
import odswriter as ods

from io import StringIO
from pdfreader import SimplePDFViewer
from xlsxwriter import Workbook


class ReceiptPdfParser(SimplePDFViewer):
    def __init__(self, file_path: str):
        if not file_path.endswith(".pdf"):
            raise Exception("Only expected file format is PDF.")

        self.file_path = file_path
        self.parsed_pdf = None

        super().__init__(open(self.file_path, "rb"))

    def parse(self) -> str:
        """
        Parses the given receipt.

        :return: Tab separated table: item price
        """
        raise NotImplemented()

    def save_to_ods(self, output_location: str) -> type(None):
        """
        Saves the receipt into an OpenDocument format.

        :param output_location: ods file location
        :return:
        """
        if self.parsed_pdf is None:
            self.parsed_pdf = self.parse()

        file_name = os.path.splitext(os.path.basename(self.file_path))[0]
        file_path = os.path.join(output_location, f"{file_name}.ods")
        with ods.writer(open(file_path, "wb")) as odsfile:
            f = StringIO(self.parsed_pdf)
            reader = csv.reader(f, delimiter="\t")
            for r, row in enumerate(reader):
                item, price = row
                odsfile.writerow([item, float(price)])

    def save_to_xls(self, output_location: str) -> type(None):
        """
        Saves the receipt into an XLS format.

        :param output_location: xls file location
        :return:
        """
        if self.parsed_pdf is None:
            self.parsed_pdf = self.parse()

        file_name = os.path.splitext(os.path.basename(self.file_path))[0]
        file_path = os.path.join(output_location, f"{file_name}.xls")

        workbook = Workbook(file_path, {"constant_memory": True})
        worksheet = workbook.add_worksheet()

        f = StringIO(self.parsed_pdf)
        reader = csv.reader(f, delimiter="\t")
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)

        workbook.close()
