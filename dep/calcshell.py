import math

def ansh():
    symbols = ['|', '/', '-', '\\']
    for _ in range(10):  # Change the range to control the duration of the animation
        for symbol in symbols:
            print(f"Calculating {symbol}", end='\r')
            ti.sleep(0.1)  # Adjust the sleep duration to control the speed of animation


GOLDEN_RATIO = (1 + math.sqrt(5)) / 2
PI = math.pi
EULER_NUMBER = math.e
SPEED_OF_LIGHT = 299792458  # meters per second
PLANCK_CONSTANT = 6.62607015e-34  # Planck constant in J·s

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Invalid input for square root"

def power(x, y):
    return x ** y

def factorial(x):
    return math.factorial(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base):
    return math.log(x, base)

def ln(x):
    return math.log(x)

def absolute(x):
    return abs(x)

def round_number(x):
    return round(x)

def calculator():
    print("Welcome to CalcShell - the calculator designed for Flash!")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Power")
        print("7. Factorial")
        print("8. Sine (sin)")
        print("9. Cosine (cos)")
        print("10. Tangent (tan)")
        print("11. Logarithm (log)")
        print("12. Natural Logarithm (ln)")
        print("13. Absolute Value")
        print("14. Round Number")
        print("15. Constants")
        print("16. Exit")

        choice = input("Enter choice (1-16): ")

        if choice == '16':
            print("Exiting CalcShell. Goodbye!")
            break

        if choice == '15':
            print("Choose a constant:")
            print("1. Golden Ratio")
            print("2. Pi")
            print("3. Euler's Number (e)")
            print("4. Speed of Light")
            print("5. Planck Constant")
            constant_choice = input("Enter constant choice (1-5): ")
            
            if constant_choice == '1':
                constant = GOLDEN_RATIO
            elif constant_choice == '2':
                constant = PI
            elif constant_choice == '3':
                constant = EULER_NUMBER
            elif constant_choice == '4':
                constant = SPEED_OF_LIGHT
            elif constant_choice == '5':
                constant = PLANCK_CONSTANT
            else:
                print("Invalid constant choice. Using default value (Golden Ratio).")
                constant = GOLDEN_RATIO

            print(f"Selected Constant: {constant}")
            continue

        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'):
            if choice in ('5', '7', '8', '9', '10', '13', '14'):
                num1 = float(input("Enter number: "))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = "Addition"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "Division"
            elif choice == '5':
                result = square_root(num1)
                operation = "Square Root"
            elif choice == '6':
                result = power(num1, num2)
                operation = "Power"
            elif choice == '7':
                result = factorial(int(num1))
                operation = "Factorial"
            elif choice == '8':
                result = sin(num1)
                operation = "Sine"
            elif choice == '9':
                result = cos(num1)
                operation = "Cosine"
            elif choice == '10':
                result = tan(num1)
                operation = "Tangent"
            elif choice == '11':
                base = float(input("Enter the base of the logarithm: "))
                result = log(num1, base)
                operation = "Logarithm"
            elif choice == '12':
                result = ln(num1)
                operation = "Natural Logarithm"
            elif choice == '13':
                result = absolute(num1)
                operation = "Absolute Value"
            elif choice == '14':
                result = round_number(num1)
                operation = "Round Number"

            print(f"{operation} Result: {result}")
        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    calculator()