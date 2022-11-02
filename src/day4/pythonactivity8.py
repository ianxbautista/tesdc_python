import array as arr

athlete = []
sales = arr.array('d', [])
totalsales = 0
ctr = 0
ctr2 = 0
while ctr <= 4:
    ath = input(f'Enter Athlete {ctr + 1}: ')
    athlete.insert(ctr, ath)
    sale = float(input("Enter Sales: "))
    sales.insert(ctr, sale)
    totalsales += sales[ctr]
    ctr += 1


print("Top Sportsman")
print("=================")
print("Name        Sales")

while ctr2 <= 4:
    print(f'{athlete[ctr2]}     $'"{:.2f}".format(sales[ctr2]))
    ctr2 += 1


print("=================")
print(f'Total: ${totalsales}')

