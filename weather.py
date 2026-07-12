weather_tuple = (1, 1, 0, 0, 0 ,1, 1, 1, 0)

rainchance = 0
sunchance = 0

for i in weather_tuple:
    if i == 0:
        sunchance += 1
    else:
        rainchance += 1

if rainchance > sunchance:
    print("It is rainy")
elif sunchance > rainchance:
    print("It is sunny")
else:
    print("Sunny or rainy")
