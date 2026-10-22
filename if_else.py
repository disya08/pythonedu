# x = 0
# if x > 0:
#     print("x is positive")
# elif x < 0:
#     print("x is negative")
# else:
#     print("x is null")


# x = 10
# y = -1
# if x > 0 and y > 0:
#     print("x and y are positive")
# else:
#     print ("some value isn`t positive")
        
my_string = input("Please, enter a number:")

if my_string.isdigit():
    my_integer = int(my_string)
    print(my_integer)
else:
    print(f"{my_string} is not a number")