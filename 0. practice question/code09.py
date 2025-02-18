#palindrome/not palindrome

list1=[1,2,3,2,1]
list_copy=list1.copy()
list_copy.reverse()

if(list_copy==list1):
    print("palindrome")
else:
    print("not palindrome")    