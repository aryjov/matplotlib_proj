import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

st.set_option('deprecation.showPyplotGlobalUse', False)


st.sidebar.title("Специальные графики")

st.title('Специальные графики')

menu = st.sidebar.radio('***',
    ("Специальные графики",
     "Графики с использованием цветовых сеток",
     "Графики с полярными координатами",
     "Ступенчатый график",
     "Стековый график",
     "Stem-график",
     "Точечный график",
    )
)

if menu == "Специальные графики":
    """
    **Графики с использованием цветовых карт\n
    **Графики с полярными координатами\n
    **Ступенчатый график\n
    **Стековый график\n
    **Stem-график\n
    **Точечный график\n
    """


if menu == "Графики с использованием цветовых сеток":
    st.markdown("""
    ## Графики с использованием цветовых сеток
    Цветовая сетка представляет собой поле, заполненное цветом, который
    определяется цветовой картой и численными значениями элементов
    переданного двумерного массива.
                    
    Рассмотрим две функции для построения цветовой сетки: imshow() и
    pcolormesh().
                    
    ## imshow()
                    
    Основное назначение функции imshow() состоит в представлении 2D
    растров. Это могут быть картинки, двумерные массивы данных, матрицы
    и т. п.
            
    Рассмотрим некоторые из параметров функции imshow():
    - **X**: массив или PIL изображение
        - Поддерживаются следующие размерности массивов:
            - (M, N): двумерный массив со скалярными данными.
            - (M, N, 3): массив с RGB значениями (0-1 float или 0-255 int).
            - (M, N, 4): массив с RGBA значениями (0-1 float или 0-255 int).
    - **cmap**: str или Colormap, optional
        - Цветовая карта изображения (см. "4.4.1 Цветовые карты (colormaps)")
    - **norm**: Normalize, optional
        - Нормализация - приведение скалярных данных к диапазону [0,1] перед использованием cmap. 
          Этот параметр игнорируется для RGB(A) данных.
    - **aspect**: {'equal', 'auto'} или float, optional
        - 'equal': обеспечивает соотношение сторон равное 1;
        - 'auto': соотношение не изменяется.
    - **interpolation**: str, optional
        - Алгоритм интерполяции. Доступны следующие значения: 'none', 'nearest', 'bilinear', 'bicubic', 
          'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 
          'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'.
    - **alpha**: скалярное значение, optional
        - Прозрачность. Определяется в диапазоне от 0 до 1. Параметр игнорируется для RGBA значения.
    - **vmin, vmax**: скалярное значение, optional
        - Численные значения vmin и vmax (если параметр norm не задан явно) определяют диапазон данных, 
          который будет покрыт цветовой картой. По умолчанию цветовая карта охватывает весь диапазон 
          значений отображаемых данных. Если используется параметр norm, то vmin и vmax игнорируются.
    - **origin**: {'upper', 'lower'}, optional
        - Расположение начал координат (точки [0,0]): 'upper' - верхний левый, 'lower' - нижний левый угол 
          координатной плоскости.
    - **extent**: (left, right, bottom, top), optional
        - Изменение размеров изображения вдоль осей x, y.
    - **filterrad**: float > 0, optional; значение по умолчанию: 4.0
        - Параметр filter radius для фильтров, которые его используют, например: 'sinc', 'lanczos' или 
          'blackman'.
            
    Пример, использующий параметры из приведенного выше списка:
    """)
    code = """
           data = np.random.rand(10, 10)
    fig, ax = plt.subplots(figsize=(6, 6), constrained_layout=True)
    p1 = ax.imshow(data, cmap='winter', aspect='equal', vmin=-1, vmax=1, origin='lower')
    fig.colorbar(p1, ax=ax)
           """
    st.code(code, language='python')

    
    data = np.random.rand(10, 10)
    fig, ax = plt.subplots(figsize=(6, 6), constrained_layout=True)
    p1 = ax.imshow(data, cmap='winter', aspect='equal', vmin=-1, vmax=1, origin='lower')
    fig.colorbar(p1, ax=ax)
    st.pyplot(fig)


    st.markdown("""
    ## pcolormesh()

    Ещё одной функцией для визуализации 2D наборов данных является `pcolormesh()`. В библиотеке Matplotlib есть ещё одна функция с аналогичным функционалом - `pcolor()`, в отличие от неё, рассматриваемая нами `pcolormesh()`, более быстрая и является лучшим вариантом в большинстве случаев. 

    ### Параметры функции pcolormesh():

    - **C**: массив
        - 2D массив скалярных значений.
    - **cmap**: str или Colormap, optional
        - См. cmap в imshow().
    - **norm**: Normalize, optional
        - См. norm в imshow().
    - **vmin, vmax**: scalar, optional; значение по умолчанию: None
        - См. vmin, vmax в imshow().
    - **edgecolors**: {'none', None, 'face', color, color sequence}, optional; значение по умолчанию: 'none'
        - Цвет границы. Возможны следующие варианты:
            - 'none' или '': без отображения границы;
            - None: черный цвет;
            - 'face': используется цвет ячейки;
            - Можно выбрать цвет из доступных наборов.
    - **alpha**: scalar, optional; значение по умолчанию: None
        - См. alpha в imshow().
    - **shading**: {'flat', 'gouraud'}, optional
        - Стиль заливки. Доступные значения:
            - 'flat': сплошной цвет заливки для каждого квадрата;
            - 'gouraud': для каждого квадрата будет использован метод затенения Gouraud.
    - **snap**: bool, optional; значение по умолчанию: False
        - Привязка сетки к границам пикселей.

    ### Пример использования функции pcolormesh():
    """)
    code = """
           np.random.seed(123)
    data = np.random.rand(5, 7)
    fig, ax = plt.subplots()
    pcm = ax.pcolormesh(data, cmap='plasma', edgecolors='k', shading='flat')
    cbar = plt.colorbar(pcm)
           """
    st.code(code, language='python')

    np.random.seed(123)
    data = np.random.rand(5, 7)
    fig, ax = plt.subplots()
    pcm = ax.pcolormesh(data, cmap='plasma', edgecolors='k', shading='flat')
    cbar = plt.colorbar(pcm)
    st.pyplot(fig)


