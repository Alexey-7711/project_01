#  Задача 3
# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней
    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней
    # Введите номер месяца: 15
    # Такого месяца нет!


n = int(input('Введите номер месяца: ')) 
if n == 1:
    print ('Вы ввели Январь. 31 день')
elif n == 2:     
    print ('Вы ввели Февраль. 28 день')
elif n == 3:    
    print ('Вы ввели Март. 31 день')
elif n == 4:
    print ('Вы ввели Апрель. 30 день')
elif n == 5:
    print ('Вы ввели Май. 31 день')
elif n == 6:
    print ('Вы ввели Июнь. 30 день')
elif n == 7:
    print ('Вы ввели Июль. 31 день')
elif n == 8:
    print ('Вы ввели Август. 31 день')
elif n == 9:
    print ('Вы ввели Сентябрь. 30 день')
elif n == 10:
    print ('Вы ввели Октябрь. 31 день')
elif n == 11:
    print ('Вы ввели Ноябрь. 30 день')
elif n == 12:
    print ('Вы ввели Декабрь. 31 день')
else:
    print ('Такого месяца нет!')