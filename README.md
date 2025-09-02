
---

# 🎧 AudioBook Reader (Windows) - PDF to Speech Converter

![Windows](https://img.shields.io/badge/Platform-Windows-blue)
![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

> Easily convert any PDF into an audiobook!
> A Windows-only Python app that extracts text from PDFs and reads it aloud using Windows native Text-to-Speech.

---

## 🚀 Features

* 🗂️ Select any PDF via an intuitive GUI file dialog
* 📄 Extracts and cleans text from each PDF page for clarity
* 🔊 Speaks text aloud using Windows SAPI.SpVoice COM interface (high quality, native speech)
* ⏯️ User-controlled flow: decide whether to continue after each page
* ✅ Simple, lightweight, and fast

---

## 🧰 Prerequisites

* **Windows OS** (uses Windows SAPI, so not cross-platform)
* Python 3.6+
* Python packages:

  * `pywin32` (`pip install pywin32`)
  * `PyPDF2` (`pip install PyPDF2`)
* `tkinter` (usually comes with Python)

---

## 🎯 Installation & Setup

1. **Clone or download** this repository.

2. (Recommended) Create a virtual environment:

   * Windows:

     ```
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install dependencies:**

   ```
   pip install pywin32 PyPDF2
   ```

---

## ▶️ How to Use

1. Run the program:

   ```
   python audiobook_reader.py
   ```
2. A file dialog will open — select your PDF file.
3. The app will read aloud the text from each page.
4. After each page, you’ll be prompted to continue or stop:

   ```
   Continue reading? (y/n):
   ```
5. Enjoy your audiobook experience!

---

## 🛠️ How It Works

* Opens a file picker via `tkinter` for easy PDF selection
* Reads text from each page using `PyPDF2`
* Cleans extracted text for smoother speech
* Speaks text aloud using Windows SAPI.SpVoice via `pywin32` COM
* Prompts user to continue after each page

---

## ❗ Troubleshooting & Tips

* Make sure you run this on **Windows** — the speech engine is Windows-specific.
* If you get an error importing `win32com.client`, run:

  ```
  pip install pywin32
  ```
* For missing `tkinter`, install via your Python distribution or system package manager.
* Ensure your speakers/headphones are working and volume is up!

---

## 🤝 Contributing

Feel free to open issues, suggest features, or submit pull requests. Your contributions are welcome!

---

## 📜 License

This project is licensed under the **MIT License**. See the LICENSE file for details.

---

## 🙋‍♀️ About Me

**Your Name** — passionate Python developer and audiobook lover.

---

## ❤️ Acknowledgements

* Windows Text-to-Speech engine via [pywin32](https://github.com/mhammond/pywin32)
* PDF parsing thanks to [PyPDF2](https://github.com/py-pdf/PyPDF2)
* GUI file dialogs with Python’s built-in `tkinter`

---

**Enjoy listening and happy coding! 🎉**

---

