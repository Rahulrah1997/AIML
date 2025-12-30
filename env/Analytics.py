import streamlit as st
import pandas as pd
from SQLAnalytics import SQL_Analytics

class analy():
   

    def sss(self):
        sa = SQL_Analytics()
        qn = {'q1':'qqqq','q2':'fsdfsd'}

        selectalue = st.selectbox("select",qn.values())
       
        if selectalue == qn['q1']:
            st.dataframe(sa.q1(),hide_index=True)
            

