dict1={
    "key":"value",
    "name":"Anshul kumar",
    "cgpa":6.6,
    "height":5.10,
    "subject":["python","math","html"],
    "number":(90,80,85)
}
print(type(dict1))
print(dict1)


#Accessing Values
print(dict1["cgpa"])
print(dict1["subject"])
print(dict1["number"])


#Modifying Dictionaries
dict1["cgpa"]=8.0
dict1["height"]=5.9
print(dict1)

#1. operations
#(a). keys operation
print(dict1.keys())

#(b). values operation
print(dict1.values())

#(c). items operation
print(dict1.items())

dict0=list(dict1.items())
print(dict0[1])

#(d). get() method
print(dict1.get("subject"))   #return none
print(dict1["subject"])       #return error
 
#(e). add a new dict
new_dict={"city":"muzaffernagar"}
dict1.update(new_dict)
print(dict1)



