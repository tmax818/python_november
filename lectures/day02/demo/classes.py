

from time import perf_counter


person = {'name': 'Tyler', 'age': 39}

person_list = ['Tyler', 39, True]
person_list = [
    {'name': 'Tyler', 'age': 39},
    {'name': 'Tyler', 'age': 29},
    {'name': 'John', 'age': 29},
    ]

print(person_list[1])

def find_tyer(age, name):
    for person in person_list:
        if person['age'] == age and person['name'] == name:
            print(person)

# print(type(person))
# print(type(person_list))


# print(person_list[0])