import csv
with open ("python_text_file_working/people.csv", "a") as f:
    writer=csv.writer(f)
    csvdata=(5,"Anne","Amsterdam")
    writer.writerow(csvdata)

#we can check content of csv file csv data has ben appended in it

#Now we will create csv file with first row having num second row having square 
# and third row having cube of the num respectively
with open("python_text_file_working/numbers.csv","w", newline="")as f:
    writer -csv.writer(f)
    writer.writerrow([x,x**2,x**3,x**4])
    for x in range(1,101):
        writer.writerow([x,x**2,x**3,x**4])

#by default newline arg is \n 