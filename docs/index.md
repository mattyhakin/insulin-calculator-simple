---
title: SimpleInsulinCalc User Guide
---

# 🧭 SimpleInsulinCalc – User Guide

Welcome to the official user guide for **SimpleInsulinCalc**, an open-source insulin dose calculator built to help Type 1 diabetes patients estimate bolus doses based on carbohydrate intake and correction needs.

This guide covers usage of both the command-line interface (CLI) and the graphical user interface (GUI).

---

## 🚀 CLI Version

### ▶️ Running

```bash
cd v1.0_cli
python main.py
```

### 🧪 Example

```
Type of dose: breakfast
Carbs (g): 45
Need correction? (yes/no): no
```

---

## 🖥️ GUI Version

### ▶️ Running

```bash
cd v1.1_gui
python SimpleInsulinCalc_GUI_Refactored_Accessible.py
```

### 🧰 Features

- Drop-down menu for meal types (breakfast, lunch, etc.)
- Text input for carbohydrates
- Optional correctional insulin input
- Read-only result field
- Larger fonts and keyboard accessibility
- Branded icon in the window (Windows only)

---

## 💡 Dosing Logic

The calculator uses predefined insulin-to-carb ratios per meal type (e.g., breakfast: 1 unit per 5g), and applies correctional insulin units if required.

All math is performed as:
```
(total carbs / 10) * ratio [+ correction]
```

---

## ⚠️ Disclaimer

This tool is **not a substitute for medical advice**. Always consult your healthcare provider before making any changes to your insulin regimen.

---

## 📬 Feedback

Find an issue or have a suggestion? Submit it via the [GitHub Issues](https://github.com/mattyhakin/insulin-calculator-simple/issues) page.
