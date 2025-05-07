import tkinter as tk
import os

# Ratios for different meal types
RATIOS = {
    "breakfast": 2.0,
    "lunch": 1.5,
    "dinner": 1.5,
    "snack": 1.5
}
CORRECTIONAL_RATIO = 1.0

def calculate():
    try:
        dose_type = input_display.get().lower()
        if dose_type not in RATIOS:
            result_display.set("Select a valid dose type.")
            return

        carbs_str = carbs_display.get()
        if not carbs_str:
            result_display.set("Enter carbohydrate amount.")
            return

        try:
            carbs = float(carbs_str)
        except ValueError:
            result_display.set("Invalid carb value.")
            return

        dose = RATIOS[dose_type] * carbs / 10

        if correctional_question.get() == "yes":
            correction_units = correction_display.get()
            try:
                correction = float(correction_units) * CORRECTIONAL_RATIO
                total_dose = dose + correction
                result_display.set(f"You need {total_dose:.1f} units of insulin.")
            except ValueError:
                result_display.set("Invalid correction units.")
        else:
            result_display.set(f"You need {dose:.1f} units of insulin.")

    except Exception as e:
        result_display.set(f"Error: {e}")

def clear_inputs():
    input_display.set("breakfast")
    carbs_display.set("")
    correctional_question.set("no")
    correction_display.set("")
    result_display.set("")

# Main window
root = tk.Tk()
root.title("Insulin Dose Calculator")
icon_path = os.path.join(os.path.dirname(__file__), "..", "installer", "icon.ico")
if os.path.exists(icon_path):
    try:
        root.iconbitmap(icon_path)
    except:
        pass

# Fonts and padding
font = ("Arial", 12)
pad_opts = {'padx': 6, 'pady': 6, 'sticky': 'w'}

# Variables
input_display = tk.StringVar(value="breakfast")
carbs_display = tk.StringVar()
correctional_question = tk.StringVar(value="no")
correction_display = tk.StringVar()
result_display = tk.StringVar()

# Layout
tk.Label(root, text="Type of Dose:", font=font).grid(row=0, column=0, **pad_opts)
dose_menu = tk.OptionMenu(root, input_display, *RATIOS.keys())
dose_menu.grid(row=0, column=1, **pad_opts)
dose_menu.config(font=font)

tk.Label(root, text="Carbs (g):", font=font).grid(row=1, column=0, **pad_opts)
carbs_entry = tk.Entry(root, textvariable=carbs_display, font=font)
carbs_entry.grid(row=1, column=1, **pad_opts)
carbs_entry.focus_set()

tk.Label(root, text="Need Correction?", font=font).grid(row=2, column=0, **pad_opts)
frame = tk.Frame(root)
frame.grid(row=2, column=1, **pad_opts)
tk.Radiobutton(frame, text="Yes", variable=correctional_question, value="yes", font=font).pack(side="left")
tk.Radiobutton(frame, text="No", variable=correctional_question, value="no", font=font).pack(side="left")

tk.Label(root, text="Correction Units:", font=font).grid(row=3, column=0, **pad_opts)
tk.Entry(root, textvariable=correction_display, font=font).grid(row=3, column=1, **pad_opts)

tk.Label(root, text="Result:", font=font).grid(row=4, column=0, **pad_opts)
tk.Entry(root, textvariable=result_display, font=font, state="readonly").grid(row=4, column=1, **pad_opts)

tk.Button(root, text="Calculate", command=calculate, font=font).grid(row=5, column=0, **pad_opts)
tk.Button(root, text="Clear", command=clear_inputs, font=font).grid(row=5, column=1, **pad_opts)

if __name__ == "__main__":
    root.mainloop()
