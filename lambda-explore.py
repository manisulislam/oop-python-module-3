def double(x):
    return x*2

# result= double(20)

doubled = lambda num : num * 2
squared =  lambda num : num * num
result = doubled(65)
square_result= squared(85)
print(result)
print(square_result)

add = lambda x,y : x+y
sum = add(10,20)
print(sum)


# map 
numbers= [10,20,60,40,50,95]
numbers_nums= map (doubled, numbers)
print(numbers)
print(list(numbers_nums))

# filter
actors = [
    {"name": "a", "age": 56},
    {"name": "b", "age": 25},
    {"name": "c", "age": 26},
    {"name": "d", "age": 60},
]

juniors = filter( lambda actor : actor["age"] < 30, actors)
fivers = filter (lambda actor : actor["age"] %5==0, actors)
print(list(juniors))
print(list(fivers))