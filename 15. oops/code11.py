#multiple inheritance


class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C:
    varC = "welcome to class C"

class D(A, B, C): 
    varD = "welcome to class D"

d1 = D()

# Accessing the class variables
print(d1.varA)  # Accessing varA from class A
print(d1.varB)  # Accessing varB from class B
print(d1.varC)  # Accessing varC from class C
print(d1.varD)  # Accessing varD from class D
