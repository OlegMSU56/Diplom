import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")

# Построение карты
# Загрузка данных из файла CSV
data = pd.read_csv('../CSV_files/map.csv', sep=',', skiprows=0)

# Установка стиля для графиков
sns.set(style='whitegrid')

# Создание карты изолиний
plt.figure(figsize=(10, 8))
contour = plt.tricontourf(data['X'], data['Y'], data['Z'], levels=50, cmap='viridis')

# Добавление цветовой шкалы и подписи
colorbar = plt.colorbar(contour)
colorbar.set_label('Мощность просадочных грунтов, м')  # Замените "единицы" на единицы измерения, если известно

# Заголовок и подписи осей
plt.title('Карта мощности просадочных грунтов')
plt.xlabel('X координаты')
plt.ylabel('Y координаты')
plt.grid(True)

# Показываем  графика
plt.show()



# Создание гистограммы с разделением по группам
diamonds = sns.load_dataset("diamonds")

# Установка размера графика
plt.figure(figsize=(12, 6))

# Гистограмма с разделением по группам
sns.histplot(data=diamonds, x='carat', hue='cut', multiple='stack', bins=30, kde=False, alpha=0.7)

# Настройка заголовка и подписей
plt.title('Гистограмма распределения веса бриллиантов по огранке')
plt.xlabel('Вес в каратах')
plt.ylabel('Количество')

# Создание пользовательских элементов легенды
handles = []
labels = diamonds['cut'].unique()  # Получаем уникальные значения для типа огранки

# Определяем цвета для каждой категории
colors = sns.color_palette("husl", len(labels))

for color, label in zip(colors, labels):
    handles.append(plt.Line2D([0], [0], color=color, lw=4))

# Добавление легенды
plt.legend(handles, labels, title='Тип огранки')

# Показываем график
plt.show()

# Графики плотности для каждого типа огранки
plt.figure(figsize=(12, 6))
for cut_type in diamonds['cut'].unique():
    subset = diamonds[diamonds['cut'] == cut_type]
    sns.kdeplot(subset['carat'], label=cut_type, fill=True, alpha=0.5)

plt.title('График плотности распределения веса бриллиантов по огранке')
plt.xlabel('Вес в каратах')
plt.ylabel('Плотность')
plt.legend(title='Тип огранки')
plt.show()

# Создание "скрипичного" графика
plt.figure(figsize=(12, 6))
sns.violinplot(x='cut', y='carat', data=diamonds)
plt.title('Скрипичный график распределения веса бриллиантов по типу огранки')
plt.xlabel('Тип огранки')
plt.ylabel('Вес в каратах')
plt.show()