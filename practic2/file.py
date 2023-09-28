
import random
import uuid
import time

def delay_print(s, sum = 0):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.05)
    if(sum): 
        print(sum, '$')

class Animal():
   
   _weight = 0
   _age_month = 0
   _quality = 100
   
   def __init__(self, num, weight,age):
       self._number = num
       self._weight = weight
       self._age_month = age

   def eat(self):
       if(self._quality<=95):
            self._quality+=5         


   def sleep(self):
       if(self._quality<=70):
           self._quality+= 30
       else:
           self._quality=100

   def animal_info(self, type):
       return f" номер - {self._number} тип - {type}, вік - {self._age_month}, вага - {self._weight}, якість -  {self._quality}"
   
class Cow(Animal):
    type = "корова"

    def __init__(self, num, weight, age):
        super().__init__(num, weight, age)

    def produce_milk(self):
        if(self._quality<=0): return 0
        self._quality-=10
        return random.randint(round(self._quality/100),round(self._quality / 4 ))
    
    def __str__(self):
        return super().animal_info(self.type)

class Chicken(Animal):
    type = "курка"
    def __init__(self, num, weight, age):
        super().__init__(num, weight, age)

    def produce_egg(self):
        if(self._quality > 0):
            self._quality-=5
            return random.randint(0,1)
    
    def __str__(self):
        return super().animal_info(self.type) 
    
class Pig(Animal):

    type = "свиня"

    def __init__(self, num, weight, age):
        super().__init__(num, weight, age)

    def prepare_land(self):
        if(self._quality > 0):
            self._quality-=30
            self._weight+=1
        
    def __str__(self):
        return super().animal_info(self.type)
    
