"""
audiobook_reader.py

A simple audiobook reader that reads aloud text extracted from each page of a PDF file.

Uses Windows native Text-to-Speech (TTS) engine via pywin32 COM interface for reliable speech output.

Features:
- Select a PDF file via GUI file dialog.
- Extracts and cleans text from each page.
- Reads each page aloud.
- Prompts user whether to continue reading after each page.

Requirements:
- Windows OS
- pywin32 (`pip install pywin32`)
- PyPDF2 (`pip install PyPDF2`)

Author: Your Name
Date: 2025-09-03
"""

import win32com.client
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename
import re
import sys


def select_pdf_file():
    """
    Open a file dialog for the user to select a PDF file.
    Returns:
        str: The path to the selected PDF file, or None if no file selected.
    """
    return askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])


def extract_text_from_page(page):
    """
    Extract and clean text from a PDF page object.

    Args:
        page (PyPDF2._page.PageObject): A page from PdfReader.

    Returns:
        str: Cleaned text extracted from the page.
    """
    raw_text = page.extract_text()
    if raw_text and raw_text.strip():
        # Replace multiple whitespace/newlines with a single space
        cleaned_text = re.sub(r'\s+', ' ', raw_text).strip()
        return cleaned_text
    return None


def speak_text(text, speaker):
    """
    Use the Windows SAPI.SpVoice engine to speak text aloud.

    Args:
        text (str): The text to be spoken.
        speaker (COM object): Initialized SAPI.SpVoice object.
    """
    speaker.Speak(text)


def main():
    pdf_path = select_pdf_file()

    if not pdf_path:
        print("No file selected. Exiting.")
        sys.exit()

    reader = PdfReader(pdf_path)
    pages = len(reader.pages)

    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    print(f"Loaded PDF: {pdf_path} with {pages} pages.\n")

    current_page = 0

    while current_page < pages:
        page = reader.pages[current_page]
        text = extract_text_from_page(page)

        if text:
            print(f"\n📖 Reading page {current_page + 1}...")
            print(f"Preview: {text[:100]!r}...\n")
            speak_text(text, speaker)
        else:
            print(f"Page {current_page + 1} has no extractable text.")

        choice = input("Continue reading? (y/n): ").strip().lower()
        if choice != 'y':
            print("Stopping reading.")
            break

        current_page += 1

    print("\n✅ Done.")


if __name__ == "__main__":
    main()
