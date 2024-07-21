class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Testing the Calculator class
if __name__ == "__main__":
    # Using the static method add
    sum_result = Calculator.add(3, 5)
    print(f"The sum of 3 and 5 is: {sum_result}")

    # Using the class method multiply
    product_result = Calculator.multiply(4, 6)
    print(f"The product of 4 and 6 is: {product_result}")
