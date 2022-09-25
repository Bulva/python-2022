# Napiste funkci, ktera na vstupu dostane
# libovolne velky neprazdny seznam (list, pole) cisel a vrati
# jejich soucet

def sum(values:list):
    sum = 0
    for v in values:
        sum += v
    return sum


print(sum([1, 23, 28893, 98]))

l = [1, 23, 28893, 98]
print(sum(l))
