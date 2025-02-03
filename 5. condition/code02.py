#voter card

n=int(input("Enter your age:"))

if(n>=18):
    print("you are above the age of consent")
elif(n<0):
    print("you are entering an invalid")   
else:
    print("you are below the age of consent")    