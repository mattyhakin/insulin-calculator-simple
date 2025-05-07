# CLI version of SimpleInsulinCalc with improvements

ratios = {
    "breakfast": 2,
    "lunch": 1.5,
    "dinner": 1.5,
    "snack": 1.5
}
correctional = 1.0

# Get dose type
dose_type = input("What type of dose is it? (breakfast/lunch/dinner/snack): ").lower()
if dose_type not in ratios:
    print("Invalid dose type. Please try again.")
    exit()

# Get carbs
try:
    carbs = float(input("How many carbs are you eating? "))
except ValueError:
    print("Invalid number for carbs.")
    exit()

# Calculate base dose
ratio = ratios[dose_type]
dose = ratio * carbs / 10

# Check for correctional dose
correctq = input("Do you need a correctional dose? (yes/no): ").strip().lower()
if correctq == "yes":
    try:
        correct_units = float(input("How many correction units? "))
    except ValueError:
        print("Invalid number for correction units.")
        exit()
    total_dose = dose + (correct_units * correctional)
else:
    total_dose = dose

print(f"You need {total_dose:.1f} units of insulin.")