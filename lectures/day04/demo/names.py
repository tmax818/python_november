from faker import Faker

fake = Faker()

names = []

for i in range(100):
    dict = {}
    dict['first_name'] = fake.first_name()
    dict['last_name'] = fake.last_name()
    names.append(dict)

print(names)    
