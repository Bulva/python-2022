def function_name(retezec1, retezec2):
    print(retezec1, retezec2)

function_name('Ahoj', 'Petře')
function_name('Ahoj', 'Jirko')
function_name('Ahoj', 'Davide')


def sum(n1, n2):
    sum = n1 + n2
    return sum


soucet = sum(1, 2)
print(soucet)


def concate(*args):
    print(args)

concate('Ahoj', 'Marku', False)


# age, eye_color, name
def create_person(**kwargs):
    print(kwargs)

create_person(name='Honza', eye_color='modrá', age=20)


def create_person(name, eye_color, age, kind=True):
    return {
        'name': name,
        'eye_color': eye_color,
        'age': age,
        'kind': kind
    }

print(create_person('Honza', 'modrá', 20))
print(create_person('Honza', 'modrá', 20, kind=False))
