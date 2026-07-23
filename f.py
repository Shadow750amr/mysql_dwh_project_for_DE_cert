
import csv

with open('airflow/dags/capstone/accesslog.txt', "r", encoding="utf-8") as file:
    with open('extracted_data.txt','w') as final:
        reader = csv.reader(file, delimiter="-")
        for row in reader:
            lista = row.pop(0)
            final.write(lista)


