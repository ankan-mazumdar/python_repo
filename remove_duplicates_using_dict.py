def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)

#Create a dictionary, using the List items as keys. 
# This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
# Then, convert the dictionary back into a list: