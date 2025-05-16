# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

# def switch_it_up(number):
#     pass

number = ['One',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'None'
    ]

def switch_it_up(number):
    n = int(input('введите число от 1 до 9: '))
    while n > 0 and n < 10:
        print(f'switch_it_up ({(n)}) -> {number[n-1]}')
        break
    while n < 0 or n > 9:
        print(f'switch_it_up ({n}) -> {None}')
        break

switch_it_up(number)

# n = int(input('введите число от 1 до 9: '))
# print(n)
# while n == 1:
#     print('witch_it_up(1) -> One')
#     break
# while n == 2:
#     print('witch_it_up(2) -> Two')
#     break
# while n == 3:
#     print('witch_it_up(3) -> Three')
#     break
# while n == 4:
#     print('witch_it_up(4) -> Four')
#     break
# while n == 5:
#     print('witch_it_up(5) -> Five')
#     break
# while n == 6:
#     print('witch_it_up(6) -> Six')
#     break
# while n == 7:
#     print('witch_it_up(7) -> Seven')
#     break
# while n == 8:
#     print('witch_it_up(8) -> Eigth')
#     break
# while n == 9:
#     print('witch_it_up(9) -> Nine')
#     break
# while  n < 1 or n > 9:
#     print('witch_it_up(9) -> Nine')
#     break