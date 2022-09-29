print("*****************STRING MANIPULATION********************")
# STRING Manipulations
print("hello world")
name= input("whats your name")
print("Hello {}!\nWelcome to DataQuest!" .format(name))
# Create new string
string = "This is string in Python"
# Let's get the first element
print(string[0])
# Let's get all the elements from index 3 to 8
print(string[3:9])
# Let's get the last but one element
print(string[-2])
# Let's get the number of symbols 
print("*****************SLICING********************")
#SLICING
#Given string "This is string for learning" assigned to variable test_str. You need to:
#Extract the very first and very last symbols.
#Extract word string.
#Get the length of this string.
# Create new variable
test_str = "This is string for learning"
print(test_str)
# Extract the very first and very last elements of this string
print("The first symbol of string:", test_str[0])
print("The last symbol of string:", test_str[-1])
# Extract the word string using slicing
print("Extracted word:", test_str[8:14])
# Get total number of symbols
print("Total number of symbols in test_str:", len(test_str))
print("*****************CONCATENATION********************")
#CONCATENATION
# Let's concatenate strings
print("I " + "can " + "concatenate " + "strings")
# Let's count number of a in specific string
s = "Linear discriminant analysis"
print(s.count("a"))
# Replicate string multiple times
print("test " * 5)

# Variables name and surname
name = "Alex"
surname = "Ferguson"
# Create variable fullname
fullname = name + " " + surname
# Print fullname
print("Full name:", fullname)
# Count number of letter e in fullname
print("Letter e is found in Fullname:", fullname.count("e"), "times")

print("*****************COMBINE CONDITION********************")
#Combining Conditions
# For example, let's check the following conditions:
# If 2 greater than 1 and "bbb" greater than "aaa"
# If the second index symbol in the string "my string" equals "y" or "s"

# Check the first two conditions
print(2 > 1 and "bbb" > "aaa")
# Check the next two conditions
print("my string"[2] == "y" or "my string"[2] == "s")

# Variable t
t = "Introduction to Python"
# Complete the first part of task
print(len(t) < 15 and t.count("n") > 2)

# Variable a
a = 89
# Complete the second part of task (Hint remainder use % to find)
print(a > 9475 / 37 or a % 14 < 7)

# Simple if/else Expressions
#Consider some examples: imagine you have a string and want to check if it's wide. Let's call a string 'wide' if it has more than 20 symbols.
# Assign some variable
test = "small string"

# Conditional statement
if(len(test) > 20):
    print("This string is wide!")
else:
    print("Nothing special")
    
# Check on different string
test = "This string is very-very and very large"

# Conditional statement
if(len(test) > 20):
    print("This string is wide!")
else:
    print("Nothing special")

#Assume you own a small grocery and your expense is 2000 dollars every day. Obviously, if your revenue per day is less than 2000, then you suffer losses, otherwise - you're making money. Let's try to write if/else statement for that.
revenue = 2000

# Check if revenue is less than 2000
if(revenue < 2000):
  # Output We suffer losses!
  print("Output We suffer losses!")
else:
  # Output Everything is ok!
  print("Everything is ok!")


  #You are given number num. Using if/else, print the message "The number num is odd" if num is odd, and "The number num is even" if num is even. Do it by replacing the ___ parts within print() functions with respective text ('odd' or 'even').

# Define if/else construction
num = 8941 % 931
if(num % 2):
  # Print message below
  print("The number num is", "odd")
else:
  # Print another message below
  print("The number num is", "even")
