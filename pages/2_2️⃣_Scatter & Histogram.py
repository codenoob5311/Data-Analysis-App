import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px



st.header("Make Graphics 💪")

file = st.file_uploader("Uploader File : ",type=['csv'])

if file :
    df = pd.read_csv(file)
    tab1, tab2 = st.tabs(["Scatter Plot", "Histogram"])
    with tab1:
            # Make Tab For Scatter Plot
            NumCol = df.select_dtypes(np.number).columns.to_list()
            NumCol = NumCol[1:]
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                x = st.selectbox("Axis x : ", NumCol)
            with col2:
                y = st.selectbox("Axis y : ", NumCol, index=1)
            with col3:
                color = st.selectbox("color : ", df.columns.to_list(), index=2)
            with col4:
                Hover = st.selectbox("Hover : ", df.columns.to_list())
            plot = px.scatter(df, x=x, y=y, color=color, hover_data=Hover)
            show = st.plotly_chart(plot)

    with tab2:
            x = st.selectbox("Axis : ", df.columns.to_list(), index=1)
            plot = px.histogram(df, x=x)
            show = st.plotly_chart(plot)
