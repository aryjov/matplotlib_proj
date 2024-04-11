import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

with st.sidebar:
    add_radio = st.radio(
        "",
        ("Столбчатые диаграммы", "График на плоскости", "Размещение графиков в кадре")
    )
"""
# Графики одномерной функции
"""    

if (add_radio == "Столбчатые диаграммы"):

    """
    ## Работа со столбчатыми диаграммами  
    """
    option = st.selectbox(
        '',
        ('Базовый случай', 'Несколько столбчатых диаграмм на одном графике', 'Диаграмма вместе с кривой'))
    if (option == 'Базовый случай'):
        """
        ### Простая столбчатая диаграмма
        """
        ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        dev_y = [38496, 42000, 46752, 49320, 53200,
                56000, 62316, 64928, 67317, 68748, 73752]
        plt.bar(ages_x, dev_y, color="blue", label="Все разработчики", edgecolor='black', linewidth=1.2, zorder = 3)
        plt.grid(zorder=0)
        plt.legend()
        
        plt.title("Средняя зарплата по возрасту")
        plt.xlabel("Возраст")
        plt.ylabel("Средняя зарплата (USD)")
        plt.tight_layout()
        st.pyplot(plt)
        with st.expander("Код"):
            """
            ```python
            ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        dev_y = [38496, 42000, 46752, 49320, 53200,
                56000, 62316, 64928, 67317, 68748, 73752]
        plt.bar(ages_x, dev_y, color="blue", label="Все разработчики", edgecolor='black', linewidth=1.2, zorder = 3)
        plt.grid(zorder=0)
        plt.legend()
        
        plt.title("Средняя зарплата по возрасту")
        plt.xlabel("Возраст")
        plt.ylabel("Средняя зарплата (USD)")
        plt.tight_layout()
        st.pyplot(plt)
        ```
            """
        """
        ### Пример использования текстовых данных в качестве значений по оси Х
        """
        plt.cla()
        data = [1100, 480, 1500]
        cat = ["Первая", "Вторая", "Третья"]
        plt.bar(cat, data, color="blue", label="Пример", edgecolor='black', linewidth=1.2, zorder = 3)
        plt.grid(zorder=0)
        plt.title("Пример")
        st.pyplot(plt)
        with st.expander("Код"):
            """
            ```python
            plt.cla()
        data = [1100, 480, 1500]
        cat = ["Первая", "Вторая", "Третья"]
        plt.bar(cat, data, color="blue", label="Пример", edgecolor='black', linewidth=1.2, zorder = 3)
        plt.grid(zorder=0)
        plt.title("Пример")
        st.pyplot(plt)
        ```
            """
    
    elif (option == 'Несколько столбчатых диаграмм на одном графике'):

        """
        ### Размещение нескольких столбчатых диаграмм на одном графике
        """
        import numpy as np
        width = 0.25
        ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        x_ind = np.arange(len(ages_x))
        dev_y = [38496, 42000, 46752, 49320, 53200,
                56000, 62316, 64928, 67317, 68748, 73752]
        plt.bar(x_ind-width, dev_y, color="#444444", label="Все разработчики", width = width)
        py_dev_y = [45372, 48876, 53850, 57287, 63016,
                    65998, 70003, 70000, 71496, 75370, 83640]
        plt.bar(x_ind, py_dev_y, color="#008fd5", label="Python",  width = width)

        js_dev_y = [37810, 43515, 46823, 49293, 53437,
                    56373, 62375, 66674, 68745, 68746, 74583]
        plt.bar(x_ind+width, js_dev_y, color="#e5ae38", label="JavaScript",  width = width)

        plt.legend()
        plt.xticks(ticks = x_ind, labels = ages_x)
        plt.title("Средняя зарплата по возрасту")
        plt.xlabel("Возраст")
        plt.ylabel("Средняя зарплата (USD)")

        plt.tight_layout()
        st.pyplot(plt)
        with st.expander("Код"):
            """
            ```python
            import numpy as np
        width = 0.25
        ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        x_ind = np.arange(len(ages_x))
        dev_y = [38496, 42000, 46752, 49320, 53200,
                56000, 62316, 64928, 67317, 68748, 73752]
        plt.bar(x_ind-width, dev_y, color="#444444", label="Все разработчики", width = width)
        py_dev_y = [45372, 48876, 53850, 57287, 63016,
                    65998, 70003, 70000, 71496, 75370, 83640]
        plt.bar(x_ind, py_dev_y, color="#008fd5", label="Python",  width = width)

        js_dev_y = [37810, 43515, 46823, 49293, 53437,
                    56373, 62375, 66674, 68745, 68746, 74583]
        plt.bar(x_ind+width, js_dev_y, color="#e5ae38", label="JavaScript",  width = width)

        plt.legend()
        plt.xticks(ticks = x_ind, labels = ages_x)
        plt.title("Средняя зарплата по возрасту")
        plt.xlabel("Возраст")
        plt.ylabel("Средняя зарплата (USD)")

        plt.tight_layout()
        st.pyplot(plt)
        ```
            """
    elif (option == 'Диаграмма вместе с кривой'):
        """
        ### Размещение столбчатой диаграммы и кривой на одном графике
        """
        

        ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

        dev_y = [38496, 42000, 46752, 49320, 53200,
                56000, 62316, 64928, 67317, 68748, 73752]
        
        plt.bar(ages_x, dev_y, color="#444444", label="Все разработчики")
        py_dev_y = [45372, 48876, 53850, 57287, 63016,
                    65998, 70003, 70000, 71496, 75370, 83640]
        plt.plot(ages_x, py_dev_y, color="#008fd5", label="Python", linewidth = 3.5)

        js_dev_y = [37810, 43515, 46823, 49293, 53437,
                    56373, 62375, 66674, 68745, 68746, 74583]
        plt.plot(ages_x, js_dev_y, color="#e5ae38", label="JavaScript", linewidth = 3.5)

        plt.legend()

        plt.title("Средняя зарплата по возрасту")
        plt.xlabel("Возраст")
        plt.ylabel("Средняя зарплата (USD)")

        plt.tight_layout()
        st.pyplot(plt)
        with st.expander("Код"):
            """
            ```python
            ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

        dev_y = [38496, 42000, 46752, 49320, 53200,
                56000, 62316, 64928, 67317, 68748, 73752]
        
        plt.bar(ages_x, dev_y, color="#444444", label="Все разработчики")
        py_dev_y = [45372, 48876, 53850, 57287, 63016,
                    65998, 70003, 70000, 71496, 75370, 83640]
        plt.plot(ages_x, py_dev_y, color="#008fd5", label="Python", linewidth = 3.5)

        js_dev_y = [37810, 43515, 46823, 49293, 53437,
                    56373, 62375, 66674, 68745, 68746, 74583]
        plt.plot(ages_x, js_dev_y, color="#e5ae38", label="JavaScript", linewidth = 3.5)

        plt.legend()

        plt.title("Средняя зарплата по возрасту")
        plt.xlabel("Возраст")
        plt.ylabel("Средняя зарплата (USD)")

        plt.tight_layout()
        st.pyplot(plt)
        ```
            """
