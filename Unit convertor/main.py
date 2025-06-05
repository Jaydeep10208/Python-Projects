while True:
    print("\n=== Unit Converter Menu ===")
    print("1. Kilometers to Meter")
    print("2. Meter to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Exit")

    choice = (input("Enter your choice (1-7): "))

    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        print(f"{km} km = {km * 1000:.2f} meters")
    elif choice == "2":
        meters = float(input("Enter distance in meters: "))
        print(f"{meters} meters = {meters / 1000:.2f} km")
    elif choice == "3":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {(c * 9/5) + 32:.2f}°F")
    elif choice == "4":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {(f - 32) * 5/9:.2f}°C")
    elif choice == "5":
        kg = float(input("Enter weight in kilograms: "))
        print(f"{kg} kg = {kg * 2.20462:.2f} pounds")
    elif choice == "6":
        pounds = float(input("Enter weight in pounds: "))
        print(f"{pounds} pounds = {pounds / 2.20462:.2f} kg")
    elif choice == "7":
        print("Exiting the converter. Goodbye!")
        break