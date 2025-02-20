person={
    "name":"Aung Aung",
    "age":30,
    "country":"Myanmar"
}
#add key value
# person['city']='Yangon'
#remove key value
# person.pop('country')
#update key value
person['name']='Maung Maung'
# print(person)


#  in condition
# if 'name' in person: #True  
#     print('Working')
person_key=list(person.keys());
print(person_key)

person_value=list(person.values());
print(person_value)