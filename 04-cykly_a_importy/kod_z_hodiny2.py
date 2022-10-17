import random as rd
from random import randint

print(random.randint(1, 10))
print(rd.randint(1, 10))
print(randint(1, 10))

ls = [1, 3, 5, 87]

for i in ls:
    print(i)

dic = {
    'name': 'Honza',
    'age': 20
}

for k in dic:
    print(dic[k])

k, v = input('neco'), input('neco2')
for k, v in dic.items(): #(key: value)
    print(k, v)

from random import randint


num = 0
while num < 10:
    num += 1  # num = num + 1
    print(num)

num = 10
while True:
    num2 = randint(1, 11)
    print(num2)
    if num == num2:
        break