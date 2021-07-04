from app.ocado_pdf_parser import OcadoPdfParser


def main():
    parser = OcadoPdfParser(file_name='../static/pdf/receipt-3596989256.pdf')
    parser.save_to_xlsx()


if __name__ == "__main__":
    main()
