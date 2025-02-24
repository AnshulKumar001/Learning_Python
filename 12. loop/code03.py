#range()

#for num in range(5):  #range(stop)
   # print(num)

#for num2 in range(7,10): #range(start ,stop)
 #   print(num2)

#for num3 in range(100,1000,100):  #range(start, stop, step)
 #   print(num3)  

#negative or decrease number
#for neg in range (50, 1, -1) :
#    print(neg)  

#i=int(input("Table no. "))
#for table in range (1,11):
 #   print(i*table)   

# pass statement is use to hold of code

#for pas in range(10):  # error a jata agar pass ka use nahi krte to q ki code ko half hi likha hai
 #   pass

#for pas in range(15):
 #   print(pas)
 

 #sum all number
n=int(input("enter a number: "))
sum=0
for i in range (1, n+1):
         sum+=i
print("sum",sum)  


#factorial

p=int(input("Enter a number: "))

fac=1
for i in range (1, p+1):
   fac*=i
   i+=1
   
print("factorial",fac)   