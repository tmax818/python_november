x = [ [5,2,3], [10,8,9] ] 

print(x[1])
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print(type(z))
print(type(z[0]))
print(z[0]['y'])
z[0]['y'] = 30
print(z[0]['y'])


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
students2 = [
         {'first_name':  'Ricky', 'last_name' : 'Gonzalez'},
         {'first_name' : 'Tyler', 'last_name' : 'Maxwell'},

    ]

def iterateDictionary(listParam):
    for student in listParam:
        print(student)
 
iterateDictionary(students) 
iterateDictionary(students2) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
