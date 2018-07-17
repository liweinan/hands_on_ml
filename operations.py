import random
import math


def roundup(x):
    return int(math.ceil(x / 100.0)) * 100


list = []

for i in range(8):
    x = random.randint(5, 10)
    y = random.randint(5, 10)
    list.append("{0} + {1} =".format(x, y))

for i in range(8):
    x = random.randint(10, 50)
    y = random.randint(10, 50)
    list.append("{0} + {1} =".format(x, y))

# 千位和百位的加减法3道，百位需要是整数
for i in range(2):
    x = roundup(random.randint(100, 499))
    y = roundup(random.randint(100, 499))
    list.append("{0} + {1} =".format(x, y))

for i in range(2):
    x = roundup(random.randint(499, 4999))
    y = roundup(random.randint(499, 4999))
    list.append("{0} + {1} =".format(x, y))

# 除法两道，带余数
for i in range(2):
    x = random.randint(1, 8)
    y = random.randint(1, 9)
    m = random.randint(1, 9)
    z = x * y + m
    list.append("{0} ÷ {1} =".format(z, y))


for i in range(18):
    x = random.randint(10, 99)
    y = random.randint(10, 50)
    if x < y:
        x, y = y, x
    list.append("{0} - {1} =".format(x, y))

for i in range(20):
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    z = x * y
    list.append("{0} ÷ {1} =".format(z, y))

for i in range(20):
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    list.append("{0} × {1} =".format(x, y))

for i in range(7):
    x = random.randint(1, 4)
    y = random.randint(1, 5)
    z = random.randint(1, 9)
    r = (x + y) * z
    list.append("({0} + {1}) × {2} =".format(x, y, z))

for i in range(7):
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    if x == y:
        x = x + 1
    if x < y:
        x, y = y, x
    z = random.randint(1, 9)
    r = (x - y) * z
    list.append("{0} ÷ ({1} - {2}) =".format(r, x, y))

for i in range(6):
    x = random.randint(1, 2)
    y = random.randint(1, 3)
    z = random.randint(1, 3)
    r = x * y * z
    list.append("{0} ÷ ({1} × {2}) =".format(r, x, y))

random.shuffle(list)

for i in range(len(list)):
    print("{0}{1}".format("{0}{1}".format(str(i + 1), ")").ljust(5), list[i]))
