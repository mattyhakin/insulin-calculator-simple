# GitHub Release Notes

This file contains release descriptions used on GitHub Releases, matching the project's tagged versions.

---

## 🔹 v1.1.1 – Automation & Packaging Enhancements

### 📦 Release v1.1.1 – Automation & Packaging Enhancements

This patch release adds workflow automation and packaging improvements:

#### 🔄 Changed
- Replaced original `v1.1` tag due to conflict; now using `v1.1.1`.
- Automated Windows executable builds using GitHub Actions + PyInstaller.
- `.exe` files now attached directly to GitHub Releases.
- Added custom icon and batch installer for Windows users.
- Introduced a structured `CHANGELOG.md` following Keep a Changelog.

#### 📁 Installer
A pre-built Windows executable is available under **Assets** in this release.

---

## 🔹 v1.1 – GUI Version

### 🖥️ Major Update – GUI Interface Added

This release introduces a graphical interface using Tkinter.

#### ✅ Features
- Clean GUI layout with input fields and result display.
- Support for breakfast, lunch, dinner, snack dose types.
- Optional correction input.
- Same bolus calculation logic as CLI version.

#### 💡 Improvements
- Better input validation and user-friendly UI.
- Ready to be built into an `.exe` using PyInstaller.

---

## 🔹 v1.0 – Initial CLI Tool

### 🚀 Initial Release – CLI Tool

The first version of SimpleInsulinCalc.

#### ✅ Features
- Command-line interface for insulin dose calculation.
- Inputs: blood glucose, carbohydrate intake, correction factor.
- Outputs suggested bolus insulin dose.
- Python 3 compatible and lightweight.
