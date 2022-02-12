import os
from os import walk, listdir
from os.path import isfile, join


class TestHelper:
    def get_validation_file(self, file_name: str):
        file_path = os.path.join(
            self.get_tests_folder_location(), "data", "txt", f"{file_name}.txt"
        )

        with open(file_path, "r", encoding="utf-8") as opened_file:
            return opened_file.read()

    def get_pdf_path(self, file_name: str):
        return os.path.join(
            self.get_tests_folder_location(), "data", "pdf", f"{file_name}.pdf"
        )

    def get_output_folder(self):
        return os.path.join(self.get_tests_folder_location(), "static", "output")

    def get_tests_folder_location(self):
        return os.path.join(os.path.dirname(__file__), "..")
