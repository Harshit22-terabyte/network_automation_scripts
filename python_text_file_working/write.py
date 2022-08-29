with open ("python_text_file_working/myfile.txt","w") as file:
    file.write("Just a line\n")
    file.write("Adding 2nd line")

#in w mode the file will be overriden if already present use a to append
#we have to manually add \n to add space in the string 

#use r+ access mode for reading and writing
#while using r+ mode whatevr we write is written in the starting of file
#to use seperate place use seek function to put cursor there then write
#using r+ mode files should already be present
# https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/#difference-between-r-r-w-w-a-and-a