class Farm():
    __animal_prices = {"корова":600, "курка": 45, "свиня": 450,}
    __product_prices = {"яйце":0.5, "молоко/літр": 1, "свинина/кг": 3, "курка/кг": 1.5, "телятина/кг": 3.25}
    __cows = []
    __pigs = []
    __chikens =  []
    __milk = 0
    __eggs = 0
    __chiken_meat = 0
    __cow_meat = 0
    __pig_meat = 0


    __balance = 5000


    def __init__(self):
        work = True
        print("Вітаю, ви знаходитеся на фермі, на вашому рахунку ", self.__balance, "$. Ви можете придбати тварин, і отримувати з них продукти або м'ясо і продавати їх")

        while work:
            print('-----------------------------------------------------------')
            self.__show_menu()
            print('-----------------------------------------------------------')
            self.__take_menu_option()


    # Показати баланс ферим  
    def show_balance(self):
        delay_print("На вашому рахнку знаходиться ", self.__balance)
    # Придбати тварину  
    def buy_animal(self):
        delay_print("Яку тварину ви хочете придбати\n")
        delay_print("1. корову\n2. курку\n3. свиню\n4. вийти\n")
        animal_type = int(input())
        match(animal_type):
            case 1:
                print("Введіть кількість тварин, яку ви хочете придбати")
                count = int(input())
                if(self.__decrease_balance("корова", count)):
                    for i in range(count):
                        self.__cows.append(Cow(round(time.time() + (random.randint(1, 1000) / 2 + random.randint(0,1000))), 150, 18))
                    
            case 2:
                print("Введіть кількість тварин, яку ви хочете придбати")
                count = int(input())
                if(self.__decrease_balance("курка", count)):
                    for i in range(count):
                        self.__chikens.append(Chicken(round(time.time() + (random.randint(1, 1000) / 2 + random.randint(0,1000))), 3, 6))

            case 3: 
                print("Введіть кількість тварин, яку ви хочете придбати")
                count = int(input())
                if(self.__decrease_balance("свиня", count)):
                    for i in range(count):
                        self.__pigs.append(Pig(round(time.time() + (random.randint(1, 1000) / 2 + random.randint(0,1000))), 25, 3))

            case 4: return
            case _: 
                print("Неправильно обрана дія")
                return
    # Показати інформацію по тваринах 
    def show_animals_info(self):
        delay_print("Оберіть тварин, про яких ви хочете перглянути інформацію")
        delay_print("1. корову\n2. курку\n3. свиню\n4. вийти\n")
        animal_type = int(input())
        match animal_type:
            case 1: 
                if(len(self.__cows) == 0):
                    return print("У вас немає корів")
                for animal in self.__cows:
                    print(animal)
            case 2: 
                if(len(self.__chikens) == 0):
                    return print("У вас немає курей")
                for animal in self.__chikens:
                    print(animal)
            case 3: 
                if(len(self.__pigs) == 0):
                    return print("У вас немає свиней")
                for animal in self.__pigs:
                    print(animal)
            case 4: return
            case _:
                return print("Неправильно обрана дія")
                
    # Знайти тварину по унікальному номеру 
    def find_animal(self):
        is_in_list = False
        combined_list = self.__cows + self.__chikens + self.__pigs
        delay_print('Введіть номер тварини яку ви хочете знайти')
        animal_num = int(input())
        for animal in combined_list:
            if(animal._number == animal_num):
                is_in_list = True
                print(animal)
        if(not is_in_list): delay_print("Жодної тварини не знайдено")
    # Продати тварин  
    def sell_animal(self):


        delay_print("Оберіть що ви хочете зробити")
        delay_print("1. продати всі корови\n2. продати всі кури\n3. продати всі свині\n")
        animal_type = int(input())
        match animal_type:
            case 1: 
                if(len(self.__cows == 0)): return print("У вас немає корів")
                self.__balance+= len(self.__cows) * self.__animal_prices["корова"]
                self.__cows.clear()
                delay_print("Всі корови продані, ваш баланс - ", self.__balance)
            case 2:
                if(len(self.__chikens == 0)): return print("У вас немає курей")
                self.__balance+= len(self.__chikens) * self.__animal_prices["курка"]
                self.__chikens.clear()
                delay_print("Всі кури продані, ваш баланс - ", self.__balance)

            case 3:
                if(len(self.__pigs == 0)): return print("У вас немає свиней")
                for pig in self.__pigs:
                    self.__balance+= pig._weight * self.__product_prices["свинина/кг"]
                self.__pigs.clear()
                delay_print("Всі свині продані, ваш баланс - ", self.__balance)    

            case _: 
                 return delay_print("Некорктний вибір")
                
    # Перевірити іноформацію про склад 
    def check_warehouse(self):
        print("Молоко - ", self.__milk, ' літрів')
        print("Яйця - ", self.__eggs, ' шт.')
        print("Куряче м'ясо - ", self.__chiken_meat, ' кг.')
        print("Свиняче м'ясо - ", self.__pig_meat, 'кг' )
        print("Телятина - ", self.__cow_meat, ' кг')
    
    # Подивитися статистику кількості тварин  
    def check_animal_count(self): 
        print("Кількість корів - ", len(self.__cows))
        print("Кількість курей - ", len(self.__chikens))
        print("Кількість свиней - ", len(self.__pigs))
    #=========================================
    # Отримати мясо тварини
    def get_animal_meat(self):
        combined_animal_list = self.__cows + self.__chikens + self.__pigs
        delay_print("Введіть номер тварини")
        animal_num = int(input())
        for animal in combined_animal_list:
            if(animal._number == animal_num):
                match animal.type:
                    case "корова":
                        self.__cow_meat+= animal._weight - (round(animal._weight * 0.1))
                        self.__cows.remove(animal)
                    case "курка":
                        self.__chiken_meat+= animal._weight - (round(animal._weight * 0.05))
                        self.__chikens.remove(animal)
                    case "свинина":
                        self.__pig_meat+= animal._weight - (round(animal._weight * 0.1))
                        self.__pigs.remove(animal)

    # Виробити нових курей з яєць
    def reproduce_chikens(self):
        delay_print("Ввдеіть кількість курей яку ви хочете виростити")
        chiken_num = int(input())
        if(self.__eggs >= chiken_num):
            for i in range(chiken_num):
                self.__eggs-=1
                self.__chikens.append(Chicken(round(time.time() + (random.randint(1, 1000) / 2 + random.randint(0,1000))), 3, 6))
            print("Ви вивели ", chiken_num, ' курей')
        else:
            delay_print("У вас немає на складі яєць")
    # Продати товари
    def sell_the_commodity(self):
        delay_print(" Oберіть, що продати ")
        print("1. Молоко - ", self.__milk, ' літрів')
        print("2. Яйця - ", self.__eggs, ' шт.')
        print("3. Куряче м'ясо - ", self.__chiken_meat, ' кг.')
        print("4. Свиняче м'ясо - ", self.__pig_meat, 'кг' )
        print("5. Телятина - ", self.__cow_meat, ' кг')
        commodity_num = int(input())
        match commodity_num:
            case 1: 
                selling_sum = self.__milk * self.__product_prices["молоко/літр"]
                self.__balance+= selling_sum
                print("Ви продали ", self.__milk, ' молока і заробили - ', selling_sum, '$')
                self.__milk = 0

            case 2: 
                selling_sum = self.__eggs * self.__product_prices["яйце"]
                self.__balance+= selling_sum
                print("Ви продали ", self.__eggs, ' яєць і заробили - ', selling_sum, '$')
                self.__eggs = 0
            case 3: 
                selling_sum = self.__chiken_meat * self.__product_prices["курка/кг"]
                self.__balance+= selling_sum
                print("Ви продали ", self.__chiken_meat, " кг. курячого м'яса і заробили - ", selling_sum, '$')
                self.__chiken_meat = 0
            case 4: 
                selling_sum = self.__pig_meat * self.__product_prices["свинина/кг"]
                self.__balance+= selling_sum
                print("Ви продали ", self.__pig_meat, ' кг свинини і заробили - ', selling_sum, '$')
                self.__pig_meat = 0
            case 5: 
                selling_sum = self.__cow_meat * self.__product_prices["телятина/кг"]
                self.__balance+= selling_sum
                print("Ви продали ", self.__cow_meat, ' кг телятини і заробили - ', selling_sum, '$')
                self.__cow_meat = 0
            case _:
                print("Некоректна дія")
                return

    # Зібрати яйця
    def gather_eggs(self):
        if(len(self.__chikens) == 0): return print("У вас немає курей")
        total_eggs = 0
        for chiken in self.__chikens:
            total_eggs += chiken.produce_egg()
        self.__eggs+= total_eggs
        print("Ви зібрали - ", total_eggs, ' яєць')

    # Зібрати молоко
    def gather_milk(self):
        if(len(self.__cows)==0): return print("У вас немає корів")
        total_milk = 0
        for cow in self.__cows:
            total_milk += cow.produce_milk()
        self.__milk+= total_milk
        print("Ви зібрали - ", total_milk, ' молока')

    # Погодувати тварин
    def feed_animals(self):
        delay_print("Оберіть тварин яких ви хочете погодувати ")
        delay_print("1. корову\n2. курку\n3. свиню\n4. вийти\n")
        animal_type = int(input())

        match animal_type:
            case 1:
                if(len(self.__cows) ==0): return print("У вас немає корів")
                for cow in self.__cows:
                    cow.eat()
                delay_print("Корови погодовані")
            case 2:
                if(len(self.__chikens) ==0): return print("У вас немає курей")
                for chiken in self.__chikens:
                    chiken.eat()
                delay_print("Кури погодовані")
            case 3: 
                if(len(self.__pigs) == 0): return print("У вас немає свиней")
                for pig in self.__pigs:
                    pig.eat()
                delay_print("Свниі погодовані")
            case 4: return
            case _: return delay_print("Ви обрали некоректу дію")

    # Підготувати землю до посіву
    def prepare_land(self):
        if(len(self.__pigs)==0): return print("У вас немає свиней")
        for pig in self.__pigs:
            pig.prepare_land()
        delay_print("Земля до посіву підготовлена")

    # Функція зменшення балансу при купівлі тварини
    def __decrease_balance(self, animal_type, count):
        if(self.__balance >= self.__animal_prices[animal_type] * count):
            self.__balance-= self.__animal_prices[animal_type] * count
            print("Ви придбали ", count, ' тварин')
            return 1
        else: return 0
    # Меню
    def __show_menu(self):
        print("Оберіть дію: ")
        print("1. Показати баланс ")
        print("2. Показати інформацію про тварин ")
        print("3. Придбати тварину ")
        print("4. Продати тварину ")
        print("5. Перевірити інформація про склад ")
        print("6. Переглянути статистику кількості тварин ")
        print("7. Знайти тварину по номеру ")
        print("8. Продати продукти ")
        print("9. Виростити курей власноруч ")
        print("10. Отримати м'ясо з тварини")
        print("11. Зібрати яйця")
        print("12. Зібрати молоко")
        print("13. Погодувати тварин")
        print("14. Підготувати землю до посіву")
        print("0. Вийти")
    # Меню дії
    def __take_menu_option(self):
        option_num = int(input())
        match option_num:
            case 1: self.show_balance()
            case 2: self.show_animals_info()
            case 3: self.buy_animal()
            case 4: self.sell_animal()
            case 5: self.check_warehouse()
            case 6: self.check_animal_count()
            case 7: self.find_animal()
            case 8: self.sell_the_commodity()
            case 9: self.reproduce_chikens()
            case 10: self.get_animal_meat()
            case 11: self.gather_eggs()
            case 12: self.gather_milk()
            case 13: self.feed_animals()
            case 14: self.prepare_land()
            case 0: exit(0)
            case _: delay_print("Ви обрали некоретну дію, будь ласка спробуйте ще раз")


farm = Farm()



