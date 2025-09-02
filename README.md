
---

# 🎧 AudioBook - PDF to Speech Converter

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Working%20Perfectly-brightgreen)

> **Transform your PDFs into audiobooks!**
> Effortlessly convert any PDF into clear, natural-sounding speech — page by page.

---

## ✨ Features

* 📂 **Easy PDF selection** with a friendly file dialog
* 📝 **Page-by-page text extraction** using `PyPDF2`
* 🔊 **Offline Text-to-Speech** powered by `pyttsx3`
* ⏯️ **Pause and control** reading after each page
* ⚡ **Lightweight & efficient** — no internet needed

---

## 🧰 Prerequisites

* Python 3.6 or above
* Libraries:

  * `pyttsx3`
  * `PyPDF2`
  * `tkinter` (usually pre-installed)

---

## 🚀 Installation

**Step 1: Clone or Download**

```bash
git clone https://github.com/yourusername/AudioBook.git
cd AudioBook
```

**Step 2: Create a virtual environment (recommended)**

* Windows:
  `python -m venv .venv`
  `.venv\Scripts\activate`

* macOS/Linux:
  `python3 -m venv .venv`
  `source .venv/bin/activate`

**Step 3: Install dependencies**

```bash
pip install pyttsx3 PyPDF2
```

---

## 🎯 How to Use

Run the app:

```bash
python main.py
```

1. Select your PDF in the dialog that appears
2. Listen as each page is read aloud
3. After each page, choose to continue or stop

---

## 🛠️ How It Works

* Uses `tkinter` for file selection
* Extracts text with `PyPDF2`
* Reads aloud with `pyttsx3`
* User controls flow via prompts after each page

---

## ❗ Troubleshooting

* **tkinter missing?**
  Linux users:
  `sudo apt-get install python3-tk`

* **No sound?**
  Verify your audio system and that `pyttsx3` installed correctly.

---

## 🤝 Contributing

Open to contributions! Fork, improve, and submit PRs. Issues and feature requests welcome.

---

## 📜 License

MIT License. See the LICENSE file.

---

## 🙋‍♀️ About Me

**Monika Bhardwaj** – passionate Python dev & audiobook enthusiast.

---

## ❤️ Acknowledgements

* [pyttsx3](https://github.com/nateshmbhat/pyttsx3)
* [PyPDF2](https://github.com/py-pdf/PyPDF2)
* Python’s built-in `tkinter`

---

**Enjoy your listening experience! 🎉**

---

