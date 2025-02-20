# names = ['Heroku','oracle', 'aws', 'gcp', 'azure', 'ibm']
# for name in names :
#    if name == 'aws' :
#       print(f'{name} is the best cloud provider')
#       break #break the loop when the condition is met
#    else: 
#       print(f'{name} is not the best cloud provider')
    
# fruits = ['apple', 'banana', 'mango', 'orange', 'grape']
# for fruit in fruits:
# #    print(f'{fruit} is a fruit')
#     if fruit ==  'orange' :
#         print(f'{fruit} is my favorite fruit')
#         continue
#     else:
#         print(f'{fruit} is not my favorite fruit')

#While loop
num = 0
while num < 10:
    if num == 5:
        break
    if num % 2 == 0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an odd number')
    num += 1