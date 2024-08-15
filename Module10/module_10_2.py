# Домашнее задание по теме "Потоки на классах"

from threading import Thread
from time import sleep


class Knight(Thread):
    ENEMIES = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = self.ENEMIES
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies:
            sleep(1)
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            self.days += 1
            print(f'{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
sleep(1)
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
