import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import time
import json
from LiveDashbord import Live_Dashbord 

de = Live_Dashbord()
st.sidebar.title("Criket Dashboard")
#st.sidebar.header("Select a page to view details")
Pageselection =st.sidebar.selectbox("Select Match",['Live Matches','Player Stats','SQL Analytics','CRUD Operations'])

#st.write(matches)

if Pageselection == 'Live Matches':

    de.live_matches()
    
    





   
