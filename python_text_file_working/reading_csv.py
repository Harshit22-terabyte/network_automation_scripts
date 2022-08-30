import csv
with open ("python_text_file_working/airtravel.csv") as f:
    reader=csv.reader(f)
    print(reader)
    next(reader) # this removes the heading points cursor
    #To calculate busiest month in 1958
    year_1958=dict()
    for row in reader:
        year_1958[row[0]]= row[1]

    print(year_1958)

    max_1958=max(year_1958.values())

    #for getting month in 1958 which was busiest
    for k,v in year_1958.items():
        if max_1958 == v:
            print(f"Busiest month in 1958:{k}, Flights:{v.strip()}")

    #v stores variable in string format and strip is string method
    #without strip some whitespaces will come due to csv structure