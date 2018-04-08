"""students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def fullname(list):
    for i in range(0,len(list)):
        print list[i]["first_name"], list[i]["last_name"]


fullname(students)"""

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}



def names(dict):
    
    for key, data in dict.items():
        count = 0
        print key
        for value in data:
            count +=1
            print str(count), "-", value["first_name"], value["last_name"], "-", str(len(value["first_name"]+value["last_name"]))
        

names(users)