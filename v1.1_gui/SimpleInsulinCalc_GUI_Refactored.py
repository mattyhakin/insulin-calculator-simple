import tkinter as tk

# Ratios for different meal types
RATIOS = {
    "breakfast": 2.0,
    "lunch": 1.5,
    "dinner": 1.5,
    "snack": 1.5
}
CORRECTIONAL_RATIO = 1.0

# Function to process the input and calculate the dose
def calculate():
    try:
        dose_type = input_display.get().lower()
        if dose_type not in RATIOS:
            result_display.set("Please select a valid dose type.")
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

# Function to clear all inputs and results
def clear_inputs():
    input_display.set("breakfast")
    carbs_display.set("")
    correctional_question.set("no")
    correction_display.set("")
    result_display.set("")

# Create the main window
root = tk.Tk()
root.title("Insulin Dose Calculator")

# Display variables
input_display = tk.StringVar(value="breakfast")
carbs_display = tk.StringVar()
correctional_question = tk.StringVar(value="no")
correction_display = tk.StringVar()
result_display = tk.StringVar()

# Layout
tk.Label(root, text="Type of Dose:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.OptionMenu(root, input_display, *RATIOS.keys()).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Carbs (g):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Entry(root, textvariable=carbs_display).grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Need Correction?").grid(row=2, column=0, padx=5, pady=5, sticky="e")
frame = tk.Frame(root)
frame.grid(row=2, column=1, padx=5, pady=5)
tk.Radiobutton(frame, text="Yes", variable=correctional_question, value="yes").pack(side="left")
tk.Radiobutton(frame, text="No", variable=correctional_question, value="no").pack(side="left")

tk.Label(root, text="Correction Units:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
tk.Entry(root, textvariable=correction_display).grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Result:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
tk.Entry(root, textvariable=result_display, state="readonly").grid(row=4, column=1, padx=5, pady=5)

tk.Button(root, text="Calculate", command=calculate).grid(row=5, column=0, pady=10)
tk.Button(root, text="Clear", command=clear_inputs).grid(row=5, column=1, pady=10)

# Run the application
if __name__ == "__main__":
    root.mainloop()
