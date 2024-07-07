# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: Temperature in Fahrenheit.

    Returns:
        Temperature converted to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in Celsius.

    Returns:
        Temperature converted to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    """Prompts user for temperature and unit, performs conversion, and displays result in expected format."""

    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

            if unit == "C":
                converted_temp = convert_to_fahrenheit(temperature)
                converted_unit = "F"
            elif unit == "F":
                converted_temp = convert_to_celsius(temperature)
                converted_unit = "C"
            else:
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

            print(f"{temperature:.2f}°{unit} is equal to {converted_temp:.2f}°{converted_unit}.")
            break

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
