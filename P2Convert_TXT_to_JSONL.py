import os
import argparse

from data_utils import convert_TXTtoJSONL

parser = argparse.ArgumentParser(description="Convert .txt file to .jsonl file")
parser.add_argument("TXT_PATH", help="PATH where the TXT file located")
parser.add_argument("SAVE_PATH", help="PATH where the JSONL file saved")

def main():
    convert_TXTtoJSONL(TXT_PATH, SAVE_PATH)

if __name__ == "__main__":
    args = parser.parse_args()
    TXT_PATH = args.TXT_PATH
    SAVE_PATH = args.SAVE_PATH
    main()