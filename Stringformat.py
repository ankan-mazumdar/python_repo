# String format()
# String Methods
# Python has a set of built-in methods that you can use on strings.

# Note: All string methods returns new values. They do not change the original string.

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

# The format() method allows you to format selected parts of a string.

# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

# Example
# Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))
# You can add parameters inside the curly brackets to specify how to convert the value:

# Example
# Format the price to be displayed as a number with two decimals:

txt = "The price is {:.2f} dollars"
print(txt.format(price))
# Check out all formatting types in our String format() Reference.

# Multiple Values
# If you want to use more values, just add more values to the format() method:

# print(txt.format(price, itemno, count))
# And add more placeholders:

# Example
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

# Example
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# Also, if you want to refer to the same value more than once, use the index number:

# Example
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

# Example
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

