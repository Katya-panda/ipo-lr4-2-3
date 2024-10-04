# задаём список числами
numbers = [1, 2, 3, 4, 5]
# проверяем, не пустой ли список
if len(numbers) == 0: # выводим сообщение, если список пуст
    print("Список пуст")
else:
    # инициализируем переменную max_number первым элементом списка
    max_number = numbers[0]
    # инициализируем счётчик i, который будет использоваться для перебора списка
    i = 1
    # запускаем цикл while, который будет выполняться, пока i меньше длины списка
    while i < len(numbers): # сравниваем текущий элемент списка с max_number
        if numbers[i] > max_number: # если текущий элемент больше, обновляем max_number
            max_number = numbers[i]
            # увеличиваем счётчик i на 1 для перехода к следующему элементу
            i += 1
    # после завершения цикла выводим максимальное число
    print("Максимальное число в списке:", max_number) 