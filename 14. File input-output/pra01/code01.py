with open("pra01/code02.txt","r") as f:
    data=f.read()
    new_data = data.replace("java","python")
    print(new_data)
with open("pra01/code02.txt","w") as f:
    data=f.write(new_data)