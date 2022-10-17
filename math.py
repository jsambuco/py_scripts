# Find Numbers Divisible by Another Number
# In Python, an anonymous function is a function that is defined without a name.
# While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
# anonymous functions are also called lambda functions.

# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]

# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))

# display the result
print("Numbers divisible by 13 are",result)

# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))


# Reverse a Number using a while loop
num = 1234
reversed_num = 0
print ("Standard Number: " + str(num))
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))