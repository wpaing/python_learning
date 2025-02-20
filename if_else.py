# age = int(input('Enter your age: '))
# if age < 18:
#     print('You are a minor')
# elif age >18 and age < 30:
#     print('You are a youth')
# else:
#     print('You are an adult')

# tired = input('Are you tried? "(y/n)"')
# if tired == 'y':
#     print('Go to bed')
# elif tired == 'n':
#     print('Go to work')
# else:
#     print('Type y or n')
username='admin'
password=1234
username = str(input('Enter username: '))
password = int(input('Enter password: '))
if username == 'admin' and password == 1234:
    print('Welcome admin user')
elif username == 'admin' and password != 1234:
    print('Invalid password')
elif username != 'admin' and password == 1234:
    print('Invalid username')
else:
    print('Invalid username or password')