import os
from apps.ocado_pdf_parser import OcadoPdfParser


def main():
    directory = os.path.join(os.path.dirname(__file__), "static", "pdf")
    output = os.path.join(os.path.dirname(__file__), "static", "output")
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            if f.endswith(".pdf"):
                parser = OcadoPdfParser(file_name=f)
                parser.save_to_ods(output_location=output)


if __name__ == "__main__":
    main()
