import requests
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from LiveDashbord import Live_Dashbord 
from PlayerStats import Player_Stats
from Analytics import analy

LD = Live_Dashbord()
ps = Player_Stats()
ay = analy()
st.sidebar.title("Criket Dashboard")
#st.sidebar.header("Select a page to view details")
Pageselection =st.sidebar.selectbox("Select Match",['Live Matches','Player Stats','SQL Analytics','CRUD Operations'])

#st.write(matches)

# if Pageselection == 'Live Matches':

#     LD.live_matches()

# if Pageselection == 'Player Stats':

#      ps.Player_Search()

if Pageselection == 'Player Stats':

    ay.sss()
    
    





   
