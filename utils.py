import os
import fitz

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')

def convert_PDFtoTXT(PDF_PATH, SAVE_PATH):
    if not os.path.exists(PDF_PATH):
        raise Exception("PDF file does not exist")

    if not os.path.isfile(SAVE_PATH):
        print(f"While running convert_PDFtoTXT: Create a new txt file at {SAVE_PATH}")
        with open(SAVE_PATH, 'w') as f: f.close()

    with open(os.path.join(SAVE_PATH), 'w', encoding="utf-8") as f:
        PDF = fitz.open(PDF_PATH)
        for page in PDF:
            text_blocks = page.get_text("blocks")
        
            for (x0, y0, x1, y1, content, line_no, block_no) in text_blocks:
                if x1 < 509:
                    f.write(content)
                elif content.rstrip()[-1] == '.':
                    f.write(content)
                else:
                    f.write(content.rstrip())
        print(f"While running convert_PDFtoTXT: Converted txt file saved at {SAVE_PATH}")

    return 

def convert_TXTtoJSONL(TXT_PATH, SAVE_PATH):
    if not os.path.exists(TXT_PATH):
        raise Exception("TXT file does not exist")

    if not os.path.isfile(SAVE_PATH):
        print(f"While running convert_PDFtoJSONL: Create a new JSONL file at {SAVE_PATH}")
        with open(SAVE_PATH, 'w') as f: f.close()

    with open(SAVE_PATH, 'w', encoding="utf-8") as f, open(TXT_PATH, 'r', encoding='utf-8') as txt:
        for line in txt:
            f.write('{' + f"\"role\": \"user\", \"content\": \"{line.rstrip()}\"" + '}' + '\n')
    return