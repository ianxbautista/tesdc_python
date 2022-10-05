StringName = input(f'Enter String: ')
NumofTimes = int(input(f'Enter number of times: '))
count = 1

if NumofTimes > 0:

    while count <= NumofTimes:
        print(StringName)
        count += 1
else:
    print(f'Invalid Input, Program Ends')