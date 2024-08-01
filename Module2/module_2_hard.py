# Дополнительное практическое задание по модулю "Основные операторы"

# Написать пары чисел друг за другом, чтобы данное число было кратно сумме их значений.
def pair_search(n):
    return ''.join([str(n1) + str(n2) for n1 in range(1, n//2 + n%2) for n2 in range(n1 + 1, n - n1 + 1) if n % (n1+n2) == 0])


for i in range(3, 21):
    print(i, '-', pair_search(i))
