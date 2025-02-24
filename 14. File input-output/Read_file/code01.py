f=open("Read_file/code02.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()


p=open("Read_file/code02.txt","r")
line1=p.readline()
print(line1)
line2=p.readline()
print(line2)
p.close()