
import time

def delayPrint(s):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.05)
    print('')

quest_index= 0

def gameLogic(chosen_answer, quest_index):

    match chosen_answer:
        #the point of choosing scenario 1 (3 ends)
        case 1: #1
            delayPrint("Гном: 'У мами Івана було три сини. Першого звали Петро, другого – Василь. Як звали третього сина?'")
            print("Варіанти відповідей:\n1) 'Іван'\n2) 'Петро'\n3) 'Василь'")
            answer = int(input("Введіть відповідь: "))
            match answer:
                case 1: 
                    chosen_answer = quest_index + 3
                    quest_index+=1
                case 2|3:
                    chosen_answer = quest_index + 4
                    quest_index+=1
                case _:
                    delayPrint("Що ти там бурмочеш, якшо не відгадаєш то я тебе вб'ю")

        # scenario 1.1
        case 4: #3
            delayPrint("Гном: Вітаю ти відагадав, тепер ти можеш пройти далі")
            delayPrint("Вітаю на другому рівні")
            delayPrint("На твоєму шляху попався Троль, який вміє розв'язувати математичні задачі")
            delayPrint("Троль: 'Якщо ти хочеш пройти далі то тобі потрібно розв'язати цей приклад: 115+85 / 4'\nВаріанти відповідей:\n1. 110\n2. 50\n3. 45")
            answer = int(input("Введіть відповідь: "))
            match answer:
                case 1|3: 
                    chosen_answer = quest_index + 8
                    quest_index+=1
                case 2: 
                    chosen_answer = quest_index + 7
                    quest_index+=1
                case _:
                    delayPrint("Що ти там бурмочеш, якшо не відгадаєш то я тебе вб'ю")
        case 9: #7
            delayPrint("Ти відагадав, молодець можеш йти далі")
            delayPrint("Вітаю ви пройшли через троля, це неабияке досягенення, тепер ти можеш йти далі")
            chosen_answer = quest_index + 13
        case 10: #8
            delayPrint("Троль: ти не вгадав, правила є правила тобі кінець")
            delayPrint("Троль розмахується щосили і вдарає мимо вас, і падає")
            delayPrint("У вас є час щоб втекти, або продовжити бій\nВиберіть варіант:\n 1. Втекти\n2. Продовжити бій")
            answer = int(input("Виберіть відповідь: "))
            match answer:
                case 1: 
                    print("Поки троль лежав вам вдалося заховатися в кущі а згодом втекти")
                    chosen_answer = quest_index + 13
                case _:
                    print("Що ти там бурмочеш, якшо не відгадаєш то я тебе вб'ю")
        case 16: #13 
            delayPrint("Йшовши по дорозі, ви знайшли скриню, що з нею робити?\n Варінти відподей: \n1. Продати\n2. Відкрити")
            answer = int(input("Виберіть відповідь: "))
            match answer:
                case 1: 
                    delayPrint("Ви продали скриню, не знаючи що там є і отримали 5 золотих монет, час розслабитися і випити пива в місевому кабаку, ти цього заслужив")
                    exit(0)
                case 2:
                    delayPrint("Ви відкрили скриню, а там лежать скарби, ви тепер багаті, і можете купити все що захочете, вітаю це було варте того")
                    delayPrint("The end")
                    exit(0)
                case _:
                    delayPrint("Виберіть один з запропонованих варіантів")
        
        #scenario 1.2
        case 5: #4
            delayPrint("Гном: 'Ти не вгадав, я змушений тебе вбити'\nГном розмахується із всієї сили і вдарає вас по лиці, ви падаєте але знаходите сили, щоб завдати відповідного удару, ви вдараєте гнома і він падає втрачаючи свімодість, ви розумієте що маєте шанс втекти і тікаєте")
            chosen_answer = quest_index + 9
            quest_index+=1
        case 11: #9
            delayPrint("Услизнувши від гнома, ви пішли далі і натрапили на дві дороги. Потрібео вибрати одну з доріг.\nВаріанти відповідей:\n1. Ліва дорога\n2. Права дорога")
            answer = int(input("Виберіть відповідь: "))
            match answer:
                case 1: 
                    chosen_answer = quest_index + 14
                    quest_index+=1
                case 2: 
                    chosen_answer = quest_index + 15
                    quest_index+=1
                case _: print("Оберіть один із варіантів")
        case 17: #14 left road
            delayPrint("Ви обрали ліву дорогу, ця дорога є повна пасток та вбивць, пройшовши кілька сотень метрів ви попали в яму з шипами і померли ")
            print("The end")
            exit(0)
        case 18: #15 right road
            delayPrint("На щастя ви обрали праву дорогу, яка є цілком безпечна, пройшовши кілька сотень метрів ви зустріли доброго чаклуна, який запропонував вам виконати ваше бажання")
            print("Варінти відповідей:\n1. Безсмерття 2. Бути вічно молодим")
            answer = int(input("Виберіть відповідь: "))
            match answer:
                case 1: 
                    delayPrint("Вітаю, тепер ви безсмертний і можете нічого не боятися, ви є непереможний")
                    print("The end")
                    exit(0)
                case 2: 
                    delayPrint("Вітаю, тепер чи вічно молодий, і вічно сильний як зараз, тепер зморшки вам не страшні")
                    print("The end")
                    exit(0)
                case _: print("Оберіть один із варіантів")
                

        #the point of choosing scenario 2    
        case 2: #2
            delayPrint("\nГном: 'Ти зробив неправильний вибінр, тобі кінець'")
            delayPrint("Гном розмахується і починає вас бити, ви відчуваєте сильний біль який пронизує усе тіло.\nВиберіть варінт:\n1. Погодитися на загадку\n2. Спробувати втекти")
            answer = int(input("Виберіть відповідь: "))
            match answer: 
                case 1: 
                    chosen_answer = 1
                    quest_index = 1
                case 2:
                    chosen_answer = quest_index + 6
                    quest_index+=1
                case _: print("Що ти там бурмочеш?")
                

        #scenario 2.1 (2 ends)
        case 7: #6
            delayPrint("Все таки вам вдалося втекти, проте ви є дуже сильно поранений. Виберіть варінт:\n1. Лягти перепочити\n2. Піти далі")
            answer = int(input("Виберіть відповідь: "))
            match answer: 
                case 1: 
                    chosen_answer = quest_index + 11
                    quest_index+= 1
                case 2:
                    chosen_answer = quest_index + 12
                    quest_index+=1
                case _: print("Оберіть один із варіантів")

        case 13: #11  
            delayPrint("Відновивши сили ви рушаєте далі, на дорозі вам трапляється лев")
            delayPrint("Лев: 'Я цар всіх звірів і тього лісу зокрема, для того щоб піти далі відгадай загадку, якщо нне відгадаєш я тебе з'їм ahahahah'")
            delayPrint("Хто з води виходить сухим?\nВарінти відповідей:\n1. Студент\n 2. Гуска\n 3. Ведмідь")
            answer = int(input("Виберіть відповідь: "))
            match answer: 
                case 2: 
                    delayPrint("Лев: 'Ти відгадав загадку, я стрмаю своє слово, моожеш йти але більше не трапляйся мені на очі'")
                    chosen_answer = quest_index + 17
                    quest_index +=1
                case 1|3:
                    delayPrint("Лев: 'Сьогодні не твій день'")
                    delayPrint("Лев накинувся на вас, у вас не було шансів вижити")
                    print("The end")
                    exit(0)
                case _: print("Оберіть один із варіантів")
                
        case 14: #12
            print("\nВідгадавши загадку лева ви пішли далі")
            delayPrint("На вашому шляху ви зустріли дівчину, чию сім'ю викрали, вона просить вас про допомогу.\nВиберіть варіант\n1. Приєднатися до дівчини\n2. Відмовити")
            answer = int(input("Виберіть відповідь: "))
            match answer:
                case 1:
                    delayPrint("Ви вирішили приєднатися до дівчини та допомогти їй, це благородний вчинок. Це означає що на тебе чикають нові пригоди, тож уперед")
                    delayPrint("To be continied...")
                    exit(0)
                case 2:
                    delayPrint("Ви відмовили дівчині та рушили далі")
                    chosen_answer = quest_index + 17
                    quest_index+=1
                case _: print("Оберіть один із варіантів")
                
        case 20: #17

            delayPrint("По дорозі вас наздогнав гном та вбив, ох не слід було його злити з самого початку")
            print("The end")
            exit(0)
        
    return gameLogic(chosen_answer, quest_index)
        


#The entry point of choosing scenario
delayPrint("Вітаю на першому рівні! До тебе підходить невідоме створіння, схоже на гнома, і каже: 'Привіт, незнайомцю. Якщо ти хочеш пройти, то тобі потрібно відгадати загадку. Якщо ти не хочеш, то я тебе вб'ю.\n'Варіанти відповідей:")
print("1. Так я хочу відгадати загадку\n2. Ні, я нехочу відгадувати загадку")
answer = int(input())

#Game start
isCorrect = True
while isCorrect:
    match answer:
        case 1|2:
            chosen_answer = quest_index + answer
            quest_index+=1 
            isCorrect = False
            gameLogic(chosen_answer, quest_index)
        case _: delayPrint("Гном: 'Я не розумію тебе, якщо ти незможеш відповісти тоді я вб'ю тебе'")