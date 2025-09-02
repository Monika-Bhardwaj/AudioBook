AudioBook - PDF to Speech Converter

A Python application that converts PDF documents into audiobooks by reading each page aloud using text-to-speech.

Features

Select a PDF file through a user-friendly file dialog.

Extract text from every page of the PDF.

Use offline text-to-speech synthesis to read the text aloud.

Prompt user after each page to continue or stop.

Lightweight and easy to use.

Prerequisites

Python 3.6 or higher

Python libraries:

pyttsx3 (Text-to-speech engine)

PyPDF2 (PDF text extraction)

tkinter (File dialog; usually pre-installed with Python)

Installation

Clone this repository or download the source files.

(Optional) Create and activate a virtual environment:

On Windows:
python -m venv .venv
.venv\Scripts\activate

On macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate

Install required packages with:
pip install pyttsx3 PyPDF2

Usage

Run the main Python script by executing:
python main.py

A file dialog will open to select your PDF file.

The program will read the text of each page aloud.

After each page, you will be prompted to continue reading or stop.

How It Works

Uses tkinter to open a file selection dialog.

Reads PDF pages using PyPDF2.

Extracted text is passed to pyttsx3 for speech synthesis.

Provides user control to continue or stop after each page.

Troubleshooting

If you get errors related to tkinter, install it manually (for example, on Ubuntu/Debian):
sudo apt-get install python3-tk

If speech does not work, ensure your system audio is enabled and pyttsx3 dependencies are installed properly.

Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

Monika Bhardwaj

Acknowledgements

pyttsx3 for the text-to-speech engine.

PyPDF2 for PDF parsing.

Python’s tkinter library for file dialogs.
