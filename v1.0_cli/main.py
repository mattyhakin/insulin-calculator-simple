# CLI version of SimpleInsulinCalc

#Creating a calculator in python to work out the amount of insulin to dose with
#currently my ratio's differ during different times of the day so want to make a 
#programme to do the maths for me


breakfast = 2
lunch = 1.5
dinner = 1.5
snack = 1.5
correctional = 1



dose_type = input("What Type of Dose is it: ")

if dose_type == "Breakfast" or dose_type =="breakfast":
    ratio = breakfast

elif dose_type == "Lunch" or dose_type == "lunch":
    ratio = lunch

elif dose_type == "Dinner" or dose_type == "dinner":
    ratio = dinner

elif dose_type == "Snack" or dose_type == "snack":
    ratio = snack

else:
    print("Try again")

carbs = input("How Many Carbs are you eating: ")

dose = float(ratio) * float(carbs) / 10

correctq = input("Do you need a correctional dose? ")

if correctq == "yes" or correctq == "Yes":
    correctyes = input("How many units? ")
    correct = float(correctyes) * float(correctional)
    totaldose = float(dose) + float(correct)
    print("You Need " + str(totaldose) + " Units of Insulin")

else:
    print("You Need " + str(dose) + " Units of Insulin")