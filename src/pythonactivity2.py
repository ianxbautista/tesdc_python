mathgrade = input("enter your grade in math: ")
enggrade = input("enter your grade in english: ")
filgrade = input("enter your grade in filipino: ")
average = (float(mathgrade) + float(enggrade) + float(filgrade)) / 3
print(f'your Average grade is ' "{:.2f}".format(average))