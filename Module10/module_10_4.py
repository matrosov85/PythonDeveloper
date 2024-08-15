# Домашнее задание по теме "Очереди для обмена данными между потоками"
from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name, table=None):
        super().__init__()
        self.name = name
        self.table = table

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    # Приём гостей
    def guest_arrival(self, *guests):
        for guest in guests:
            # Поиск свободного стола для гостя
            for table in self.tables:
                if table.guest is None:  # Если свободный стол найден
                    table.guest = guest  # Стол занимается гостем
                    guest.table = table  # Гость садится за стол
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest.start()  # Гость начинает приём пищи
                    break
            if guest.table is None:  # Если свободный стол не найден
                self.queue.put(guest)  # Гость встает в очередь
                print(f'{guest.name} в очереди')

    # Обслуживание гостей...
    def discuss_guests(self):
        # ... продолжается пока в очереди есть гости или есть занятые столы
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                # Если за столом есть гость, который закончил приём пищи
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None  # Освобождаем стол
                    if not self.queue.empty():  # Если в очереди есть гость
                        table.guest = self.queue.get()  # Следующий в очереди гость садится за стол
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()  # Гость начинает приём пищи


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
