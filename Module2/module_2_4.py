# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

# Дан список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
primes = []
not_primes = []

for number in numbers:
    is_prime = True
    if number < 2:
        continue
    for divider in range(2, int(number**0.5)+1):
        if number % divider == 0:
            not_primes.append(number)
            is_prime = False
            break
    if is_prime:
        primes.append(number)

print('Primes:', primes)
print('Not Primes:', not_primes)
