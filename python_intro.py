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

