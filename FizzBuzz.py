# for number in range(1, 101):
#     if number % 15 == 0:
#         print(number, "FizzBuzz")
#     elif number % 3 == 0:
#         print(number, "Fizz")
#     elif number % 5 == 0:
#         print(number, "Buzz")
#     else:
#         print(number)


num_start = int(input("Where does it start? "))
num_end = int(input("Where does it end? "))

def fizzbuzz(num_start, num_end):
    for number in range(num_start, num_end + 1):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

print(fizzbuzz(num_start, num_end))

