name ="Ankan"

print(f"Hello Bhaijaan {name}")
x = "awesome"
print("Python is " + x)

import math
x=math.factorial(5) #c:/damdlamlm
print(x)

#type of object
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#casting objects

x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)


x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

# Get characters at nth position
a = "Hello, World!"
print(a[0],a[1],a[2],a[-1])
print(a[0]+a[1]+a[2])
print(a[0:2],a[0:-1])

#trim leading/trailing white spaces
a = " Hello, World!  A"
print(a.strip())
print(len(a))
print(a.lower())

print(a.replace("l", "J"))

print(a.split(","))

x = 5
y = 3
print(x + y)

x = 12
y = 3

print(x / y)

x = 5
y = 3

print(x * y)

x = 15
y = 4
z= x % y
print(f"modulus {z}")
w= y % x
print("modulus " + str(w))# as w is int, convert it to str
print(x // y) #floor division 15/4= 3.75, then floor(lower rounding) is 3 , roof(upper rounding) is 4
print(x ** y) #exponent, x to power y








x = ["apple", "banana"]
print("pineapple" not in x)
print("banana" not in x)
print("apple" in x)
# returns True because a sequence with the value "pineapple" is not in the list

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x

print(x is not  y)
print(x is y)

# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10
print(x < 5 or x < 4)
# returns False
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

x = 5
y = 3
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)
print(x >  y)

x = 5
x &= 3 #x= x & 3 =true
print(x)

x = 5
x |= 3 #x= x |3 =x or 3=5 or 3=
print(x)

x = 5
x **= 3 #x=x**3 =125
print(x)

x = 5
x ^= 3
print(x) #x= x ^3 i.e. x XOR 3 = (x|3)-(x&3)= (5|3)- (5&3)= 7 -1=6

# 3= 011
# 5= 101

x = 5
x >>= 3
print(x) # left shift operator, least significant number

x = 5
x <<= 3
print(x)#x >>= 1 means "set x to itself shifted by one bit to the right". The expression evaluates to the new value of x after the shift.

# Note: The value of the most significant bit after the shift is zero for values of unsigned type. For values of signed type the most significant bit is copied from the sign bit of the value prior to shifting 
# as part of sign extension, so the loop will never finish if x is a signed type, and the initial value is negative.











