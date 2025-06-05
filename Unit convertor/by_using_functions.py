def km_to_meters(km):
    return km * 0.621371

def meters_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

while True:
    print("\n=== Unit Converter Menu ===")
    print("1. Kilometers to meters")
    print("2. meters to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        print(f"{km} km = {km_to_meters(km):.2f} miles")
    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        print(f"{miles} miles = {meters_to_km(miles):.2f} km")
    elif choice == '3':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
    elif choice == '4':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
    elif choice == '5':
        kg = float(input("Enter weight in kilograms: "))
        print(f"{kg} kg = {kg_to_pounds(kg):.2f} pounds")
    elif choice == '6':
        pounds = float(input("Enter weight in pounds: "))
        print(f"{pounds} pounds = {pounds_to_kg(pounds):.2f} kg")
    elif choice == '7':
        print("Exiting the converter. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option (1-7meters):")
        continue