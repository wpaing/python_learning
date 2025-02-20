country = {}
while True:
    name=str(input('Enter City : '))
    population=int(input('Enter Population : '))
    country[name] = population
    print(country)
    add_another = input("Do you want to add another city? (yes/no) : ")
    if add_another == "yes" :
        continue
    else: 
        break
population=list(country.values())
for pop in set(population):
    count=population.count(pop)
    print(f'{pop} population  - {count} city')