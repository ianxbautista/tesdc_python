import array as arr

numbers = arr.array('i', [5, 10, 1, 12, 13])

ctr = 0
while ctr < len(numbers):
    print(numbers[ctr])
    ctr += 1
print("Loop Done")