if menu == "Графики с полярными координатами":
    st.markdown("""
    ### Графики с полярными координатами

    Для создания графиков с полярными координатами в библиотеке Matplotlib выполните следующие шаги:

        **Создание фигуры и осей**: Используйте метод `subplots()` с параметром `subplot_kw={'projection': 'polar'}`.

    """)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    theta = np.linspace(0, 2*np.pi, 100)
    r = np.abs(np.sin(2*theta))
    ax.plot(theta, r, label='Полярные координаты')
    ax.set_title('Полярные координаты')
    ax.legend()
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)

if menu == "Ступенчатый график":
    st.markdown("""
    ## Ступенчатый график
    Рассмотрим ступенчатый график. Он строится с
    помощью функции step():
    
    ```python
    step(x, y, [fmt], *, data=None, where='pre', **kwargs)
    ```
    
    которая принимает следующий набор параметров:
    
    - `x`: массив - набор данных для оси абсцисс.
    - `y`: массив - набор данных для оси ординат.
    - `fmt`: str, optional - формат линии (см. функцию plot()).
    - `data`: индексируемый объект, optional - метки.
    - `where`: {'pre', 'post', 'mid'}, optional; значение поумолчанию: 'pre' - определяет место, где будет установлен шаг:
        - 'pre': значение y ставится слева от значения x, т.е. значение 
        y[i] определяется для интервала (x[i-1]; x[i]);
        - 'post': значение y ставится справа от значения x, т.е.
        значение y[i] определяется для интервала (x[i]; x[i+1]);
        - 'mid': значение y ставится в середине интервала.
    """)

    code = """
           x = np.arange(0, 7)
    y = x
    where_set = ['pre', 'post', 'mid']
    st.set_option('deprecation.showPyplotGlobalUse', False)
    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    for i, ax in enumerate(axs):
        ax.step(x, y, 'g-o', where=where_set[i])
        ax.grid()
           """
    st.code(code, language='python')

    x = np.arange(0, 7)
    y = x
    where_set = ['pre', 'post', 'mid']
    st.set_option('deprecation.showPyplotGlobalUse', False)
    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    for i, ax in enumerate(axs):
        ax.step(x, y, 'g-o', where=where_set[i])
        ax.grid()

    st.pyplot(fig)
    