elif (add_radio == "График на плоскости"):
    
    
    option = st.selectbox(
        '',
        ('Синус', 'Гауссиан', 'Степенная функция'))
    if (option == 'Синус'):
        x_min = st.sidebar.slider('Минимальное значение x', min_value=-20.0, max_value=0.0, value=-10.0)
        x_max = st.sidebar.slider('Максимальное значение x', min_value=0.0, max_value=20.0, value=10.0)
        num_points = st.sidebar.slider('Количество точек', min_value=10, max_value=1000, value=50)
        x = np.linspace(x_min,x_max, num_points)
        y = np.sin(x)
        fig, ax = plt.subplots()
        ax.plot(x, y, label = "Синус")
        ax.grid()
        ax.legend(loc = 'upper right')
        ax.axhline(y=0, color='k', linewidth = 0.6)
        ax.axvline(x=0, color='k', linewidth = 0.6)
        st.pyplot(fig)
        with st.expander("Код"):
            """
        ```python 
        x_min = st.sidebar.slider('Минимальное значение x', 
                min_value=-20.0, max_value=0.0, value=-10.0)
        x_max = st.sidebar.slider('Максимальное значение x', 
                min_value=0.0, max_value=20.0, value=10.0)
        num_points = st.sidebar.slider('Количество точек', 
                min_value=10, max_value=1000, value=50)
        x = np.linspace(x_min,x_max, num_points)
        y = np.sin(x)
        fig, ax = plt.subplots()
        ax.plot(x, y, label = "Синус")
        ax.grid()
        ax.legend(loc = 'upper right')
        ax.axhline(y=0, color='k', linewidth = 0.6)
        ax.axvline(x=0, color='k', linewidth = 0.6)
        st.pyplot(fig)
        ```
            """
        
        
    elif (option == 'Гауссиан'):
        x_slider = st.sidebar.slider('значение x', min_value=-10.0, max_value=10.0, value=5.0)
        A = st.sidebar.slider('значение A', min_value=-10.0, max_value=10.0, value=1.0)
        x0 = st.sidebar.slider('значение x0', min_value=-5.0, max_value=5.0, value=0.0)
        num_points = st.sidebar.slider('Количество точек', min_value=10, max_value=1000, value=50)
        sigma = st.sidebar.slider('значение sigma', min_value=0.0, max_value=10.0, value=1.0)
        x = np.linspace(-x_slider, x_slider, num_points)
        y = A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
        
        fig, ax = plt.subplots()
        ax.plot(x, y, label = "Гауссиан")
        ax.grid()
        ax.legend(loc = 'upper right')
        ax.axhline(y=0, color='k', linewidth = 0.6)
        ax.axvline(x=0, color='k', linewidth = 0.6)
        st.pyplot(fig)
        with st.expander("Код"):
            """
        ```python 
        x_slider = st.sidebar.slider('значение x', min_value=-10.0, 
                max_value=10.0, value=5.0)
        A = st.sidebar.slider('значение A', min_value=-10.0, 
                max_value=10.0, value=1.0)
        x0 = st.sidebar.slider('значение x0', min_value=-5.0, 
                max_value=5.0, value=0.0)
        num_points = st.sidebar.slider('Количество точек', 
                min_value=10, max_value=1000, value=50)
        sigma = st.sidebar.slider('значение sigma', 
                min_value=0.0, max_value=10.0, value=1.0)
        x = np.linspace(-x_slider, x_slider, num_points)
        y = A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
        
        fig, ax = plt.subplots()
        ax.plot(x, y, label = "Гауссиан")
        ax.grid()
        ax.legend(loc = 'upper right')
        ax.axhline(y=0, color='k', linewidth = 0.6)
        ax.axvline(x=0, color='k', linewidth = 0.6)
        st.pyplot(fig)
        ```
            """
    elif (option == 'Степенная функция'):
        x_min = st.sidebar.slider('Минимальное значение x', min_value=-30.0, max_value=0.0, value=-5.0)
        x_max = st.sidebar.slider('Максимальное значение x', min_value=0.0, max_value=30.0, value=5.0)
        a = st.sidebar.slider('значение a', min_value=-10.0, max_value=30.0, value=1.0)
        num_points = st.sidebar.slider('Количество точек', min_value=10, max_value=1000, value=50)
        x = np.linspace(x_min,x_max, num_points)
        y = x ** a
        
        fig, ax = plt.subplots()
        ax.plot(x, y, label = "Степенная функция")
        ax.grid()
        #ax.set_ylim(x_min, x_max)
        #ax.set_xlim(x_min, x_max)
        ax.legend(loc = 'upper right')
        ax.axhline(y=0, color='k', linewidth = 0.6)
        ax.axvline(x=0, color='k', linewidth = 0.6)
        st.pyplot(fig)
        with st.expander("Код"):
            """
        ```python 
        x_min = st.sidebar.slider('Минимальное значение x', 
                min_value=-30.0, max_value=0.0, value=-5.0)
        x_max = st.sidebar.slider('Максимальное значение x', 
                min_value=0.0, max_value=30.0, value=5.0)
        a = st.sidebar.slider('значение a', min_value=-10.0, 
                max_value=30.0, value=1.0)
        num_points = st.sidebar.slider('Количество точек', 
                min_value=10, max_value=1000, value=50)
        x = np.linspace(x_min,x_max, num_points)
        y = x ** a
        
        fig, ax = plt.subplots()
        ax.plot(x, y, label = "Степенная функция")
        ax.grid()
        #ax.set_ylim(x_min, x_max)
        #ax.set_xlim(x_min, x_max)
        ax.legend(loc = 'upper right')
        ax.axhline(y=0, color='k', linewidth = 0.6)
        ax.axvline(x=0, color='k', linewidth = 0.6)
        st.pyplot(fig)
        ```
            """
    
