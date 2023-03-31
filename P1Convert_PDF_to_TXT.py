import argparse

from data_utils import convert_PDFtoTXT

parser = argparse.ArgumentParser(description="Convert .pdf file to .txt file")
parser.add_argument("PDF_PATH", help="PATH where the PDF file located")
parser.add_argument("SAVE_PATH", help="PATH where the TXT file saved")

def main():
    convert_PDFtoTXT(PDF_PATH, SAVE_PATH)

if __name__ == "__main__":
    args = parser.parse_args()
    PDF_PATH = args.PDF_PATH
    SAVE_PATH = args.SAVE_PATH
    main()