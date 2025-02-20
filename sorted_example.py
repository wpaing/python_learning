person =  {}
while True:
    name=str(input('Enter Name : '))
    age=int(input('Enter Age : '))
    person[name] = age

    another = input("Do you want to add another person? (yes/no) : ")
    if another == "yes" :
        continue
    else: 
        break

ages=list(person.values())
for age in set(ages):
    count=ages.count(age)
    print(f'{age} years old  - {count} person')