import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('Streamilt Cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(1000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

def load_data_b():
    df = pd.DataFrame(
        np.random.rand(1000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

#Using cache
a0 = time()
st.subheader('Using st.cache')

st.write(load_data_a())
a1 = time()
st.info(a1 - a0)

b0 = time()
st.subheader('Not using st.cache')

st.write(load_data_b())
b1 = time()
st.info(b1-b0)

@st.cache
def fib(i):
    if i <= 0:
        return 0
    if i == 1:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)

c0 = time()
val = fib(29)
c1 = time()

st.info(c1-c0)
val

def fib2(i):
    if i <= 0:
        return 0
    if i == 1:
        return 1
    else:
        return fib2(i - 1) + fib2(i - 2)

d0 = time()
val2 = fib2(29)
d1 = time()

st.info(d1-d0)
val2