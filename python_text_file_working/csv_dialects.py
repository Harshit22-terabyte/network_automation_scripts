import csv
csv.register_dialect('hashes',delimiter='#',quoting=csv.QUOTE_NONE,lineterminator='\n')
with open ("python_text_file_working/items.csv",'r') as f:
    reader=csv.reader(f,dialect='hashes')
    for row in reader:
        print(row)

with open ("python_text_file_working/items.csv",'a') as f:
    writer=csv.writer(f,dialect='hashes')
    writer.writerow(('spoon',3,1.5))