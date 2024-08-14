# Домашнее задание по теме "Декораторы"

# Функция декоратор, которая проверяет число на простоту
def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        prime = True
        for divider in range(2, int(number ** 0.5) + 1):
            if number % divider == 0:
                prime = False
                print('Составное')
                break
        if prime:
            print('Простое')
        return number
    return wrapper


# Функция, которая складывает 3 числа
@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
