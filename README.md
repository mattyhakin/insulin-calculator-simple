<p align="center">
    <img src="https://github.com/mattyhakin/insulin-calculator-simple/blob/main/simple-insulin-header.png?raw=true" alt="Simple Insulin Calculator"/>
    
# SimpleInsulinCalc

> A lightweight insulin dose calculator with CLI and GUI support for people with Type 1 diabetes.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
[![Latest Release](https://img.shields.io/github/v/release/mattyhakin/simpleinsulincalc?label=release)](https://github.com/mattyhakin/simpleinsulincalc/releases)
[![CI Tests](https://github.com/mattyhakin/simpleinsulincalc/actions/workflows/python-ci.yml/badge.svg)](https://github.com/mattyhakin/simpleinsulincalc/actions)
[![Build Installer](https://github.com/mattyhakin/simpleinsulincalc/actions/workflows/pyinstaller.yml/badge.svg)](https://github.com/mattyhakin/simpleinsulincalc/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📦 Versions

- **v1.0 CLI** – A simple command-line tool for calculating insulin doses.
- **v1.1 GUI** – A Tkinter-based GUI app with user-friendly features.
- **v1.1.1** – Adds automated build and release workflow using GitHub Actions and PyInstaller.

---

## 🚀 Features

- Carbohydrate-based bolus dose calculation
- Optional correctional insulin input
- GUI supports dropdowns and radio buttons for better UX
- Fully testable and cross-platform
- GitHub Actions CI/CD for testing and builds

---

## 🔧 Installation

### CLI Version

```bash
cd v1.0_cli
pip install -r requirements.txt
python main.py
```

### GUI Version

```bash
cd v1.1_gui
pip install -r requirements.txt
python SimpleInsulinCalc_GUI_Refactored_Accessible.py
```

---

## 💾 Executable Download

Download the `.exe` from the [Releases page](https://github.com/mattyhakin/simpleinsulincalc/releases) for Windows — no Python required.

---

## 📄 Documentation

- [User Guide](docs/user_guide.md)
- [CHANGELOG.md](CHANGELOG.md)
- [RELEASE_NOTES.md](RELEASE_NOTES.md)
- [docs/](docs/) (for GitHub Pages)

---

## 🧪 Testing

Tests run automatically on GitHub Actions. You can run them locally with:

```bash
cd v1.0_cli
pytest test_cli.py

cd ../v1.1_gui
pytest test_gui.py
```

---

## 📁 Project Structure

```
simpleinsulincalc/
├── v1.0_cli/             # CLI version
├── v1.1_gui/             # GUI version
├── installer/            # PyInstaller scripts & icon
├── .github/workflows/    # GitHub Actions
├── docs/                 # User guide and optional docs site
├── README.md
├── CHANGELOG.md
└── RELEASE_NOTES.md
```

---

## 📝 Notes

This project is a combination of two previous projects I created the simpleinsulincalc (v1.0) and simpleinsulincalcGUI (v1.1). I have since removed them from my GitHub project after the creation of this Repo.

---

## 👨‍⚕️ Disclaimer

This app does **not** replace medical advice. Always consult your doctor before making insulin adjustments.

---

## 📝 License

MIT License. See [LICENSE](LICENSE) for full terms.
