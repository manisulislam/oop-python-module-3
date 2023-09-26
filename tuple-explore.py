things= 'paper', 'head phone', 'glass', 'book','phone','charger','scale'
items= ('pen','book')
print(things)

print(things[-2])
print(things[0])
print(things[2:5])

if 'glass' in things:
    print("exists")

for item in things:
    print(item)

print(len(things))