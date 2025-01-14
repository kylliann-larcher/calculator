history = []

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
        return "Division by zero is not possible"

def square(number):
    return number ** 2

def square_root(number):
    if number >= 0:
        return number ** 0.5
    else:
        return "Square root of a negative number is not possible"

def display_history():
    if len(history) == 0:
        return "No history available"
    else:
        print("n\ -----------------calculation history-----------------")
        return history
    
def clear_history():
    history.clear()
    return "History cleared"

def menu():
    print("----------------------Welcome to the calculator-------------------")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square root")
    print("7. Display history")
    print("8. Clear history")
    print("9. Exit")

def calculator():
    while True:
        main()
        choice = input("Enter choice: ")
        
        if choice in ['1', '2', '3', '4']:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = addition(number_1, number_2)
                sign = "+"
            elif choice == '2':
                result = subtraction(number_1, number_2)
                sign = "-"
            elif choice == '3':
                result = multiplication(number_1, number_2)
                sign = "*"
            else:
                result = division(number_1, number_2)
                sign = "/"
                
            print(f"{number_1} {sign} {number_2} = {result}")
            history.append(f"{number_1} {sign} {number_2} = {result}")
            
        elif choice == '5':
            number = float(input("Enter number: "))
            result = square(number)
            print(f"{number}^2 = {result}")
            history.append(f"{number}^2 = {result}")
            
        elif choice == '6':
            number = float(input("Enter number: "))
            result = square_root(number)
            print(f"sqrt({number}) = {result}")
            history.append(f"sqrt({number}) = {result}")
            
        elif choice == '7':
            print(display_history())
            continue
            
        elif choice == '8':
            print(clear_history())
            
        elif choice == '9':
            print("---------------Thank you for using the calculator--------------")
            break
            
        else:
            print("Invalid input")