if menu == "Стековый график":
    st.markdown("""
    ## Стековый график
    Для построения стекового графика используется функция stackplot().
    Суть его в том, что графики отображаются друг над другом, и каждый
    следующий является суммой предыдущего и заданного:
        """)
    
    code = """
      x = np.arange(0, 11, 1)
    y1 = np.array([(-0.2)*i**2+2*i for i in x])
    y2 = np.array([(-0.4)*i**2+4*i for i in x])
    y3 = np.array([2*i for i in x])
    labels = ['y1', 'y2', 'y3']
    fig, ax = plt.subplots()
    ax.stackplot(x, y1, y2, y3, labels=labels)
    ax.legend(loc='upper left')
           """
    st.code(code, language='python')

    x = np.arange(0, 11, 1)
    y1 = np.array([(-0.2)*i**2+2*i for i in x])
    y2 = np.array([(-0.4)*i**2+4*i for i in x])
    y3 = np.array([2*i for i in x])
    labels = ['y1', 'y2', 'y3']
    fig, ax = plt.subplots()
    ax.stackplot(x, y1, y2, y3, labels=labels)
    ax.legend(loc='upper left')

    st.pyplot(fig)

    st.markdown("""
    Верхний край области y2 определяется как сумма значений из наборов
    y1 и y2, y3 - соответственно сумма y1, y2 и y3
        """)

if menu == "Stem-график":
    st.markdown("""
    ## Stem-график
    Визуально этот график выглядит как набор линий от точки с
    координатами (x, y) до базовой линии, в верхней точке которой ставится
    маркер:
        """)
    
    code = """
        x = np.arange(0, 10.5, 0.5)
        y = np.array([(-0.2)*i**2+2*i for i in x])
        plt.stem(x, y)
           """
    st.code(code, language='python')
    
    x = np.arange(0, 10.5, 0.5)
    y = np.array([(-0.2)*i**2+2*i for i in x])
    plt.stem(x, y)
    st.pyplot()

    st.markdown("""
    Дополнительные параметры функции stem():

- `linefmt`: str, optional
  - Стиль вертикальной линии.
- `markerfmt`: str, optional
  - Формат маркера.
- `basefmt`: str, optional
  - Формат базовой линии.
- `bottom`: float, optional; значение по умолчанию: 0
  - y-координата базовой линии.

Пример, демонстрирующий работу с дополнительными параметрами:
        """)
    code = """
       plt.stem(x, y, linefmt='r--', markerfmt='^', bottom=1)
             """
    st.code(code, language='python')
    plt.stem(x, y, linefmt='r--', markerfmt='^', bottom=1)

    st.pyplot()

    
if menu == "Точечный график":
    st.markdown("""
    ## Точечный график
    Для отображения точечного графика предназначена функция scatter(). 
    В простейшем виде точечный график можно получить, передав функции scatter() наборы точек для x, y координат:

    ```python
    x = np.arange(0, 10.5, 0.5)
    y = np.cos(x)
    plt.scatter(x, y)
        """)
    x = np.arange(0, 10.5, 0.5)
    y = np.cos(x)
    plt.scatter(x, y)
    st.pyplot()

    st.markdown("""
    Для более детальной настройки отображения необходимо воспользоваться дополнительными параметрами функции scatter(). Сигнатура ее вызова имеет следующий вид:

```python
scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None,
        vmin=None, vmax=None, alpha=None, linewidths=None, verts=None,
        edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)
    Рассмотрим некоторые из ее параметров:
    • x: массив, shape(n, )
    ◦ Набор данных для оси абсцисс.
    • Y: массив, shape(n, )
    ◦ Набор данных для оси ординат.
    • s: скалярная величина или массив, shape(n, ), optional
    ◦ Масштаб точек.
    • c: color, набор color элементов, optional
    ◦ Цвет.
    • marker: MarkerStyle, optional
    ◦ Стиль точки объекта.
    • cmap: Colormap, optional, значение по умолчанию: None
    ◦ Цветовая схема.
    • norm: Normalize, optional, значение по умолчанию: None
    ◦ Нормализация данных.
    • alpha: скалярная величина, optional, значение по умолчанию:
    None
    ◦ Прозрачность.
        • linewidths: скалярная величина или массив, optional, значение
    по умолчанию: None
    ◦ Ширина границы маркера.
    • edgecolors: {'face', 'none', None}, color или набор color
    элементов, optional.
    ◦ Цвет границы.
    Пример использования параметров функции scatter():
        """)
    code = """
        x = np.arange(0, 10.5, 0.5)
        y = np.cos(x)
        plt.scatter(x, y, s=80, c='r', marker='D', linewidths=2, edgecolors='g')
            """
    st.code(code, language='python')
    x = np.arange(0, 10.5, 0.5)
    y = np.cos(x)
    plt.scatter(x, y, s=80, c='r', marker='D', linewidths=2, edgecolors='g')
    st.pyplot()
