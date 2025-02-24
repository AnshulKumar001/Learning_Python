#Recursive function

def rec(n):
    if(n==0):
        return
    print(n)
    rec(n-1)
rec(5)    

 
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(1))
print(fact(0))
print(fact(2))
print(fact(5))


