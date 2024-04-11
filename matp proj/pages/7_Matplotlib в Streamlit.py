import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time
import math
from datetime import time
import plotly.express as px
import datetime

st.title("Matplotlib в Streamlit")
st.divider()

data = {"a": [23, 12, 78, 4, 54], "b": [0, 13, 88, 1, 3],
        "c": [45, 2, 546, 67, 56]}

# df = pd.DataFrame(data)

t1 = ''' #### Прежде чем углубляться в основную тему, хочется отметить, что у Streamlit есть несколько "родных" типов диаграмм, то есть таких, которые можно использовать без сторонних библиотек'''

code1 = '''
    data = {"a":[23, 12, 78, 4, 54],
            "b":[0, 13 ,88, 1, 3],
            "c":[45, 2, 546, 67, 56]}
    st.line_chart(data)
         '''
st.markdown(t1)

st.markdown("### 1. Линейная диаграмма")
with st.expander("Посмотреть код"):
    st.code(code1, language='python')
st.line_chart(data)

code2 = '''
    data = {"a":[23, 12, 78, 4, 54],
            "b":[0, 13 ,88, 1, 3],
            "c":[45, 2, 546, 67, 56]}
    st.bar_chart(data)
        '''

code3 = '''
    data = {"a":[23, 12, 78, 4, 54],
            "b":[0, 13 ,88, 1, 3],
            "c":[45, 2, 546, 67, 56]}
    st.area_chart(data)
 '''
st.markdown("### 2. Столбчатая диаграмма")
with st.expander("Посмотреть код"):
    st.code(code2, language='python')
st.bar_chart(data)

st.markdown("### 3. Диаграмма с областями")
with st.expander("Посмотреть код"):
    st.code(code3, language='python')
st.area_chart(data)

st.divider()

code4 = '''
     arr = np.random.normal(1, 1, size=100)
     fig, ax = plt.subplots()
     ax.hist(arr, bins=20)
        '''

arr = np.random.normal(1, 1, size=500)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

t7 = '''#### Но так же Streamlit поддерживает подключение и использование библиотеки \"Matplotlib\", что значительно расширяет возможнсти визуализации данных'''
st.markdown(t7)

# st.markdown("**Отображение рисунка matplotlib.pyplot**")
# st.code(code4, language='python')
# st.pyplot(fig)

st.markdown("#### 1. Возможность отображения графиков функций:")
with st.expander("Посмотреть код"):
    code5 = '''        
        x = np.linspace(0, 10, 100)
        fig = plt.figure()
        plt.title("Графики")
        plt.plot(x, np.sin(x), 'r-', label="sin(x)")
        plt.plot(x, np.cos(x), 'b-', label="cos(x)")
        plt.plot(x, np.tan(x), 'g-', label="tan(x)")
        plt.axis([0,6,-10,10])
        plt.legend()
        plt.grid(True)
        st.write(fig)
            '''
    st.code(code5, language='python')

x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.title("Графики")
plt.plot(x, np.sin(x), 'r-', label="sin(x)")
plt.plot(x, np.cos(x), 'b-', label="cos(x)")
plt.plot(x, np.tan(x), 'g-', label="tan(x)")
plt.axis([0, 6, -10, 10])
plt.legend()
plt.grid(True)
st.write(fig)
st.divider()
###############################################

st.markdown("#### 2. Возможность отображения диаграмм:")
with st.expander("Посмотреть код"):
    code6 = '''
        import numpy as np
        import matplotlib.pyplot as plt
        
        arr = np.random.normal(1, 1, size=10000)
        fig, ax = plt.subplots()
        ax.hist(arr, bins=50)
        ax.set_title("Распределение Гаусса")
        ax.set_xlabel("Значения")
        ax.set_ylabel("Количество исходов, шт.")
        ax.grid(True)
        st.write(fig)
           '''
    st.code(code6, language='python')

arr = np.random.normal(1, 1, size=10000)
fig, ax = plt.subplots()
ax.hist(arr, bins=50)
ax.set_title("Распределение Гаусса")
ax.set_xlabel("Значения")
ax.set_ylabel("Количество исходов, шт.")
ax.grid(True)
st.write(fig)
st.divider()




#
# st.markdown("**Отображение диаграммы рассеяния**")
# st.code(code5, language='python')
# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# st.scatter_chart(chart_data)


