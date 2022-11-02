numbers = []
ctr = 0
while ctr < 5:
    num = int(input(f"Enter Number {ctr + 1}: "))
    numbers.insert(ctr, num)
    ctr += 1
print("loop done")

print(f"Displaying Input: {numbers}")