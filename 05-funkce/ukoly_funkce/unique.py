# napiste funkci, ktera na vstupu bude
# mit seznam hodnot a na vystupu vrati
# seznam unikatnich hodnot

def unique(*args):
    return list(set(args))

def unique_hard(*args) -> list:
    u = []
    for v in args:
        if not v in u:
            u.append(v)
    return u

print(unique(1, 1, 1, 2, 22, 'Honza', 'Honza', 'Jirka'))
print(unique_hard(1, 1, 1, 2, 22, 'Honza', 'Honza', 'Jirka'))