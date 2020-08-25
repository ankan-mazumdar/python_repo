# # In Python we have lists that serve the purpose of arrays, but they are slow to process.

# # NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.

# # The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# # Arrays are very frequently used in data science, where speed and resources are very important.
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

import numpy as np
print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr = np.array((1, 2, 3, 4, 5))#Use a tuple to create a NumPy array:
print(arr)

arr = np.array(42) #0-D
print(arr)
print(arr.ndim)

arr = np.array([1, 2, 3, 4, 5]) #1-D
print(arr)
print(arr.ndim)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(arr.ndim)



# Create an array with 5 dimensions and verify that it has 5 dimensions:
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

# In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, 
# the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.

arr = np.array([1, 2, 3, 4])
print(arr[1])
print(arr[2] + arr[3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1])
print('5th element on 2nd dim: ', arr[1, 4])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print (arr[1]) #print the whole 2nd dim array 
# print (arr[1, 2]) #print the 3rd element of  2nd dim array, but 2nd dim contains only 2 elements, hence throws an error-index 2 is out of bounds for axis 1 with size 2
print (arr[1, 1]) #print the 2nd element of  2 dim array
print (arr[1,1, 1]) # print the 2nd value contained in 2nd element of 2nd dim array
print(arr[0, 1, 2])
print(arr.ndim)
print('Last element from 2nd dim: ', arr[1, -1])

#Slicing arrays
#Slicing in python means taking elements from one given index to another given index.
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].
#If we don't pass start its considered 0
#If we don't pass end its considered length of array in that dimension
#If we don't pass step its considered 1

#Example
#Slice elements from index 1 to index 5 from the following array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[-1:-3])
#print(arr[::0])# return error slice step cannot be zero
print(arr[::1])
print(arr[::2]) #Return every other element from the entire array:
print(arr[::3])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0:2, 2]) #From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:


# By default Python have these data types:

# strings - used to represent text data, the text is given under quote marks. eg. "ABCD"
# integer - used to represent integer numbers. eg. -1, -2, -3
# float - used to represent real numbers. eg. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent a number in complex plain. eg. 1.0 + 2.0j, 1.5 + 2.5j
# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr)
print(arr.dtype) #U6' string

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype) #Create an array with data type string:

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# arr = np.array(['a', '2', '3'], dtype='i') A non integer string like 'a' can not be converted to integer (will raise an error):

arr = np.array([1.1, 2.1, 3.1])
print(arr)
print(arr.dtype)

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
print(arr)
print(arr.dtype)
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)


# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31 #make changes in the view

print(arr)#The original array SHOULD be affected by the changes made to the view.
print(x)


# Print the value of the base attribute to check if an array owns it's data or not:
#copies owns the data, and views does not own the data,

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
# The copy returns None.
# The view returns the original array.

# Print the shape of a 2-D array:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
# The example above returns (2, 4), which means that the array has 2 dimensions, and each dimension has 4 elements.
# Example
# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)


# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
# Can We Reshape Into any Shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.
# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.

# Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3) # ValueError: cannot reshape array of size 8 into shape (3,3)

# Check if the returned array is a copy or a view:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)
# The example above returns the original array, so it is a view.

# Unknown Dimension
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.

# Example
# Convert 1D array with 8 elements to 3D array with 2x2 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
# Note: We can not pass -1 to more than one dimension.

# Flattening array means converting a multidimensional array into a 1D array
# We can use reshape(-1) to do this.
# Example
# Convert the array into a 1D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
# Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.


# Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3])

for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)     

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

# Iterate through every scalar element of the 2D array skipping 1 element:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

  #Join two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

#Join two 2-D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

#Joining Arrays Using Stack Functions
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# Stacking Along Rows
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)
arr = np.vstack((arr1, arr2))
print(arr)

# stack() to stack along height, which is the same as depth.
arr = np.dstack((arr1, arr2))
print(arr)

# Split the array in 3 parts:
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
newarr = np.array_split(arr, 8)
print(newarr)
newarr = np.array_split(arr, 4)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

# Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

# Split the 2-D array into three 2-D arrays along rows.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
# hsplit() method to split the 2-D array into three 2-D arrays along rows.
newarr = np.hsplit(arr, 3)
print(newarr)

# Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
x = np.where(arr%2 == 0) #Find the indexes where the values are even:
print(x)
x = np.where(arr%2 == 1)
print(x) #Find the indexes where the values are odd
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
x = np.searchsorted(arr, 7, side='right')#Find the indexes where the value 7 should be inserted, starting from the right:
print(x)
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])#Find the indexes where the values 2, 4, and 6 should be inserted:
# return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.
print(x)
print(arr)

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# A boolean index list is a list of booleans corresponding to indexes in the array.
# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
# Example
# Create an array from the elements on index 0 and 2:
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(arr)
print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


# Generate a random integer from 0 to 100:

from numpy import random
x = random.randint(100) #randint for nteger
print(x)

x = random.rand() #Generate a random float from 0 to 1:
print(x)

x=random.randint(100, size=(5))#Generate a 1-D array containing 5 random integers from 0 to 100:
print(x)
x = random.randint(100, size=(3, 5))#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
print(x)

x = random.rand(5)#Generate a 1-D array containing 5 random floats:
print(x)
x = random.rand(3, 5)#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
print(x)

x = random.choice([3, 5, 7, 9])#Return one of the values in an array:
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
print(x)

# A random distribution is a set of random numbers that follow a certain probability density function.
# Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.

# Example
# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0
#The sum of all probability numbers should be 1.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

# Randomly shuffle elements of following array:

from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))#Generate a random permutation of elements of following array:


# Visualize Distributions With Seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
# Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot([0, 1, 2, 3, 4, 5])#Plotting a Displot
# plt.show()

# sns.distplot([0, 1, 2, 3, 4, 5], hist=False) #Plotting a Distplot Without the Histogram
# plt.show()

n1= np.zeros((5,5))
print(n1)

n2= np.full((2,2),10)
print(n2)

n3=np.arange(100,150,5)
print(n3)

n4=np.random.randint(100,200,10)
print(n4)

n5=np.array([[1,2,3],[4,5,6]])
print(n5)
print(n5.shape)
n5.shape=(3,2)
print(n5)
print(n5.shape)

n6=np.array([1,2,3,4,5,6])
n7=np.array([5,6,7,8,9,10])
print(np.intersect1d(n6,n7))
print(np.union1d(n6,n7))
print(np.setdiff1d(n6,n7)) #n6 minus intersect(n6,n7)
print(np.setdiff1d(n7,n6)) #n7 minus intersect(n6,n7)

n1=np.array([1,2])
n2=np.array([5,6])
print(np.sum([n1,n2]))
print(np.sum([n1,n2], axis=0))
print(np.sum([n1,n2], axis=1))
n1=n1+1
print(n1)
n1=n1*2
print(n1)
n1=n1-1
print(n1)
n1=n1/2
print(n1)

#Mean, median,std_dev
n1=np.array([10,20,30,20,10])
print(np.mean(n1))
print(np.median(n1)) # sort & find middle value
# print(np.mode_equivalents(n1))
print(np.std(n1))
np.save('my_numpy',n1) #save & load
print(np.load('my_numpy.npy'))