# while Loop 


#loops  are used to repeat instructions 
#1. while  loop
#count=0
#while count <=5:
 #   print("hello ",count)
  #  count +=1


#2. 
#i=5
#while i>=1:
 #   print("Anshul kumar",i)
  #  i-=1
#print("loop end")


#table
#n=int(input("Enter a number: "))
#i=1
#while i<=10:
#  print(f"{n}X{i}=",n*i)
 # i+=1

#num=[1,4,9,16,25,32,34,65,45,100]
#i=0
#while i<len(num):
 #print(num[i])
 #i+=1

#indexing
num=(1,4,9,5,25,32,5,65,45,100)
x=5
i=0
while i<len(num):
 if(num[i]==x):
   print("find",i)
 i+=1

    
#1. break statement
i = 1
while i <= 10:
    if i == 7:
        print("Loop breaks at", i)
        break  # Exit the loop when i is 7
    print(i)
    i += 1


#2. continue statement
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping", i)
        continue  # Skip the rest of the code for this iteration
    print("Value:", i)

