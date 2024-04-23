from copy import copy

countries = ["United States", "Canada", "Poland", "Germany", "Austria"]

nations1 = countries[:]
nations2 = countries.copy()
nations3 = copy(countries)
nations4 = countries
del nations4[0]

print(nations1)
print(nations2)
print(nations3)
# ['United States', 'Canada', 'Poland', 'Germany', 'Austria']
print(nations4)
# ['Canada', 'Poland', 'Germany', 'Austria']
print(countries)
# ['Canada', 'Poland', 'Germany', 'Austria']



