# Global variables for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Function to handle user interaction and input validation
def main():
    while True:
        try:
            temperature_str = input("Enter temperature (e.g., 32F or 0C): ").strip().upper()
            
            if temperature_str[-1] == 'F':
                temperature = float(temperature_str[:-1])
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp:.2f}°C")
            elif temperature_str[-1] == 'C':
                temperature = float(temperature_str[:-1])
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp:.2f}°F")
            else:
                raise ValueError("Invalid temperature format. Please enter a numeric value followed by 'C' or 'F'.")
        
        except ValueError as ve:
            print(f"Error: {ve}")
            continue
        
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

# Run the main function
if __name__ == "__main__":
    main()
