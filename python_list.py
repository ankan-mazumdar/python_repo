''''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

'''


thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # replace

print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop() #The pop() method removes the specified index, (or the last item if index is not specified):
print("pop result")
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = list(("apple", "banana", "cherry")) #using list() constructor to create list
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #As nothing is mentioned as starting index. hence it will consider all items from beginning till the item before ending index

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])# it will start with 3rd element and end at last element.


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])# start from 4th last item=orange, include all items in sequence excluding the end item here its the last item.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x) #Another way to join two lists are by appending all the items from list2 into list1, one by one:

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2) #Use the extend() method to add list2 at the end of list1:
print(list1)
























