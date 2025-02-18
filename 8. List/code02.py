list1=["pen",2.5,5,"cake"]

#1.Changing an Element:
list1[0]="book" 
print(list1)

#2. slicing
print(list1[1:3])
print(list1[1:4:2])

#3. append()
list1.append(4)
print(list1)

#4. sort()
list2=[25,3,41,5,22,2]
list3=["s","u","e","a","s"]
list2.sort()
print(list2)

list3.sort()
print(list3)

#6.reverse()
list2.reverse()
print(list2)

#5.insert(idx,ele)
list2.insert(1,1000)
print(list2)

#6.sum()
print(sum(list2))

#7.pop(idx)
list2.pop(1)
print(list2)

#8.remove()
list2.remove(25)
print(list2)



