tup1=(2,4,73,2,5,76,6)
tup2=("shika","anu","manshi","radha")
tup3=(2.3,3.1,7.5,2.4,5.9)
tup4=(1, "hello", 3.14)

print(type(tup1),tup1)
print(type(tup2),tup2)
print(type(tup3),tup3)
print(type(tup4),tup4)

#operation of tuple

#Positive Indexing:
print(tup1[1])
print(tup1[0])

#Negative Indexing:
print(tup1[-1])
print(tup1[-2])


#slicing
print(tup1[1:5])
print(tup1[1:7:3])

#add
tup3=(2.3,3.1,7.5,2.4,5.9)
tup1=(2,4,73,2,5,76,6)
top=tup3+tup1
print(top)

#count():
t = (1, 2, 3, 2, 4)  # 2 kitne baar hai
print(t.count(2)) 

#index()
print(t.index(3)) # 3 kha pr hai