temperature = float(input("Enter the current temperature (in degrees Celsius): "))
if temperature < 0:
    print("The current temperature is extremely cold.")
elif temperature < 10:
    print("The current temperature is quite cold.")
elif temperature < 25:
    print("The current temperature is comfortable.")
else:
    print("The current temperature is quite hot.")

    