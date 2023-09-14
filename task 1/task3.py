
def arithmeticOperations(num1, num2, operator):
    if(num2 == 0 and operator == '/'): return

    match operator:
        case '+':  print("result: ", num1 + num2)
        case '-':  print("result: ", num1 - num2)
        case '/':  print("result: ", num1 / num2)
        case '*':  print("result: ", num1 * num2)
    

while True:


    print("Виберіть дію")
    print("Додавання - 1")
    print("Віднімання - 2")
    print("Множення - 3")
    print("Ділення - 4")
    print("Перетворити в ціле число - 5")
    print("Перетворити в дійсне число - 6")
    print("Перетворити в логічний тип - 7")
    print("Перетворити на рівність числа - 8")
    print("Число більше за число - 9")
    print("Число менше за число - 10")
    print("Вийти - 0 \n\n")

    action = int(input())
    
    match action:

        case 1: 
            num1 = float(input("Введіть число: "))
            num2 = float(input("Введіть число: "))
            print('-------------------------------\n\n')
            arithmeticOperations(num1, num2, '+')
        case 2: 
            num1 = float(input("Введіть число: "))
            num2 = float(input("Введіть число: "))
            print('-------------------------------\n\n')
            arithmeticOperations(num1, num2, '-')
        case 3: 
            num1 = float(input("Введіть число: "))
            num2 = float(input("Введіть число: "))
            print('-------------------------------\n\n')
            arithmeticOperations(num1, num2, '*')
        case 4: 
            num1 = float(input("Введіть число: "))
            num2 = float(input("Введіть число: "))
            print('-------------------------------\n\n')
            arithmeticOperations(num1, num2, '/')
        case 5: 
            print('-------------------------------\n\n')
            num1 = float(input("Введіть число: "))
            print("result ", int(num1))
        case 6: 
            num1 = float(input("Введіть число: "))
            print('-------------------------------\n\n')
            print("result ", float(num1))
        case 7: 
            num1 = int(input("Введіть число: "))
            print('-------------------------------\n\n')
            print("result ", bool(num1))
        case 8: 
            num1 = float(input("Введіть число: "))
            num2 = float(input("Введіть число: "))
            print('-------------------------------\n\n')
            print("Числа рівні \n") if(num1 == num2) else print("Числа не рівні")
        case 0:
            exit(0)
        case _:
            print("Некоректна дія\n\n")


