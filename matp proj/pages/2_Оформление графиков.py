import streamlit as st
import matplotlib.pyplot as plt

def plot_title_graph():
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
    # plt.title("Название графика")
    # plt.show()
    fig = plt.figure()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
    plt.title("Название графика")
    st.write(fig)

def plot_xlabel_ylabel_graph():
    fig = plt.figure()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
    plt.xlabel("Это ось Х")
    plt.ylabel("А это ось Y")
    st.write(fig)

def plot_xlim_ylim_graph(x_down, x_up, y_down, y_up):
    fig = plt.figure()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
    plt.xlim()
    plt.ylim(y_down, y_up)
    st.write(fig)

def plot_axis_graph(x_down, x_up, y_down, y_up):
    fig = plt.figure()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
    plt.axis([x_down, x_up, y_down, y_up])
    st.write(fig)


def plot_grid_graph(boolean_meaning):
    fig = plt.figure()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
    plt.grid(boolean_meaning)
    st.write(fig)


def plot_legend_graph():
    fig = plt.figure()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-', label = "Легенда")
    plt.legend()
    st.write(fig)


def main():
    with st.sidebar:
        add_radio = st.radio(
            "Разделы",
            ("Теория",
             "Пример")
        )

    if add_radio == "Теория":
        st.title("Оформление графиков")
        st.divider()

        text1 = """#### В данном разделе будет рассказано об основных встренных в Matplotlib функциях, позволяющих добавлять и изменять элементы графика:"""
        st.markdown(text1)
        st.divider()


        st.markdown("### 1. plt.title()")
        st.markdown("> #### Функция позволяет задать название графика")
        code = """
            fig = plt.figure()
            plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
            plt.title("Название графика")
            st.write(fig)
               """
        with st.expander("Посмотреть пример"):
            st.code(code, language='python')
            plot_title_graph()
        st.divider()


        st.markdown("### 2. plt.xlabel() и plt.ylabel()")
        st.markdown("> #### Функции позволяют задать названия осей графика")
        code = """
            fig = plt.figure()
            plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
            plt.xlabel("Это ось Х")
            plt.ylabel("А это ось Y")
            st.write(fig)
               """
        with st.expander("Посмотреть пример"):
            st.code(code, language='python')
            plot_xlabel_ylabel_graph()
        st.divider()


        st.markdown("### 3. plt.xlim() и plt.ylim()")
        st.markdown("> #### Функции позволяют задать границы осей графика")
        code = """
            fig = plt.figure()
            plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
            plt.xlim(0, 5)
            plt.ylim(0, 18)
            st.write(fig)
               """
        with st.expander("Посмотреть пример 1"):
            st.code(code, language='python')
            plot_xlim_ylim_graph(0, 5, 0, 18)

        code = """
            fig = plt.figure()
            plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
            plt.xlim(1, 4)
            plt.ylim(1, 16)
            st.write(fig)
               """
        with st.expander("Посмотреть пример 2"):
            st.code(code, language='python')
            plot_xlim_ylim_graph(1, 4, 1, 16)
        st.divider()


        st.markdown("### 3*. plt.axis()")
        st.markdown("> #### Функция, как и две предыдущие, позволяет задать границы осей графика, но делает это с помощью СПИСКА входных паарметров")
        code = """
                    fig = plt.figure()
                    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
                    plt.axis([0, 5, 0, 18])
                    st.write(fig)
                       """
        with st.expander("Посмотреть пример 1"):
            st.code(code, language='python')
            plot_axis_graph(0, 5, 0, 18)

        code = """
                    fig = plt.figure()
                    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
                    plt.axis([1, 4, 1, 16])
                    st.write(fig)
               """
        with st.expander("Посмотреть пример 2"):
            st.code(code, language='python')
            plot_axis_graph(1, 4, 1, 16)
        st.divider()


        st.markdown("### 4. plt.grid()")
        st.markdown("> #### Функция позволяет отобразить или убрать сетку на графике")
        code = """
                    fig = plt.figure()
                    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
                    plt.grid(True)
                    st.write(fig)
                """
        with st.expander("Посмотреть пример 1"):
            st.code(code, language='python')
            plot_grid_graph(True)

        code = """
                    fig = plt.figure()
                    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
                    plt.grid(False)
                    st.write(fig)
                """
        with st.expander("Посмотреть пример 2"):
            st.code(code, language='python')
            plot_grid_graph(False)
        st.divider()


        st.markdown("### 5. plt.legend()")
        st.markdown("> #### Функция позволяет отобразить легенды на графике")
        st.markdown("> ##### Сама же легенда указывается как именованный аргумент ф-ции plt.plot(**label =\"Легенда\"**)")
        st.markdown("> ##### Либо есть возможность указать названия легенд как список входных данных для функции plt.legend([\"Легенда1\", \"Легенда2\"])")
        code = """
            fig = plt.figure()
            plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-', label = "Легенда")
            plt.legend()
            st.write(fig)
               """
        with st.expander("Посмотреть пример 1"):
            st.code(code, language='python')
            plot_legend_graph()

        code = """
            fig = plt.figure()
            plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
            plt.legend(["Легенда"])
            st.write(fig)
               """
        with st.expander("Посмотреть пример 2"):
            st.code(code, language='python')
            plot_legend_graph()

        st.markdown("> #### Важно отметить именованный аргумент функции plt.legend(loc = \"значение\"). Он позволяет указывать положение легенды на графике")
        st.write("Подробности: https://www.geeksforgeeks.org/change-the-legend-position-in-matplotlib/")

        code = """
            fig = plt.figure()
            plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
            plt.legend(["Легенда"], loc=4)
            st.write(fig)
               """
        with st.expander("Посмотреть пример 2"):
            st.code(code, language='python')
            fig = plt.figure()
            plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
            plt.legend(["Легенда"], loc=4)
            st.write(fig)



    elif add_radio == "Пример":
        st.title("Оформление графиков")
        st.divider()

        text1 = """#### Теперь объединим весь функционал и отобразим график со всеми изученными элементами: """
        st.markdown(text1)
        st.divider()

        fig = plt.figure()
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-', label="Легенда")
        plt.title("График зависимости Y(X)")
        plt.xlabel("это ось")
        plt.ylabel("и это ось")
        plt.axis([0, 8, 0, 20])
        plt.legend(loc = 0)
        plt.grid(False)
        st.write(fig)

        code = """
                    fig = plt.figure()
                    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-', label = "Легенда")
                    plt.title("График зависимости Y(X)")
                    plt.xlabel("это ось")
                    plt.ylabel("и это ось")
                    plt.axis([0, 8, 0, 20])
                    plt.legend(loc = 0)
                    plt.grid(False)
                    st.write(fig)
                """
        with st.expander("Посмотреть код"):
            st.code(code, language='python')


if __name__ == '__main__':
    main()




