import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header("Simplift Data ➿")

file = st.file_uploader("Choose File ' csv ' : ", type=["csv"])


@st.cache_data
def LoadFile(file):
    return pd.read_csv(file)


if file:
    df = LoadFile(file)
    # Show How Many Rows See
    NumRows = st.slider(
        "How Many Rows To Show : ", max_value=len(df), min_value=4, step=1
    )
    # Show How Many Columns See
    Cols = st.multiselect(
        "All Columns : ", df.columns.to_list(), default=df.columns.to_list()
    )
    st.write(df[:NumRows][Cols])
    col1, col2 = st.columns(2)
    NumCol = df.select_dtypes(np.number).columns.to_list()
    with col1:
        su1 = st.selectbox("Sum : ", NumCol)
        suu1 = df[su1].sum()
        st.write(suu1)
    with col2:
        me2 = st.selectbox("Mean : ", NumCol)
        mea2 = df[me2].mean()
        st.write(mea2)
    col3, col4 = st.columns(2)
    with col3:
        mi = st.selectbox("Min : ", NumCol)
        min = df[mi].min()
        st.write(min)
    with col4:
        ma = st.selectbox("Max : ", NumCol)
        max = df[ma].max()
        st.write(max)
    AllCol = df.select_dtypes(include='object').columns.to_list()
    count = st.selectbox("Count : ",AllCol)
    cnt = df[count].value_counts()
    n_rows = st.slider("Number Of Rows : ",max_value=len(cnt),min_value=4,step=1)
    st.write(cnt[:n_rows])
