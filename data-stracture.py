# lists

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
zero = [0] * 50
combined = matrix + zero
print(combined)
number = list(range(20))

letters = ["a","b","c","D"]
letters[0] = "A"
print(letters[:])
print(letters[::2])
numbers = list(range(20))
print(list(numbers[::-1]))
print(list(numbers[::2]))

# list unpacking

numbers = [1,2,3]

first = numbers[0]
second = numbers[1]
third = numbers[2]

first,second, *other = numbers
first, *other, last = numbers

# loop list

letters = ["a","b", "c"]
for letter in letters:
    print(letter)

for letter in enumerate(letters):
    print(letter[0])

for index, letter in enumerate(letters):
    print(index, letter)

# Add item to the list  to the end
letters.append("d")
print(letters)
letters.insert(0, "-")
print(letters)

# remove
letters.pop()
print(letters)
letters.pop(0)
print(letters)
letters.remove("b") # it remove the rist letter of the the in the list
print(letters)
del letters[0:3]
print(letters)
letters.clear()
print(letters)


# find items
letters = ["a", "b", "c"]
if "d" in letters:
    print(letters.index("d"))

# sorting list
numbers = [3,51,2,8,6]
numbers.sort()
numbers.sort(reverse=True)
numbers.sorted(numbers, reverse=True)
# lambda function

# lambda parameters:expression
# we use lamda function for only to use as argument for another function

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
items.sort(key=lambda item: item[1])
print(items)


# map fuction

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
prices = []
for item in items:
    prices.append(item[1])

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
prices = list(map(lambda item: item[1], items))
print(prices)




