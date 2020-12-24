import csv

def read_file():
    with open('files/curso-mvcad.csv', "r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=',')
    
        list_people = [item for item in reader]
        print(list_people[0])

read_file()