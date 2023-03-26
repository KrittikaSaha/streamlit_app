import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns


def get_data(parameter):
    x = np.random.normal(parameter+20, parameter/5, 10)
    y = np.random.normal(parameter-20, parameter/8, 10)
    df = pd.DataFrame(x, y).reset_index()
    df.columns = ["sales", "profit"]
    return df


st.title("Sales and profit for science")

parameter = st.slider("Arcane switch", 80, 120)
df = get_data(parameter)
graph =  sns.lmplot(data=df, x="sales", y="profit")

st.pyplot(graph)