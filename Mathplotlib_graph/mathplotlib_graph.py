import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from matplotlib.animation import FuncAnimation

# Построение карты (контурный график)
# Шаг 1: Загрузка данных
data = pd.read_csv('../CSV_files/map.csv', sep=',', skiprows=0)

# Удаление строк с пустыми значениями
#data = data.dropna()
# Преобразование значений в массивы NumPy
x = data['X'].values
y = data['Y'].values
z = data['Z'].values

# Создание сетки для контурного графика
X = np.unique(x)
Y = np.unique(y)

# Создание двумерных сеток координат
X, Y = np.meshgrid(X, Y)

# Интерполяция значений Z для сетки
Z = griddata((x, y), z, (X, Y), method='linear')

# Построение контурного графика
plt.figure(figsize=(10, 8))
contour = plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(contour, label='Мощность просадочных грунтов, м')
plt.title('Карта мощности просадочных грунтов')
plt.xlabel('X координаты')
plt.ylabel('Y координаты')

# Показать график
plt.show()

# Создание 3D карты (3D контурный график)
# Шаг 1: Загрузка данных
data = pd.read_csv('../CSV_files/map.csv', sep=',', skiprows=0)

# Преобразование значений в массивы NumPy
x = data['X'].values
y = data['Y'].values
z = data['Z'].values

# Определение уникальных значений X и Y для создания сетки
xi = np.linspace(min(x), max(x), 100)
yi = np.linspace(min(y), max(y), 100)
xi, yi = np.meshgrid(xi, yi)

# Интерполяция значений Z для сетки
zi = griddata((x, y), z, (xi, yi), method='linear')

# Создание 3D графика
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Построение 3D контурного графика
contour = ax.contour3D(xi, yi, zi, levels=50, cmap='viridis')

# Добавление цвета к графику
fig.colorbar(contour, ax=ax, label='Мощность просадочных грунтов, м')

# Настройка заголовков и меток
ax.set_title('3D Карта мощности просадочных грунтов')
ax.set_xlabel('X координаты')
ax.set_ylabel('Y координаты')
ax.set_zlabel('Высота (Z)')

# Показать график
plt.show()


# Создание гистограммы

f2 = plt.figure(figsize=(14, 10))
ax = f2.add_subplot()
x = np.arange(12)
y1 = np.random.randint(1, 22, len(x))
y2 = np.random.randint(4, 28, len(x))
w = 0.2
f2.suptitle('Создание гистограммы', size='20')
ax.set_xlabel('0x', size='14')
ax.set_ylabel('0y', size='14')
ax.bar(x - w/2, y1, width=w, label='data1')
ax.bar(x + w/2, y2, width=w, label='data2')
ax.grid(which='major', color='#2D1F2A', linewidth=1)
ax.legend()
plt.show()


# Создание круговой диаграммы

plt.figure(figsize=(10, 10))
vals = [168.1, 130.6, 74.4, 77.4, 61.5, 238]
color = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', ]
exp = [0.3, 0.2, 0, 0, 0, 0.1]
labels = ['KIA', 'Hyundai', 'Toyota', 'Volkswagen', 'Skoda', 'Остальные']
plt.pie(vals, labels=labels, autopct='%.1f%%', startangle=90, colors=color, explode=exp)
plt.title('Топ по продажам автомобилей в 2022 году', fontsize=16)
plt.axis('equal')
plt.show()


# Создание анимационного графика

def update_cos(frame, line, x):# Обновляем данные графика по оси Y для текущего кадра
    line.set_ydata(np.cos(x + frame))  # Рассчитываем косинус с учетом сдвига по времени (frame)
    return [line]  # Возвращаем обновленный объект линии

f5, ax = plt.subplots() # Создаем объект Figure и ось Axes

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1) # Задаем диапазон X от -2π до 2π с шагом 0.1
y = np.cos(x) # Инициализируем массив Y как косинус этих значений

line, = ax.plot(x, y) # Рисуем начальную линию графика

phasa = np.arange(0, 4 * np.pi, 0.1) # Задаем диапазон фреймов (сдвигов по времени) от 0 до 4π

# Создаем анимацию с помощью FuncAnimation
animation = FuncAnimation(
    f5,
    func=update_cos,
    frames=phasa,
    fargs=(line, x),
    interval=30,
    repeat=True
)

plt.show()