



class CommonError(Exception):
    def __init__(self, text = ''):
        if(text == ''):
            self.value = 'Цього року немає в списку подій'
        else: self.value = text

def display_set(set):
    for i in set:
        print(i, end=' ')

def update_dict():
    for item in events:
        dict[item[1]] = item[0]


def travel():
    print("Вітаю, мандрівнику, зараз ти можеш потрапити у такі роки:")
    display_set(set_of_years)
    year = int(input("\nВведіть рік, який ви хочете відвідати: "))
    if(year not in dict):
        raise CommonError()
    elif(year in visited_evenets): raise CommonError("Ви вже відвідали цю подію")
    print("Ви потрапили в ", year, " рік. Подія - ", dict[year])
    visited_evenets.append(year)

    
def update_info(year):
    update_dict()
    set_of_years.update([year])

def delete_event_info(year):
    set_of_years.remove(year)
    dict.pop(year)
    for i in events:
        if(i[1] == year): events.remove(i)

def add_event():
    year = int(input("Введіть рік події: "))
    if(year in set_of_years): raise CommonError("Подія з даним роком вже існує")
    event_name = input("Введіть опис події: ")
    events.append((event_name, year))
    update_info(year)
    print("Подія додана")

def delete_event():
    year = int(input("Введіть рік події, яку ви хочете видалити: "))
    if(year not in dict): raise CommonError("Вказаний рік не знаходиться в списку")
    delete_event_info(year)
    print("Подія видалена")




#Список подій
events = [
    ("Відкриття олімпійських ігор", 1896),
    ("Створення Всесвітньої організації охорони здоров'я", 1948),
    ("Перший космічний польот Юрія Гагаріна", 1961),
    ("Атака на США 11 вересня", 2001),
    ("Прийняття Паризької угоди про зміну клімату", 2015),
    ("Виявлення перших екзопланет", 1992),
    ("Прийняття загальноєвропейського стандарту GSM", 1982),
    ("Оголошення незалежності України", 1991),
    ("Запуск першого супутника Шанхайської співтовариства", 2020)
]
#Словник часу
dict = {}
update_dict()
#Множина подій
set_of_years = {i[1] for i in events}

#Відвідані роки
visited_evenets = []


try:
    print("Привіт мандрівнику, прямо зараз ти можеш подорожувати або додати нову подію")

    while True:
        action  = int(input("1. Подорожувати\n2. Додати подію\n3. Видалити подію\n"))
        match action:
            case 1: travel()
            case 2: add_event()
            case 3: delete_event()
            case _: print("Неправильно обрана дія")

except CommonError as err:
    print(err.value)
except ValueError as e:
    print(str(e))






