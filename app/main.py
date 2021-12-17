import os
from app.ocado_pdf_parser import OcadoPdfParser


def main():
    directory = './static/pdf/'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            if f.endswith('.pdf'):
                parser = OcadoPdfParser(file_name=f)
                parser.save_to_ods()


if __name__ == "__main__":
    main()
