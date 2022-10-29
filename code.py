# import math
# course = " hello \"world"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())  # remove white space rstirp,lstrip
# print(course.find("o"))  # find the index of the first occurence of the character
# # replace the first argument with the second argument
# print(course.replace("world", "universe"))
# # check if the first argument is in the second argument
# print("hello" in course)
# # check if the first argument is not in the second argument")
# print("swfit" not in course)
# courses = " hello \\world"  # to print \ we need to use \\ (\n  new line)
# print(course)
# print(course.upper())
# print(course.lower())
# print(course[:3])
# print(course[3:])
# print(course[3:7])
# # in python three type of numbers
# # int
# # float
# # complex
# x = 1
# x = 1.1
# x = 1 + 2j
# print(type(x))
# # type casting
# print(10//3)  # floor division
# print(10 % 3)  # modulus
# print(10**3)  # exponent
# print(round(2.9))  # rounding
# print(abs(-2.9))  # absolute value
# print(math.ceil(2.2))  # round up
# x = int(input("x: "))
# y = int(input("y: "))
# print(x + y)
# print(f"{x} + {y} = {x + y}")
# bool(0)
# bool(1)
# bool(-1)
# 10 > 3  # true
# 10 < 3  # false
# 10 == 3  # false
# 10 != 3  # true
# 10 >= 3  # true
# 10 == "10"  # false
# "bag" > "apple"  # true becasue of sort order
# # false  because of case sensitive and ord("b") 98 and ord("B") 66
# "bag" == "Bag"


# # format string
# first = "john"
# last = "smith"
# message = first + " [" + last + "] is a coder"  # concatenation
# msg = f'{len(first)} [{last} {2+2}] is a coder'  # format string


# temperature = 30
# if temperature > 30:
#     print("it's a hot day")
# elif temperature > 20:
#     print("it's a nice day")


# #  ternary operator
# age = 22
# message = "eligible" if age >= 18 else "not eligible"

# # logical operator
# # and, or, not
# high_income = True
# good_credit = True
# student = False
# if high_income and good_credit:
#     print("eligible")

# if (high_income or good_credit) and not student:
#     print("eligible")


# # chainig comparison operator
# age = 22
# if 18 <= age < 65:
#     print("eligible")
# # instade
# if age >= 18 and age < 65:
#     print("eligible")


# # for loop

# for number in range(1, 11, 2):
#     print("attempt", number, number * ".")
# # for loop with else
# successful = True
# for number in range(3):
#     print("attempt")
#     if successful:
#         print("successful")
#         break


# # nested loop
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# # iterable
# for x in [1, 2, 3, 4, 5]:
#     print(x)
# print(type(x))

# for x in "hello":
#     print(x)

# for x in range(5):
#     print(x)
# shopping_cart = ["milk", "pasta", "egg", "spam", "bread", "rice"]
# for item in shopping_cart:
#     if item == "spam":
#         continue
#     print("buy " + item)

# # while loop
# i = 1
# while i <= 5:
#     print("*" * i)
#     i //= 2
# print("done")

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# # infinite loop
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break
# y = 0
# for x in range(1, 10):

#     if x % 2 == 0:
#         print(x)
#         y += 1
# print(y)

# # function


# def greet(name):
#     # 1. function perform a task
#     print(f"hello {name}")
#     print("welcome aboard")


# # there are two type of function
# # 1. function perform a task
# # 2. function return a value
# round(2.9)  # return a value


# # keyword argument

# def increment(number, by):
#     return number + by


# print(increment(2, by=1))  # by is keyword argument

# # default argument
# def increment(number, by=1): # default parameter should be at the end of the parameter in the function
#     return number + by

# print(increment(2))  # by is keyword argument
# print(increment(2, 5))  # by is keyword argument

# # multiple argument 
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
# print(multiply(2, 3, 4, 5))

# # multiple keyword argument
# def save_user(**user):
#     print(user)
#     print(user["id"])
# save_user(id=1, name="john", age=22)

def fizz_buzz(input):
    if (input %3 ==0 and input %5 ==0):
        return "fizzbuzz"
    elif input %3 ==0:
        return "fizz"
    elif input %5 ==0:
        return "buzz"
    else :
        return input
print(fizz_buzz(15))
    


