import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)


st.sidebar.title("Трехмерные графики")

st.title('Трехмерные графики')

menu = st.sidebar.radio('***',
    ("Основные функции",
     "Линия",
     "Поверхность",
     "Задание графика параметрически",
    )
)

if menu == "Основные функции":
    """
    ## Основные функции\n
    **fig = plt.figure()** - Создать окна для отображения графиков.\n
    **ax = fig.add_subplot(projection='3d')** - Добавить оси в окно отображения графиков.\n
    **ax.plot()** - Построить график в виде линии\n
    **ax.scatter()** - Постоить график в виде точек\n
    **ax.plot_surface()** - Построить график в виде поверхности\n
    **ax.elev, ax.azim** - Указать угол обзора\n
    **ax.quiver()** - Построить стрелки направления\n
    **ax.stem()** - Нарисовать стебли\n
    **ax.voxels()** - Построить объемные воксели\n
    **ax.add_patch()** - Добавить 2D объект\n
    **ax.bar3d()** - Построить 3D столбчатые диаграммы\n
            """


if menu == "Линия":

    x_value = st.slider(
        'Диапазон значений x',
        -10, 10, (-5, 5))

    page = st.selectbox("***",
                        ["Линия",
                         "Точки",
                         ])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    x = np.linspace(min(x_value), max(x_value), 100)
    y = np.linspace(-5, 5, 100)
    z = np.sin(x)
    ax.elev = st.slider('углы обзора', 0, 360, 45)
    ax.azim = st.slider('***', 0, 360, 145)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    if page == "Линия":
        ax.plot(x, y, z)
    if page == "Точки":
        ax.scatter(x, y, z)
    st.pyplot()

    with st.expander("Код"):
        code = """
           x = np.linspace(min(x_value), max(x_value), 100)
           y = np.linspace(-5, 5, 100)
           z = np.sin(x)
           fig = plt.figure()
           ax = fig.add_subplot( projection='3d')
           if page == "Линия":
                ax.plot(x, y, z)
           if page == "Точки":
                ax.scatter(x, y, z)
           """
        st.code(code, language='python')


if menu =="Поверхность":

    col1, col2 = st.columns(2)

    with col1:
        x_value = st.slider(
            'диапазон значений x',
            -10, 10, (-5, 5))
    with col2:
        y_value = st.slider(
            'диапазон значений y',
            -10, 10, (-5, 5))

    num_points = st.slider('Количество точек по осям x, y', min_value=10, max_value=100, value=50)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    with col2:
        ax.elev = st.slider("***", 0, 360, 45)
        page = st.selectbox("***",
                            ["Поверхность",
                             "Сетка",
                             "Точки",
                             ])
    with col1:
        ax.azim = st.slider('углы обзора', 0, 360, 45)
        func = st.text_input("Функция z(x,y) =", "np.sin(np.sqrt(x ** 2 + y ** 2))")

    X = np.linspace(min(x_value), max(x_value), num_points)
    Y = np.linspace(min(y_value), max(y_value), num_points)
    x, y = np.meshgrid(X, Y)
    z = 0
    try:
        exec(f"z={func}")

        if isinstance(z, (int, float)):
            mas = np.ones((X.size, Y.size))
            z = mas*z

        if page == "Поверхность":
            ax.plot_surface(x, y, z, cmap='viridis')
        if page == "Сетка":
            ax.plot_wireframe(x, y, z, color="green")
        if page == "Точки":
            ax.scatter(x, y, z, c=z, cmap='turbo')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        st.pyplot()

    except:
        """### Неверное задание функции"""

    with st.expander("Код"):
        code = """
                fig = plt.figure()
                ax = fig.add_subplot(projection='3d')
            
                x = np.linspace(min(x_value), max(x_value), num_points)
                y = np.linspace(min(y_value), max(y_value), num_points)
                x, y = np.meshgrid(x, y)
                z = np.sin(np.sqrt(x ** 2 + y ** 2))
            
                if page == "Поверхность":
                    ax.plot_surface(x,y,z, cmap='viridis')
                if page == "Сетка":
                    ax.plot_wireframe(x, y, z, color="green")
                if page == "Точки":
                    ax.scatter(x, y, z, c=z, cmap='turbo')
                """
        st.code(code, language='python')

if menu == "Задание графика параметрически":
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    t = np.linspace(0, 4 * np.pi, 100)
    x = np.cos(t)
    y = np.sin(t)
    z = t / (4 * np.pi)
    ax.elev, ax.azim = 45, 30
    ax.plot(x, y, z)
    st.pyplot()

    with st.expander("Код"):
        code = """
                fig = plt.figure()
                ax = fig.add_subplot(projection='3d')
            
                t = np.linspace(0, 4 * np.pi, 100)
                x = np.cos(t)
                y = np.sin(t)
                z = t / (4 * np.pi)
                ax.elev, ax.azim = 45, 30
                ax.plot(x, y, z)
                """
        st.code(code, language='python')

if menu == "Задание графика параметрически - поверхность":
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Make data
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

    # Plot the surface
    ax.plot_surface(x, y, z)

    # Set an equal aspect ratio
    ax.set_aspect('equal')
    st.pyplot()

    with st.expander("Код"):
        code = """
                fig = plt.figure()
                ax = fig.add_subplot(projection='3d')
            
                # Make data
                u = np.linspace(0, 2 * np.pi, 100)
                v = np.linspace(0, np.pi, 100)
                x = 10 * np.outer(np.cos(u), np.sin(v))
                y = 10 * np.outer(np.sin(u), np.sin(v))
                z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
            
                # Plot the surface
                ax.plot_surface(x, y, z)
            
                # Set an equal aspect ratio
                ax.set_aspect('equal')
                """
        st.code(code, language='python')


    st.pyplot()
