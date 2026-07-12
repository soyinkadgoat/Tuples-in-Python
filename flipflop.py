tuple1 = (5, 3, 9, 9, 3, 5)
print(tuple1)

reversedtuple = ()

for i in tuple1:
    reversedtuple = (i, ) + reversedtuple

print(reversedtuple)

if reversedtuple == tuple1:
    print("it is a palindrome")