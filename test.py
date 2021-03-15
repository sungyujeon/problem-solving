import math

r = 5.72

x1 = 0.0
y1 = 0.0

x2 = 1.0
y2 = 1.0

# btw = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
# btw2 = math.sqrt((btw ** 2) - ((2*r) ** 2))

d1 = math.degrees(math.atan((x2-x1) / (y2-y1)))
print(f'탄젠트:{d1}')

height = math.sqrt(2) * math.sin(math.radians(45.0))
print(f'height: {height}')

# print(math.degrees(math.atan2(1, 1)))

# d2 = math.degree(math.atan((2*r)/btw2))

# tan theta = y / x
# theta = cotan(x/y)