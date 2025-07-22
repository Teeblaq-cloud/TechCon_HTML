num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operator = input('Enter the operator (+, -, *, /): ')
match operator:
    case '+':
        print(f'The result is: {num1 + num2}.')
    case '-':
        print(f'The result is: {num1 - num2}.')
    case '*':
        print(f'The result is: {num1 * num2}.')
    case '/':
        print(f'The result is: {num1 / num2}.' if num2 != 0 else 'Error: Division by zero .')
    case _:
        print('Invalid operator')