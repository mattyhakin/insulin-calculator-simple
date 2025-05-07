# SimpleInsulinCalc User Guide

SimpleInsulinCalc is a lightweight tool for calculating insulin doses based on carb intake and optional correction. It includes both a command-line (CLI) version and a graphical user interface (GUI).

---

## 🖥️ GUI Version

### How to Run

```bash
cd v1.1_gui
python SimpleInsulinCalc_GUI_Refactored.py
```

### Inputs

- **Type of Dose**: Select from breakfast, lunch, dinner, snack.
- **Carbs (g)**: Enter the number of grams of carbohydrate.
- **Need Correction?**: Select 'Yes' if a correction dose is needed.
- **Correction Units**: If Yes, enter the number of correction units.

### Output

- The total insulin dose needed is calculated and displayed in the result field.

---

## 🖱️ GUI Features

- Dropdown menu for dose type
- Radio buttons for correction input
- Read-only result field
- Icon and improved font accessibility
- Works with Windows `.exe` if built using PyInstaller

---

## 🔧 CLI Version

### How to Run

```bash
cd v1.0_cli
python main.py
```

The script will prompt you for:

1. Type of dose (e.g., breakfast)
2. Carbs
3. Correction needed (yes/no)
4. Correction units (if yes)

It will then print out the required insulin dose.

---

## ⚠️ Disclaimer

This calculator is a convenience tool and does **not** replace professional medical advice. Always consult your diabetes care team before adjusting insulin.

