# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# a = input('Введите трехзначное число: ')
# a1 = int(a[0])
# a2 = int(a[1])
# a3 = int(a[2])
# print (f'Сумма чисел = {a1+a2+a3}')



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал 
# каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза
#  больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
# если получается некорректное разделение - напечатать "Неверное S"

# s = int(input('Введите суммарное количество журавликов: '))

# if s%6==0:
#     print(f'У Сережи и Пети по {round(s/6)} журавликов, у Кати {round((s/6)*4)} журавликов')
# else:
#     print('Неверное S')







# Задача 6: Вы пользуетесь общественным транспортом?
#  Вероятно, вы расплачивались за проезд и получали билет
#  с номером. Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна 
# сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no


# a = input('Введите шестизначное число: ')
# a1 = int(a[0])
# a2 = int(a[1])
# a3 = int(a[2])
# a4 = int(a[3])
# a5 = int(a[4])
# a6 = int(a[5])

# if a1+a2+a3==a4+a5+a6:
#     print (f'Билет счастливый, сумма чисел = {a1+a2+a3}')
# else:
#     print('Билет не счастливый')




# Задача 8: Требуется определить, можно ли от шоколадки
#  размером n × m долек отломить k долек, если разрешается
#  сделать один разлом по прямой между дольками (то есть 
# разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

