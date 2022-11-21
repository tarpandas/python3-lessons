'''
Convert weight from pounds to kilograms or kilograms to pounds based on user input
'''
unit = input("Enter weight in (L)bs or (K)g: ")
weight = int(input("Weight: "))

unit = unit.lower()

if unit == 'l' or unit == "lbs":
    weight_kgs = weight * 0.45
    print(f"{weight} in kilograms is {weight_kgs} kg.")
elif unit == 'k' or unit == "kg":
    weight_lbs = weight / 0.45
    print(f"{weight} in pounds is {weight_lbs} lbs.")
else:
    print("invalid input.")
