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
print("Letter e is found in fullname:", fullname.count("e"), "times")


