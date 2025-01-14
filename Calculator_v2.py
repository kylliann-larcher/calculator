import random

# Main function to run the program
def main():
    calculator()

# Calculation history
history = []

# Last result
last_result = None

# Define calculation functions
def addition(number_1, number_2):
    return number_1 + number_2

def subtraction(number_1, number_2):
    return number_1 - number_2

def multiplication(number_1, number_2):
    return number_1 * number_2

def division(number_1, number_2):
    if number_2 != 0:
        return number_1 / number_2
    else:
        return "Division by zero is not allowed"

def square(number):
    return number ** 2

def square_root(number):
    if number >= 0:
        return number ** 0.5
    else:
        return "Square root of a negative number is not allowed"

def power(base, exponent):
    return base ** exponent

def logarithm_base10(number):
    if number > 0:
        return (number ** (1 / 10)) - 1  # Simplified logarithmic approximation
    else:
        return "Logarithm of a number <= 0 is undefined"

def factorial(number):
    if number >= 0 and number == int(number):
        result = 1
        for i in range(1, int(number) + 1):
            result *= i
        return result
    else:
        return "Factorial is only defined for positive integers"

def modulo(number_1, number_2):
    return number_1 % number_2

def floor_division(number_1, number_2):
    if number_2 != 0:
        return number_1 // number_2
    else:
        return "Floor division by zero is not allowed"

def absolute_value(number):
    return number if number >= 0 else -number

def sine(number):
    return round(sum((-1) ** k * (number ** (2 * k + 1)) / factorial(2 * k + 1) for k in range(10)), 6)

def cosine(number):
    return round(sum((-1) ** k * (number ** (2 * k)) / factorial(2 * k) for k in range(10)), 6)

def tangent(number):
    try:
        return sine(number) / cosine(number)
    except ZeroDivisionError:
        return "Undefined tangent"

# Manage history
def show_history():
    if len(history) == 0:
        return "No history available"
    else:
        print("\n----------------- Calculation History -----------------")
        return "\n".join(history)

def clear_history():
    history.clear()
    return "History cleared"

# Display options menu
def menu():
    print("---------------------- Welcome to the Calculator -------------------")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")
    print("7. Power")
    print("8. Logarithm (base 10)")
    print("9. Factorial")
    print("10. Modulo")
    print("11. Floor Division")
    print("12. Absolute Value")
    print("13. Sine")
    print("14. Cosine")
    print("15. Tangent")
    print("16. Show History")
    print("17. Clear History")
    print("18. Exit")

# Calculator function
def calculator():
    global last_result  # Use global variable for last result
    while True:
        menu()
        choice = input("Enter your choice: ")

        try:
            if choice in ['1', '2', '3', '4', '7', '10', '11']:  # Operations requiring two numbers
                if last_result is not None:
                    use_last_result = input("Use the last result? (y/n): ").lower()
                    if use_last_result == 'y':
                        number_1 = last_result
                    else:
                        number_1 = float(input("Enter the first number: "))
                else:
                    number_1 = float(input("Enter the first number: "))

                number_2 = float(input("Enter the second number: "))

                operations = {
                    '1': (addition, "+"),
                    '2': (subtraction, "-"),
                    '3': (multiplication, "*"),
                    '4': (division, "/"),
                    '7': (power, "^"),
                    '10': (modulo, "%"),
                    '11': (floor_division, "//")
                }
                operation, symbol = operations[choice]
                result = operation(number_1, number_2)
                print(f"{number_1} {symbol} {number_2} = {result}")
                history.append(f"{number_1} {symbol} {number_2} = {result}")
                last_result = result

            elif choice in ['5', '6', '8', '9']:  # Operations requiring one number
                if last_result is not None:
                    use_last_result = input("Use the last result? (y/n): ").lower()
                    if use_last_result == 'y':
                        number = last_result
                    else:
                        number = float(input("Enter a number: "))
                else:
                    number = float(input("Enter a number: "))

                if choice == '5':
                    result = square(number)
                    print(f"Square of {number} = {result}")
                elif choice == '6':
                    result = square_root(number)
                    print(f"Square root of {number} = {result}")
                elif choice == '8':
                    result = logarithm_base10(number)
                    print(f"Logarithm (base 10) of {number} = {result}")
                elif choice == '9':
                    result = factorial(number)
                    print(f"Factorial of {number} = {result}")

                history.append(f"Result: {result}")
                last_result = result

            elif choice == '16':  # Show history
                print(show_history())

            elif choice == '17':  # Clear history
                print(clear_history())
                last_result = None

            elif choice == '18':  # Exit
                print("--------------- Thank you for using the calculator ---------------")
                break

            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Invalid input, please enter a number.")
        except Exception as e:
            print(f"Error: {e}")

# Run the main function
if __name__ == "__main__":
    main()
