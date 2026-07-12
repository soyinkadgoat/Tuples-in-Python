tuple1 = (2, 4, 6, 8, 10, 5)
tuple2 = (1, 3, 5, 7, 9, 4)

product = 1

for i in tuple1:
    for j in tuple2:
        product += i * j
print(product)