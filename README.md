🎧 AudioBook - PDF to Speech Converter

Convert your PDFs into audiobooks effortlessly! This Python app reads each page aloud, turning your documents into listening experiences.


✨ Features

📂 Easy file selection: Choose any PDF via a graphical file dialog

📄 Page-by-page reading: Extracts and reads text from every PDF page

🗣️ Offline Text-to-Speech: Uses pyttsx3 for smooth, offline speech synthesis

⏸️ Control flow: Pause after each page and decide whether to continue or stop

⚡ Lightweight & fast: No heavy dependencies, runs smoothly on most systems


🛠️ Prerequisites

Python 3.6+


Libraries:

pyttsx3 (text-to-speech engine)

PyPDF2 (PDF text extraction)

tkinter (GUI file dialog, usually included with Python)


🚀 Installation Steps

Clone or download this repository to your local machine.


(Optional but recommended) Create a virtual environment to keep dependencies clean:

Windows:

python -m venv .venv
.venv\Scripts\activate


macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate


Install required packages:

pip install pyttsx3 PyPDF2


▶️ How to Use

Run the program:

python main.py


A file dialog will appear. Select the PDF you want to convert.

The app will read the text aloud page by page.

After each page, you will be asked:

Continue reading? (y/n):

Type y to go on, or n to stop listening.


💡 How It Works

Opens a GUI file selector using tkinter.

Uses PyPDF2 to extract text from each PDF page.

Speaks the extracted text aloud using pyttsx3.

Waits for user input after each page to continue or stop.


🐞 Troubleshooting Tips

tkinter errors?
On Linux systems, you might need to install it manually:

sudo apt-get install python3-tk


No speech or sound issues?

Check your audio system is working.

Make sure pyttsx3 installed correctly with all dependencies.


🤝 Contributing

Contributions are warmly welcomed! Fork the repo, make your changes, and open a pull request. Suggestions and bug reports are appreciated!


📄 License

This project is licensed under the MIT License. See the LICENSE file for details.


🙋‍♀️ Author

Monika Bhardwaj


❤️ Acknowledgements

pyttsx3
 for the text-to-speech engine

PyPDF2
 for PDF handling

Python’s built-in tkinter for GUI dialogs
