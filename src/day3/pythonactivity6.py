number = int(input(f'Enter Number: '))
exponent = int(input(f'Enter Exponent: '))
count = 1
numexp = 1
while count <= exponent:
    numexp *= number
    count += 1
print(f'{number} raised to {exponent} is {numexp}')