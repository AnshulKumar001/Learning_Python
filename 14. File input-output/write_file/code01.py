f=open("write_file/code.txt","w")
data=f.write("Hello! my hobbies: sleeping")
print(data)
f.close()

f=open("write_file/code.txt","a")
data=f.write(", coding, online game\nMy life is the best life")
print(data)
f.close()