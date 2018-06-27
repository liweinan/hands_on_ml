import random

list = []

for i in range(10):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    list.append("{0} + {1} =".format(x, y))

for i in range(10):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    list.append("{0} + {1} =".format(x, y))

for i in range(10):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
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

for i in range(10):
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    z = random.randint(1, 9)
    r = (x + y) * z
    list.append("({0} + {1}) × {2} =".format(x, y, z))

for i in range(10):
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    if x == y:
        x = x + 1
    if x < y:
        x, y = y, x
    z = random.randint(1, 9)
    r = (x - y) * z
    list.append("{0} ÷ ({1} - {2}) =".format(r, x, y))

for i in range(10):
    x = random.randint(1, 2)
    y = random.randint(1, 5)
    z = random.randint(1, 9)
    r = x * y * z
    list.append("{0} ÷ ({1} × {2}) =".format(r, x, y))

random.shuffle(list)

for i in range(len(list)):
    print("{0}{1}".format("{0}{1}".format(str(i + 1), ")").ljust(5), list[i]))
