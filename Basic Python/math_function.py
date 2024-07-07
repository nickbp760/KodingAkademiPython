import math
y= 15
x = (math.sqrt(5 ** 2) / (y + 1)) + 2 * y ** 2
print(x)


a, b, c = 1, 8, 12
diskriminan = b ** 2 - 4 * a * c
akar_diskriminan = math.sqrt(diskriminan)
x1 = (-b + akar_diskriminan) / (2 * a)
x2 = (-b - akar_diskriminan) / (2 * a)
print(x1, x2)