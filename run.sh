#!/bin/bash 
echo "Run P1Convert_PDF_to_TXT.py "
echo "Enter the PATH where the pdf file located: "
read -r PDF_PATH
echo "Enter the PATH where the txt file saved: "
read -r SAVE_PATH
python P1Convert_PDF_to_TXT.py "$PDF_PATH" "$SAVE_PATH"
echo "Successfully P1 Executed"

echo "Run P2Convert_TXT_to_JSONL.py "
echo "Enter the PATH where the TXT file located: "
read -r PDF_PATH
echo "Enter the PATH where the JSONL file saved: "
read -r SAVE_PATH
python P2Convert_TXT_to_JSONL.py "$TXT_PATH" "$SAVE_PATH"
echo "Successfully P2 Executed"