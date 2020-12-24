import csv
from pessoa_connection import insere_pessoa, retorna_pessoas

def read_file():
    with open('files/curso-mvcad.csv', "r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=',')
    
        #list_people = [item for item in reader]
        #print(list_people[0])

        for pessoa in reader:
            cpf = pessoa['cpf'].replace('.', '')
            pessoa['cpf'] = cpf.replace('-', '')
            insere_pessoa(pessoa)


read_file()