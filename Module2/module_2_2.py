# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else"

# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
first = int(input())
second = int(input())
third = int(input())

# Написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
