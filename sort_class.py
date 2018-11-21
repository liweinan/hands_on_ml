from collections import OrderedDict

class Student:
    def __init__(self, name, order):
        self.name = name
        self.order = order


tom = Student("Tom", 0)
jack = Student("Jack", 0)
rose = Student("Rose", 1)
lucy = Student("Lucy", 2)

users = OrderedDict()
users[rose.name] = rose
users[lucy.name] = lucy
users[jack.name] = jack
users[tom.name] = tom

# 接下来是转化users，让order变成key，然后让value是student数组

users2 = OrderedDict()

for k, v in users.items():
    if v.order not in users2.keys():
        users2[v.order] = []
    users2[v.order].append(v)

# 然后是sort这个数组，生成一个新的dict:

sorted_users = OrderedDict()

sorted_keys = sorted(users2)

for k in sorted_keys:
    for v in users2[k]:
        print(str(v.order) + ", " + v.name)
        sorted_users[v.name] = v

# 这样，我们就得到了sorted_users：
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")

for k, v in sorted_users.items():
    print(str(v.order) + ", " + k)
