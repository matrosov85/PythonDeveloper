# Домашнее задание по теме "Блокировки и обработка ошибок"

from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    # Увеличение баланса
    def deposit(self):
        # 100 транзакций на случайную сумму от 50 до 500
        for _ in range(100):
            replenish = randint(50, 500)
            self.balance += replenish
            print(f'Пополнение: {replenish}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    # Уменьшение баланса
    def take(self):
        # 100 транзакций на случайную сумму от 50 до 500
        for _ in range(100):
            withdraw = randint(50, 500)
            print(f'Запрос на {withdraw}')
            if withdraw <= self.balance:
                self.balance -= withdraw
                print(f'Снятие: {withdraw}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
