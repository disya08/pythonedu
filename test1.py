Name = input("Please, write your name")

if Name.isalfa():
    print("Incorrect form")
else:
        print("Okay")
Age = input("Please, write your age")
if Age.isdigit():
    print("Okay")
else:
    print("Incorrect form")

print(f"Hello, my name is {Name} and I`m {Age} years old! Nice to meet you.")