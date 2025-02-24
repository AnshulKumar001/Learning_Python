#average
def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg) 
    return avg
cal_avg(2,40,7)


cites=["pune","delhi","mumbai","chennai","kanpur"]
def cal_list(list):
    print(len(list))
    return
cal_list(cites)

def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cites)
print()  #print for % 
