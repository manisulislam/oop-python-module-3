person={"name": "anis", "age": 23," address": "baborer bari"}
print(person)

print(person.keys())
print(person.values())
person["language"]="python"
person["name"]=["anisul islam"]
print(person)

numbers_enumerate=[14,25,236,25,65,96,52]
for i, v in enumerate(numbers_enumerate):
    print(i, v)