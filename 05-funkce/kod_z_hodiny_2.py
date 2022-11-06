list comprehension
l = [1, 1, 1, 1]
l2 = [x+1 for x in l]
print(l2)
l2 = []

for x in l:
    l2.append(x+1)

print(l2)

def sum(x: int, y: int) -> int:
    return x + y

my_sum = sum(100, 1000)
print(sum)
print(sum(100, 1000))
print(my_sum)
print(type(sum(100, 1000)))

numbers = [1, 34, 3423, 2312, 8789]
numbers2 = [3423, 2312, 8789]


def sum(nums: list) -> int:
    sum = 0
    for x in nums:
        sum += x
    return sum

print(sum(numbers))

def sum(*args):
    print(type(args))
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum(1, 2, 3))

print('ahoj', 'jak', 'se', 'máš', end='.', sep=';')

def create_people(skill: str, name: str = 'Honza') -> dict:
    return {'name': name, 'skill': skill}


print(create_people('kominík', name='Jirka'))


def sum(**kwargs):
    print(type(kwargs))
    print(kwargs)


sum(cislo1=1, cislo2=2)
