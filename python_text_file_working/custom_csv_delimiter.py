import csv
with open("python_text_file_working/passwd.csv","r", newline="")as f:
    reader=csv.reader(f,delimiter=":",lineterminator='\n')
    for row in reader:
        print(row)