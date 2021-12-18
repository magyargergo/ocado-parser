import os
from os import walk, listdir
from os.path import isfile, join


class TestHelper:
    PDF = 1
    TXT = 2

    def get_input_files(self, data_type, directory_name):
        sub_dir = "pdf" if data_type == TestHelper.PDF else "txt"
        path = f"./tests/data/{sub_dir}"
        return [f for f in listdir(path) if isfile(join(path, f))]

    def get_validation_file(self, file_name: str):
        files = self.get_input_files(TestHelper.TXT, "data")
        file_name_without_ext = file_name.replace(".pdf", "")
        for file in files:
            if file_name_without_ext in file:
                file_path = os.path.join(
                    os.path.dirname(__file__), f"../data/txt/{file}"
                )

                with open(file_path, "r", encoding="utf-8") as opened_file:
                    return opened_file.read()

        return None
