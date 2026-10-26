# numbers_1 = [1, 2, 3, 4, 5]


# def find_average(numbers):
#      average = sum(numbers) / len(numbers)
#      return average

# average_1 = find_average(numbers_1)
# print(average_1)

# def count_vowels(string):
#     VOWELS = 'AEIOUYaeiouy'
#     count = 0
#     for char in string:
#         if char in VOWELS:
#             count += 1


#     return count

# print(count_vowels("Hello, world!"))
# print(count_vowels("Python is a very powerful language"))

# def nothing():
#     pass


# nothing()

# def format_date(day: int, month : str) -> str:
#     return f"Today is {day} of {month}"

# print(format_date(26, 'October'))

def custom_greeting(name: str, greeting: str = 'Hello') -> str:
    return f"{greeting} {name}!"

print(custom_greeting('Denis'))
 