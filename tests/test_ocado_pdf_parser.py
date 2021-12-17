import sys
from unittest import TestCase

from app.ocado_pdf_parser import OcadoPdfParser
from tests.common.test_helper import TestHelper


class TestOcadoPdfParser(TestCase):
    def setUp(self) -> None:
        self.helper = TestHelper()
        self.maxDiff = sys.maxsize

    def test_receipt_3203908341(self):
        receipt_pdf = "receipt-3203908341.pdf"
        validation_file = self.helper.get_validation_file(receipt_pdf)
        if validation_file is not None:
            parser = OcadoPdfParser(file_name=f"../tests/data/pdf/{receipt_pdf}")
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )

    def test_receipt_3129973309(self):
        receipt_pdf = "receipt-3129973309.pdf"
        validation_file = self.helper.get_validation_file(receipt_pdf)
        if validation_file is not None:
            parser = OcadoPdfParser(file_name=f"../tests/data/pdf/{receipt_pdf}")
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )

    def test_receipt_3482933001(self):
        receipt_pdf = "receipt-3482933001.pdf"
        validation_file = self.helper.get_validation_file(receipt_pdf)
        if validation_file is not None:
            parser = OcadoPdfParser(file_name=f"../tests/data/pdf/{receipt_pdf}")
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )

    def test_receipt_3790976741(self):
        receipt_pdf = "receipt-3790976741.pdf"
        validation_file = self.helper.get_validation_file(receipt_pdf)
        if validation_file is not None:
            parser = OcadoPdfParser(file_name=f"../tests/data/pdf/{receipt_pdf}")
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )

    def test_receipt_3845981748(self):
        receipt_pdf = "receipt-3845981748.pdf"
        validation_file = self.helper.get_validation_file(receipt_pdf)
        if validation_file is not None:
            parser = OcadoPdfParser(file_name=f"../tests/data/pdf/{receipt_pdf}")
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )
