# SET= duplicate values ignored
#set is immutable

#empty set==>set{}
#empty dict==>{}

num1={1,2,3,4,5,6,7,3,3,3,3,3,3}
num2={"anshul","abhi","raj","rohan","anshul","anshul","anshul"}
num3={1.2,2,3.5,4.5,5,6.2,7}
num4={"mango",2,3.3,4,"orange",6.9,7}
print(type(num1),num1)
print(len(num1),num1)
empty_set=set()
print(type(empty_set))

#set operation

#1. add operation
num1.add("hello")
print(num1)
#2. remove operation
num2.remove("anshul")
print(num2)
#3. pop operation
num4.pop()
print(num4)  # remove a random values

#4. clear operation
num3.clear()
print(num3)

set1={1,2,3}
set2={3,4,5}
union=set1.union(set2)
inters=set1.intersection(set2)
print(union)
print(inters)




