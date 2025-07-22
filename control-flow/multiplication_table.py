User = input('Enter a number to see its multiplication table: ')
number = int(User)
for i in range(1, 11):
    result = number * i
    print(f'{number} x {i} = {number}')  # Using f-string for formatted output