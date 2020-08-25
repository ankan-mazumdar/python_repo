thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print(thistuple[-1])

thistuple = ("apple", "banana", "cherry")
# thistuple[1] = "blackcurrant" #'tuple' object does not support item assignment, non-changebale
# the value is still the same:
print(thistuple)    

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple",) # add a comma after the item 
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
x=tuple3.count(2) #	Returns the number of times a specified value occurs in a tuple
print(x)
y=tuple3.index(2) #Searches the tuple value and returns the position of where it was found
print(y)
