#John Maghanga
#+ operators
#Assignment 1 
#Python Operators.

#Arithmetic Operators...
#Comparison Operators
#Logical Operators
#Identity Operators
#Membership Operators
#Assignment Operators
#Bitwise Operators

print("Operators")
print("Arrithmetic Operators")

#the + Operators Addition
print("The Addition Operator")
x = 10
y = 20

print(x + y)


# the * Operator
print("The * Operator")
x = 10  #initializing x
y = 20  #initializing y
#printing value
print(x * y)

#the // operators
print("The // Operator")
x = 20
y = 4

print(x // y)


#the % Operator
print("The modulus Operator")
u = 10
c = 23

print(c % u)

#the ** (Exponential) operator
print("The ** (Exponential) Operator")
b = 1
d = 3

print ( d ** b)



print("Comparison Operators")
print("The == operator")

l = 0
i = 10

print(x==y)

print("The != Operator")

q = 12
w = 3

print(q != w)

print("The > Operator")

q = 9
s = 4

if q > s:
    print("q is greater than s")

else:
    print("s is greater than q")

print("the < operator")

q = 11
s = 15

if q < s:
    print("q is smaller than s")

else:
    print("q is greater than s")

print("The >= operator")

u = 10
r = 32

if u >= r:
    print("r is smaller than u")

else:
    print("r is greater than u")

print("The <= operator")

q = 10
s = 32

if q <= s:
    print("q is smaller than s")

else:
    print("q is greater than s")

print("The Logical Operators")

print("Logical And")
x = 10 
y = 30

print(x < y and y < x)

print("Logical or")

x = 10 
y = 30

print(x < y or y < x)

print("Logical not")

x = 10 
y = 30

print(not(x < y and x > y))


print("Identity Operators")

print("Is Operator")

x = -5
y = -5

print(x is y)

print("Is not operator")

x = -3
y = -3

print(x is not y)

print("Membership Operator")
print("in operator")
#returns true if a sequence of values is found
x = ["Maghanga", "John"]

print("Maghanga" in x)
print(x)

print("Not in operator")
#returns true if a sequence of values is found
x = ["Maghanga", "John"]

print("Maghanga" not in x)
print(x)

print("BITWISE OPERATORS")

exit()