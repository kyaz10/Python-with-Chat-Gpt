def calculator():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Введите номер операции (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print("Результат:", num1 + num2)
        elif choice == '2':
            print("Результат:", num1 - num2)
        elif choice == '3':
            print("Результат:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Результат:", num1 / num2)
            else:
                print("Ошибка: Деление на ноль!")
    else:
        print("Неверный выбор")

calculator()
