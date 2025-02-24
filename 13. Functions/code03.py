#factorial

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
fact(5)    
fact(8)
fact(6)


#currency converter
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")
converter(1)
converter(2)
converter(5)

