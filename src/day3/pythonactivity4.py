ProductName = input(f'Enter Product Name: ')
ProductPrice = float(input(f'Enter Product Price: '))

DiscountRate = 0
Discount = 0
NetPrice = 0

if 0 <= ProductPrice <= 10000:
    DiscountRate = 0
elif 10001 <= ProductPrice <= 20000:
    DiscountRate = 0.05
elif 20001 <= ProductPrice <= 50000:
    DiscountRate = 0.1
elif 50001 <= ProductPrice <= 100000:
    DiscountRate = 0.15
elif ProductPrice >= 100001:
    DiscountRate = 0.2
else:
    DiscountRate = 0

Discount = ProductPrice * DiscountRate
NetPrice = ProductPrice - Discount

print(f'Price of {ProductName} is '"{:.2f}".format(ProductPrice))
print(f'Discount is ' "{:.2f}".format(Discount))
print(f'Net Price is '"{:.2f}".format(NetPrice))