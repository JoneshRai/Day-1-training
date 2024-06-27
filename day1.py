#me = {
 #   'name' : "jonesh rai",
  #  'age' : 20,
   # 'address' : "Itahari"
#}

#print (me['age'])


friend = {
    'name' : 'gukkodalla',
    'age' : 90,
    'isnepali' : True
}

#del friend['age']
#print(friend)
#friend['isnepali'] = True

#print(friend['name'])
#print(friend['age'])

#print(friend.keys())
#print(friend.values())

#fruits = ['apple','banana','mango']
#for fruit in fruits: 
 #   print(fruit) 

#unique_numbers = {1,2,3,4,5}
#for number in unique_numbers:
 #       print(number)

students_grade = {
    'math' : 10,
    'physics' : 20,
    'nepali' : 30,
} 
#print(students_grade.values())
#print(students_grade.items())
#print(students_grade['math'])
#for student in students_grade:
 #   print(student,"scored", students_grade[student])

for student,grade in students_grade.items():
    print(student,"scored",grade)

for value in students_grade.values():
    print(value)

message = "this mcuh for today!"

for char in message:
    print(char)

