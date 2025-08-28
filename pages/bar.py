import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px


st.header("Make Graphics 💪")

file = st.file_uploader("Uploader File : ", type=["csv"])

if file:
    df = pd.read_csv(file)
    tab1, tab2 = st.tabs(["Bar", "Pie"])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            x = st.selectbox("Axis X : ", df.columns.to_list())

        with col2:
            y = st.selectbox("Axis Y : ", df.columns.to_list())
        plot = px.bar(df, x=x, y=y)
        show = st.plotly_chart(plot)
    with tab2:
        str_col = df.select_dtypes(include="object").columns.to_list()
        x = st.selectbox("Enter A Column : ", str_col)
        pie = df[x].value_counts()
        name_pie = pie.index
        value_pie = pie.values
        plot = px.pie(names=name_pie, values=value_pie)
        plot.update_traces(textinfo="label+percent")
        show = st.plotly_chart(plot)
