# Global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def FAHRENHEIT_TO_CELSIUS_FACTOR(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor."""
    return (fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR) - 32


def CELSIUS_TO_FAHRENHEIT_FACTOR(celsius):
    """Convert Celsius to Fahrenheit using global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)

        # Get temperature unit input
        unit = input(
            "Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(fahrenheit)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
