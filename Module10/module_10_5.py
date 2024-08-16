# Домашнее задание по теме "Многопроцессное программирование"

from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name) as file:
        for line in file:
            all_data.append(line)


filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start = datetime.now()
for filename in filenames:
    read_info(filename)
end = datetime.now()
print(end - start)

# Многопроцессный
if __name__ == '__main__':
    with Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start)