elif (add_radio == "Размещение графиков в кадре"):
    option = st.selectbox(
        '',
        ('Использование pyplot', 'Использование subplots', 'Способы размещения нескольких графиков'))
    if (option == 'Использование pyplot'):
        """
        ## Использование pyplot
        """
        x = np.linspace(-10,10, 100)
        y_sin = np.sin(x)
        plt.plot(x, y_sin, label = 'sin')
        plt.tight_layout()
        plt.title("Синус")
        plt.grid()
        plt.legend(loc = 'upper right')
        plt.axhline(y=0, color='k', linewidth = 0.6)
        plt.axvline(x=0, color='k', linewidth = 0.6)
        plt.ylim(-1, 1)
        st.pyplot(plt)
        with st.expander("Код"):
            """
        ```python 
        import matplotlib.pyplot as plt
        x = np.linspace(-10,10, 100)
        y_sin = np.sin(x)
        plt.plot(x, y_sin, label = 'sin')
        plt.tight_layout()
        plt.title("Синус")
        plt.grid()
        plt.legend(loc = 'upper right')
        plt.axhline(y=0, color='k', linewidth = 0.6)
        plt.axvline(x=0, color='k', linewidth = 0.6)
        plt.ylim(-1, 1)
        st.pyplot(plt)
        ```
            """
    elif (option == 'Использование subplots'):
        """
        ## Метод subplots
        """  
        st.write("Более подробная информация про метод [subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html).")
        x = np.linspace(-10,10, 100)
        y_sin = np.sin(x)
        y_cos = np.cos(x)
        y_sc = np.cos(x)/3 + np.sin(x)/3
        y_cs = np.cos(x)/2 - np.sin(x)/2 - 1
        fig, axs = plt.subplots(2, 2)
        axs[0][0].plot(x, y_sin , label = 'y_sin')
        axs[0][1].plot(x, y_sc, label = 'y_cs')
        axs[1][0].plot(x, y_sc, label = 'y_sc')
        axs[1][1].plot(x, y_cos, label = 'y_cos')
        
        names = ['График sin', 'График cs', 'График sc', 'График cos']
        fig.tight_layout()
        for idx, ax in enumerate(axs.ravel()):
            
            ax.set_title(names[idx])
            ax.grid()
            ax.legend(loc = 'upper right')
            ax.axhline(y=0, color='k', linewidth = 0.6)
            ax.axvline(x=0, color='k', linewidth = 0.6)
            ax.set_ylim(-1, 1)
        st.pyplot(fig)
        with st.expander("Код"):
            """
        ```python 
        x = np.linspace(-10,10, 100)
        y_sin = np.sin(x)
        y_cos = np.cos(x)
        y_sc = np.cos(x)/3 + np.sin(x)/3
        y_cs = np.cos(x)/2 - np.sin(x)/2 - 1
        fig, axs = plt.subplots(2, 2)
        axs[0][0].plot(x, y_sin , label = 'y_sin')
        axs[0][1].plot(x, y_sc, label = 'y_cs')
        axs[1][0].plot(x, y_sc, label = 'y_sc')
        axs[1][1].plot(x, y_cos, label = 'y_cos')
        
        names = ['График sin', 'График cs', 'График sc', 'График cos']
        fig.tight_layout()
        for idx, ax in enumerate(axs.ravel()):
            ax.set_title(names[idx])
            ax.grid()
            ax.legend(loc = 'upper right')
            ax.axhline(y=0, color='k', linewidth = 0.6)
            ax.axvline(x=0, color='k', linewidth = 0.6)
            ax.set_ylim(-1, 1)
        st.pyplot(fig)
        ```
            """
    elif (option == 'Способы размещения нескольких графиков'):
        """
        ## Метод fig.add_subplot
        """ 
        x = np.linspace(-10,10, 100)
        y_sin = np.sin(x)
        y_cos = np.cos(x)
        y_sc = np.cos(x)/3 + np.sin(x)/3
        y_cs = np.cos(x)/2 - np.sin(x)/2 - 1
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(3, 3, (1, 5))
        ax2 = fig1.add_subplot(3, 3, 9)
        ax3 = fig1.add_subplot(3, 3, (7, 8))
        ax4 = fig1.add_subplot(3, 3, (3, 6))
        fig1.tight_layout()
        ax1.plot(x, y_sin , label = 'y_sin')
        ax2.plot(x, y_sc, label = 'y_cs')
        ax3.plot(x, y_sc, label = 'y_sc')
        ax4.plot(x, y_cos, label = 'y_cos')
        st.pyplot(fig1)
        
        with st.expander("Код"):
            """
        ```python 
        x = np.linspace(-10,10, 100)
        y_sin = np.sin(x)
        y_cos = np.cos(x)
        y_sc = np.cos(x)/3 + np.sin(x)/3
        y_cs = np.cos(x)/2 - np.sin(x)/2 - 1
        
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(3, 3, (1, 5))
        ax2 = fig1.add_subplot(3, 3, 9)
        ax3 = fig1.add_subplot(3, 3, (7, 8))
        ax4 = fig1.add_subplot(3, 3, (3, 6))
        
        fig1.tight_layout()
        ax1.plot(x, y_sin , label = 'y_sin')
        ax2.plot(x, y_sc, label = 'y_cs')
        ax3.plot(x, y_sc, label = 'y_sc')
        ax4.plot(x, y_cos, label = 'y_cos')
        st.pyplot(fig1)
        ```
            """
        """
        ## Метод plt.subplot2grid
        """ 
        fig2 = plt.figure()
        ax1 = plt.subplot2grid((3, 3), (0, 0))
        ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
        ax3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)
        ax4 = plt.subplot2grid((3, 3), (1, 1), colspan=2, rowspan=2)
        fig2.tight_layout()
        ax1.plot(x, y_sin , label = 'y_sin')
        ax2.plot(x, y_sc, label = 'y_cs')
        ax3.plot(x, y_sc, label = 'y_sc')
        ax4.plot(x, y_cos, label = 'y_cos')
        st.pyplot(fig2)
 
        with st.expander("Код"):
            """
        ```python 
        x = np.linspace(-10,10, 100)
        y_sin = np.sin(x)
        y_cos = np.cos(x)
        y_sc = np.cos(x)/3 + np.sin(x)/3
        y_cs = np.cos(x)/2 - np.sin(x)/2 - 1
        
        fig2 = plt.figure()
        ax1 = plt.subplot2grid((3, 3), (0, 0))
        ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
        ax3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)
        ax4 = plt.subplot2grid((3, 3), (1, 1), colspan=2, rowspan=2)
        
        fig2.tight_layout()
        ax1.plot(x, y_sin , label = 'y_sin')
        ax2.plot(x, y_sc, label = 'y_cs')
        ax3.plot(x, y_sc, label = 'y_sc')
        ax4.plot(x, y_cos, label = 'y_cos')
        st.pyplot(fig2)
        ```
            """
