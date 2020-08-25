thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #this will raise an error because the set no longer exists

thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.
