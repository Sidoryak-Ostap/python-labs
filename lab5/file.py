import csv

car_list = [
['Марка', 'Модель', 'Рік', 'Колір'],
['BMW', 'i8', 2020, 'чорний'],
['Ford', 'E-Class', 2019, 'сірий'],
['Toyota', 'Camry', 2018, 'синій'],
['Audi', 'A6', 2021, 'червоний'],
['Audi', 'A8', 2015, 'чорний'],
['Tesla', 'Model S', 2019, 'білий'],
['Audi', 'Camry', 2025, 'синій'],
]





class DataBaseActions():
    _file_path = None
    _file_instance = None
    def __init__(self, file_path):
        self._file_path = file_path
        # self.inititialize_file()

    def open_file(self,path,  mode='r'):
        file = open(path, mode, encoding='utf-8', newline='')
        return file

# Ініцілізувати файл з даними
    def inititialize_file(self):
        self.get_file_instance('w')
        
        writer = csv.writer(self._file_instance, delimiter=',' )
        writer.writerows(car_list)
            
    def get_file_instance(self, mode):
        if(self._file_instance != None): self._file_instance.close()
        self._file_instance = self.open_file(self._file_path, mode)
    
# Читання файлу
    def read_info(self):
        self.get_file_instance('r')
        csv_reader = csv.reader(self._file_instance, delimiter=',')
        for id, line in enumerate(csv_reader):
            if(id == 0): print('\t'.join(line))
            else: print(f'{id}','\t'.join(line))
        
# Запис інформації в файл
    def write_file(self, info=None):
        self.get_file_instance('a')
        writer = csv.writer(self._file_instance, delimiter=',')
        
        if(info !=None and type(info) is type(list())):
            writer.writerow(info)
        else:
            print("Введіть марку, модель, рік та колір автомобіля")
            list = []
            for i in range(4):
                list.append(input())
            writer.writerow(list)
# Пошук за фільтром
    def search_info(self):
        self.get_file_instance('r')
        
        list = self.read_data()
        
            
        search_by = int(input("Виберіть фільтр для пошуку інормації\n1. Марка\n2. Модель\n3. Рік випуску\n4. Колір\n"))
        search_value = input("Введіть значеня: ")
        
        for list_item in list:
            if(list_item[search_by - 1].lower() == search_value.lower()):
                print('\t'.join(list_item))
# Видалення інформації        
    def delete_info(self):
        self.read_info()
        self.get_file_instance('r')
        car_number = int(input('Введіть номер запису який ви хочете видалити:  '))
        
        data = self.read_data()
        
        
        del data[car_number]
        
        self.insert_new_data(data)    
# Оновлення записів
    def update_record(self):
        self.read_info()
        self.get_file_instance('r')
        car_number = int(input('Введіть номер запису який ви хочете редагувати:  '))
        update_by = int(input("Виберіть що ви хочете поміняти\n1. Марка\n2. Модель\n3. Рік випуску\n4. Колір\n"))
        update_value = input("Введіть значення: ")
        
        data = self.read_data()
        
        data[car_number][update_by - 1] = update_value
        self.insert_new_data(data)

# Сортування інформації
    def sort_info(self):
        self.get_file_instance('r')
        data = self.read_data()
        
        del data[0]
        sort_by = int(input("Виберіть фільтр для сортування інормації\n1. Марка\n2. Модель\n3. Рік випуску\n4. Колір\n"))
        
        sorted_info = sorted(data, key=lambda x:x[sort_by - 1])
        for id, line in enumerate(sorted_info):
            print(f'{id+1}','\t'.join(line))
        


# Вставити оновлену/видалену інформацію в файл 
    def insert_new_data(self, data):
        self.get_file_instance('w')
        csv_writer = csv.writer(self._file_instance)
        csv_writer.writerows(data)
    
    def read_data(self):
        data = []
        csv_reader= csv.reader(self._file_instance)
        for item in csv_reader:
            data.append(item)
        return data
            
# Виведення середнього року випуску кожної марки
    def average_year_of_car_mark(self):
        self.get_file_instance('r')
        data = []
        csv.reader = csv.reader(self._file_instance, delimiter=',')
        for line in csv.reader:
            data.append(line)

        list_of_dict = []

        for id, line in enumerate(data):
            chnaged = False
            if(id == 0): continue
            for dict in list_of_dict: 
                if(line[0] in dict):
                    dict[line[0]] = int(dict[line[0]]) + int(line[2])
                    dict['c'] +=1
                    chnaged = True
                    
            if(not chnaged): list_of_dict.append({line[0]: line[2], 'c': 1})


        new_list = []
        for i in list_of_dict:
            my_dict = list(i.items())
            new_list.append(my_dict)

        print(new_list)        
        print("Марка\t  Рік")
        for i in new_list:
            print(i[0][0],"\t", round((int(i[0][1]) / i[1][1])))



class Singleton(DataBaseActions):
    _instance = None

    def __new__(cls, path):
        print(path)
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    
    
    
        
        

            
        
    
    
database= Singleton('test.csv')
print(database)