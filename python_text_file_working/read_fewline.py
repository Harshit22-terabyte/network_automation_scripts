f=open("python_text_file_working/configuration.txt","r")
content=f.read() 
print(content)
print("#######################################")
#give the number of char you want to read in form of integer
content=f.read(11)#read 11 characters
print(content)
print("***************************************")
#Now if we use read again it will print characters after 30 not from starting
content=f.read(4) #Read next 4 characters
print(content)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(f.tell()) # this will tell position of cursor
print(f.seek(2)) # this moves the position of cursor to 2 tehn we can read further
print(f.closed)
f.close()
print(f.closed)#returns true if file is closed