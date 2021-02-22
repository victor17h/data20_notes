str_var = 'Hello'
int_var = 5
float_var = 2.3

print(type(str_var))
print(type(int_var))
print(type(float_var))

#####

print('What is your age?')
#age = input()

#print(age)
#print(type(age))

#####

hello = "Hello World"

print(hello[6:10])

hello = 'Hello World             '

print(hello.strip())
print(hello.count(hello))
print(hello.upper())
print(hello.lower())

hello = 'hello'
name = 'jenny'
age = '11'

print(f"{hello} {name} you are {age} years old")

hi = "Hello everyone"
print(hi.isalpha())
print(name.islower())
print(age.islower())

#####

x = None
y = False

print(bool(x))
print(bool(y))
print(x == False)
print(y == False)
print(x == True)

##### lists

shopping_list = ["cheese", "avocados", "apples", "bread", "ham"]
shopping_list[0] = "milk"

print(shopping_list)
print(type(shopping_list))
shopping_list.append("sugar")
shopping_list.remove("avocados")
print(shopping_list)
shopping_list = ["cheese", "avocados", "apples", "bread", "ham"]
print(shopping_list[:2])
print(shopping_list[1::2])

##### tuples

shopping_tup = ("cheese", "avocados", "apples", "bread", "ham")
print(shopping_tup)
print(type(shopping_tup))
print(shopping_list[0])

#### dictionaries

new_dict = {"my_key": "values", "num": 3,
            "key_list": ["val1", "val2", "val3"]}

print(new_dict)
print(new_dict["num"])
print(new_dict['key_list'][0])
print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())
new_dict["my_key"] = "something else"
print(new_dict)

#####

num = 11

if num == 10:
    print("number is 10")
elif num > 10:
    print("num is greater than 10")
else:
    print("number is not 10")

##### iterate in a dictionary

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3],[4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"},
             2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

for num in embedded_lists:
    for num2 in num:
        print(num2, end=" ")

for x in dict_data:
    print(x)

for x in dict_data.values():
    print(x)
    for y in x.values():
        print(y)

##### while loop

x = 0

while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1

##### function

def my_function(number1 = 3, number2 = 4):
    print(f"your input was {number1} and {number2}")
    return number1 + number2

print(my_function(4, 5))

def my_add_func(*multiargs):
    print(multiargs)
    print(type(multiargs))
    for arg in multiargs:
        print(arg)

my_add_func(3, "dafad", ["hello", 5])