result = 0
number = 1
while number > 0:
    number = int(input(f'Enter number [enter a (-) value to exit]: '))
    if number < 0:
        print(f'Exiting')
    else:
        result = result + number
        print(result)
print(f'Bye!')