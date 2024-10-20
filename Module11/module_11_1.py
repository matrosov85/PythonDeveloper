# Домашнее задание по теме "Обзор сторонних библиотек Python"

import requests
import matplotlib.pyplot as plt
import numpy as np


# Пример использование библиотеки requests
city = 'Москва'
appid = '79d1ca96933b0328e1c7e3e7a26cb347'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={appid}'

weather = requests.get(url).json()
temperature = round(weather['main']['temp'])
feels_like = round(weather['main']['feels_like'])

print(f'Температура воздуха в городе {city}: {temperature}°')
print(f'Ощущается как: {feels_like}°\n')


# Пример использования библиотеки numpy
data = np.random.randn(100)
x = np.arange(len(data))
sorted_data = np.sort(data)

print(f'Исходные данные:\n {data}\n')
print(f'Отсортированные данные:\n {sorted_data}')


# Пример использования библиотеки matplotlib
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, data, color='blue')
ax.plot(x, sorted_data, color='red')

plt.show()
