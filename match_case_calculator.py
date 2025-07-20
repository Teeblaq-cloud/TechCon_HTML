num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = input('choose an operation (+, -, *, /): ')
match operation:
    case '+':
        print('The result is:', num1 + num2)

    case '-':
        print('The result is:', num1 - num2)
   
    case '*':
        print('The result is:', num1 * num2)

    case '/':
        if num2 != 0:
            print('The result is:', num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")