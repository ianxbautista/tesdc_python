def calculatePerimeter(x, y):
    return (x + y) * 2


def calculateArea(x, y):
    return x * y


length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
perimeter = calculatePerimeter(length, width)
area = calculateArea(length, width)
print(f'Perimeter is ' "{:.2f}".format(perimeter))
print(f'Area is ' "{:.2f}".format(area))
