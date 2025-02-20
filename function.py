# #Typ1
# def greet():
#     print("Hello")
# greet()
#Typ2
# def greet(name):
#     print(f'Hello {name}')
# greet('John')
#Typ3
# def greet(name='John'): #default value / parameter is John
#     print(f'Hello {name}')
# greet('Alex')
# greet()

#Typ4
# def greet(name,time):
#     print(f'good {time} {name}')
# greet('morning','John')
# greet('evening','Alex')

#Typ5
# def greet(name,time):
#     print(f'good {time} {name}')
# greet(name='John',time='morning')

#Typ6
def greet(name='John',time='morning'):
    print(f'good {time} {name}')
greet(time='evening',name='Alex')
greet("evening","Alex") #positional argument