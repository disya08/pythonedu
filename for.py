# file_names = ['document.txt', 'image1.jpg', 'document2.txt', 'image2.jpg']
# for file_name in file_names:
#     print(file_name)

# greeting = "Hello, world!"
# count_o = 0
# for char in greeting:
#     if char == 'o':
#         count_o += 1
# print(count_o)


# students = ['Alice', 'Bob', 'Mark', 'David']
# for student in students:
#     print(student)
#     for char in student:
#         print(char)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# odd_num = 0
# for number in numbers:
#     if number % 2 > 0:
#         print(number)
#         odd_num += 1
# print(f"count of odd numbers is {odd_num}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for number in numbers:
#     if number % 2 == 0:
#         continue
#     print(number)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for number in numbers:
#     if number == 10:
#         break
#     print(number)

# range_object = range(10)
# print(range_object)
# numbers = list(range_object)
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(len(numbers)):
#     numbers[i] += 1

# print(numbers)

greeting = 'Hello, world!'
indexes = []
count = 0
for i in range(len(greeting)):
    if greeting[i] == 'o':
        count += 1
        indexes.append(i)

print(count)
print(indexes)

    