"""
Temperature conversions
"""

MENU = """
    CE - Convert Celsius to Fahrenheit
    FA - Convert Fahrenheit to Celsius
    Q - Quit"""


def main():
    print(MENU)
    choice = input("# ").upper()
    while choice != "Q":
        if choice == "CE":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "FA":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()