a = 33
b = 200

if b > a:
  print("b is greater than a")


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33

if a > b: print("a is greater than b")


a = 2
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

b = 330

print("A") if a > b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement
