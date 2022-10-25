# my_list = ['Buddy', 'Roy', 'Ryan']

# print(my_list)

# my_list.append('Eric')
# print(my_list)
# # print(help(list))

# my_list.insert(1, "Nick")

# print(my_list)

# person = {'name': 'Jahmil', 'age': 30, 'hobbies': []}
# person['hobbies'].append('coding')
# person['hobbies'].append('twerking')
# print(person)
# print(person['age'])

# if "":
#     print("it worked")
# elif " ":
#     print("IDK")
# else:
#     print("no it didn't")

def say_hello(name, age=None):
    print(f'hello {name} you are {age} years old')
    return f'hello {name} you are {age} years old'
    
my_func = say_hello('Buddy')    

print('line 31', my_func)
