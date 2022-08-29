with open("python_text_file_working/configuration.txt","r") as file:
    my_list=file.read().splitlines()
    print(my_list)




with open("python_text_file_working/configuration.txt","r") as file:
    my_list=file.readlines()
    print(my_list)

print("#################################")
#To read line by line
with open("python_text_file_working/configuration.txt","r") as file:
    print(file.readline())
    print(file.readline())
print("#################################")
#To read line by line using loop
with open("python_text_file_working/configuration.txt","r") as file:
    for line in file:
        print(line)
        #by default print is having /n to make it go away use end=" " in the print fun