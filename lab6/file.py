
from datetime import datetime
import csv


def initialize_file():
    with open('info.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Дата', '\t\t\tНазва функції', 'Аргументи', 'Результат'])
        file.close()

def write_in_file(item):
    with open('info.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(item)
        file.close()

def read_from_file():
    with open('info.csv', mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for line in csv_reader:
            print('\t\t'.join(line))
        file.close()

logs_list = []
def get_logs(list):
    for item in list:
        yield item

def logger(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        tuple = (datetime.now(), func.__name__, args, return_value)
        logs_list.append(tuple)
        write_in_file(tuple)
        return return_value
    return wrapper

@logger
def multiply(a,b):
    return a*b

initialize_file()
multiply(15,44)
multiply(10,12)
read_from_file()

log = get_logs(logs_list) 
print(next(log))
print(next(log))



