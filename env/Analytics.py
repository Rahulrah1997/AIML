import streamlit as st
import pandas as pd
from SQLAnalytics import SQL_Analytics

class DataAnalytics():
   

    def data_display(self):
        sa = SQL_Analytics()
        qn = {'q1':'All Players who repesent India','q2':'All cricket matches that were played in the last Few days'}

        selectalue = st.selectbox("select",qn.values())
       
        if selectalue == qn['q1']:
            st.dataframe(sa.q1(),hide_index=True)

        if selectalue == qn['q2']:
            st.dataframe(sa.q2(),hide_index=True)
            

