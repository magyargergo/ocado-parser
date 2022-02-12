import pytest

from shutil import rmtree
from sys import maxsize
from unittest import TestCase
from os.path import exists, join
from os import makedirs

from apps.ocado_receipt_pdf_parser import OcadoReceiptPdfParser
from tests.common.test_helper import TestHelper

PREFIX = "receipt-"
TESTING_DIR = TestHelper().get_output_folder()


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup a testing directory once we are finished."""

    def remove_test_dir():
        rmtree(TESTING_DIR)

    request.addfinalizer(remove_test_dir)


class TestOcadoReceiptPdfParser(TestCase):
    def setUp(self) -> None:
        self.helper = TestHelper()
        self.maxDiff = maxsize

    def test_unknown_file_extension(self):
        unknown_file = "unknown.txt"
        with self.assertRaises(Exception) as context:
            OcadoReceiptPdfParser(file_path=unknown_file)
            self.assertTrue("Only expected file format is PDF." in context.exception)

    def test_saves_ods(self):
        receipt_file = f"{PREFIX}3129973309"
        makedirs(TESTING_DIR, exist_ok=True)

        parser = OcadoReceiptPdfParser(file_path=self.helper.get_pdf_path(receipt_file))
        parser.save_to_ods(output_location=TESTING_DIR)

        file_exists = exists(join(TESTING_DIR, f"{receipt_file}.ods"))
        self.assertTrue(file_exists)

    def test_saves_xls(self):
        receipt_file = f"{PREFIX}3129973309"
        makedirs(TESTING_DIR, exist_ok=True)

        parser = OcadoReceiptPdfParser(file_path=self.helper.get_pdf_path(receipt_file))
        parser.save_to_xls(output_location=TESTING_DIR)

        file_exists = exists(join(TESTING_DIR, f"{receipt_file}.xls"))
        self.assertTrue(file_exists)

    def test_receipt_3129973309(self):
        receipt_file = f"{PREFIX}3129973309"
        validation_file = self.helper.get_validation_file(receipt_file)
        if validation_file is not None:
            parser = OcadoReceiptPdfParser(
                file_path=self.helper.get_pdf_path(receipt_file)
            )
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )

    def test_receipt_3203908341(self):
        receipt_file = f"{PREFIX}3203908341"
        validation_file = self.helper.get_validation_file(receipt_file)
        if validation_file is not None:
            parser = OcadoReceiptPdfParser(
                file_path=self.helper.get_pdf_path(receipt_file)
            )
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )

    def test_receipt_3433538625(self):
        receipt_file = f"{PREFIX}3433538625"
        validation_file = self.helper.get_validation_file(receipt_file)
        if validation_file is not None:
            parser = OcadoReceiptPdfParser(
                file_path=self.helper.get_pdf_path(receipt_file)
            )
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )

    def test_receipt_3482933001(self):
        receipt_file = f"{PREFIX}3482933001"
        validation_file = self.helper.get_validation_file(receipt_file)
        if validation_file is not None:
            parser = OcadoReceiptPdfParser(
                file_path=self.helper.get_pdf_path(receipt_file)
            )
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )

    def test_receipt_3790976741(self):
        receipt_file = f"{PREFIX}3790976741"
        validation_file = self.helper.get_validation_file(receipt_file)
        if validation_file is not None:
            parser = OcadoReceiptPdfParser(
                file_path=self.helper.get_pdf_path(receipt_file)
            )
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )

    def test_receipt_3845981748(self):
        receipt_file = f"{PREFIX}3845981748"
        validation_file = self.helper.get_validation_file(receipt_file)
        if validation_file is not None:
            parser = OcadoReceiptPdfParser(
                file_path=self.helper.get_pdf_path(receipt_file)
            )
            parsed_file = parser.parse()

            self.assertEqual(
                validation_file.replace(" ", ""), parsed_file.replace(" ", "")
            )
