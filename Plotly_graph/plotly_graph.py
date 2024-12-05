import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
np.random.seed(1)

# Построение карты (контурный график)
# Загрузка данных
data = pd.read_csv('../CSV_files/relief.csv', sep=',', skiprows=0)

# Извлечение координат и высот
x = data['X']
y = data['Y']
z = data['Z']

# Создание фигур с контурным графиком с сеткой
fig = go.Figure(data=go.Contour(
    z=z,
    x=x,
    y=y,
    contours=dict(
        start=min(z),
        end=max(z),
        size=(max(z) - min(z)) / 12,  # Количество контуров можно настроить
    ),
    colorbar=dict(title='Высота, м'),
))

# Настройка графика
fig.update_layout(
    title='Рельеф',
    xaxis_title='X координаты',
    yaxis_title='Y координаты',
    xaxis=dict(showgrid=True, gridcolor='LightGray'),  # Настройки сетки для оси X
    yaxis=dict(showgrid=True, gridcolor='LightGray'),  # Настройки сетки для оси Y
)

# Показываем график
fig.show()


# Построение 3D карты (контурный график)
# Загрузка данных
data = pd.read_csv('../CSV_files/fakemap.csv', sep=',', skiprows=0)

# Преобразование значений в массивы NumPy
X = data['X'].values
Y = data['Y'].values
Z = data['Z'].values

# Уникальные значения для X и Y
x_unique = sorted(data['X'].unique())
y_unique = sorted(data['Y'].unique())

# Создаем двумерные массивы для X, Y
X_grid, Y_grid = np.meshgrid(x_unique, y_unique)

# Используем griddata для интерполяции Z на сетку X_grid, Y_grid
Z_grid = griddata((X, Y), Z, (X_grid, Y_grid), method='linear')

# Создание 3D контурного графика
fig = go.Figure(data=go.Surface(z=Z_grid, x=X_grid, y=Y_grid, colorscale='Viridis'))

# Настройки графика
fig.update_layout(title='3D fakemap', scene=dict(
    xaxis_title='X координаты',
    yaxis_title='Y координаты',
    zaxis_title='Z координаты'))

# Отображение графика
fig.show()


# Создание гистограммы

x0 = np.random.randn(500)
x1 = np.random.randn(500) + 1

gist = go.Figure()
gist.add_trace(go.Histogram(
    x=x0,
    histnorm='percent',
    name='date1',
    xbins=dict(
        start=-4.0,
        end=4.0,
        size=0.5),
    marker_color='#EB68B5',
    opacity=0.5
))
gist.add_trace(go.Histogram(
    x=x1,
    histnorm='percent',
    name='date2',
    xbins=dict(
        start=-4.0,
        end=4,
        size=0.5),
    marker_color='#330C53',
    opacity=0.5
))

gist.update_layout(
    title_text='Создание гистограммы',
    xaxis_title_text='0x',
    yaxis_title_text='0у',
    bargap=0.2,     # расстояние между столбцами в разных значениях 0х
    bargroupgap=0.1     # расстояние между столбцами в одном значении 0х
)

gist.show()

# Создание подвижных графиков

dvig = go.Figure(
    data=[go.Scatter(x=[0, 1], y=[0, 2])],
    layout=go.Layout(
        xaxis=dict(range=[0, 7], autorange=False),
        yaxis=dict(range=[0, 7], autorange=False),
        title=dict(text="Начальный заголовок"),
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Начать",
                          method="animate",
                          args=[None])])]
    ),
    frames=[go.Frame(data=[go.Scatter(x=[1, 1], y=[1, 2])]),
            go.Frame(data=[go.Scatter(x=[1, 4], y=[1, 6])]),
            go.Frame(data=[go.Scatter(x=[3, 6], y=[5, 6])],
                     layout=go.Layout(title_text="Конечный заголовок"))]
)

dvig.show()
