f=open("python_text_file_working/configuration.txt","r")
content=f.read()
print(content)
print(f.closed)
f.close()
print(f.closed)#returns true if file is closed