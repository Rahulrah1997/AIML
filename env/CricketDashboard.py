import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import time
import json
from Data import DataExtraction 

Matches = []
de = DataExtraction()
Matches = de.livematches()
st.sidebar.title("Criket Dashboard")
#st.sidebar.header("Select a page to view details")
Pageselection =st.sidebar.selectbox("Select Match",['Live Matches','Player Stats','SQL Analytics','CRUD Operations'])

#st.write(matches)

if Pageselection == 'Live Matches':

    #de.livematches()
    
    st.title("Live Match Dashboard 🏏",width='stretch')
    selected_match = st.selectbox('Select a Match',options=Matches,
                 format_func=lambda m: f"{m['series_name']} ({m['team1_sname']} vs {m['team2_sname']})")
    
    if selected_match['state'] == 'Complete':
        st.balloons()
       
    if selected_match:
        formatter = lambda n:f"Match Details: ({n['team1_name']} vs {n['team2_name']})"
        subheader_text = formatter(selected_match)
        st.subheader(subheader_text)
        st.info(f"***{selected_match['series_name']}***")

        MatchDetails = {'Description':selected_match['description'],
                        'Match_Format':selected_match['match_format'],
                        'Venue':selected_match['Ground_name'],
                        'City':selected_match['city'],
                        'Status':selected_match['match_status'],
                        'State':selected_match['state']}
        
        
        Team1details_inn1 = {'Score':selected_match['team1score_inn1'],'Overs':selected_match['team1overs_inn1'],
                       'wicket':selected_match['team1wicket_inn1'],'TeamName':selected_match['team1_name']}
        
        if selected_match['team1score_inn2']:
            Team1details_inn2 = {'Score':selected_match['team1score_inn2'],'Overs':selected_match['team1overs_inn2'],
                        'wicket':selected_match['team1wicket_inn2'],'TeamName':selected_match['team1_name']}
        
        Team2details_inn1 = {'Score':selected_match['team2score_inn1'],'overs':selected_match['team2overs_inn1'],
                       'wicket':selected_match['team2wicket_inn1'],'TeamName':selected_match['team2_name']}
        
        if selected_match['team2score_inn2']:
            Team2details_inn2 = {'Score':selected_match['team2score_inn2'],'overs':selected_match['team2overs_inn2'],
                            'wicket':selected_match['team2wicket_inn2'],'TeamName':selected_match['team2_name']}
       
        st.markdown(f"*{MatchDetails['Description']}* | {MatchDetails['Match_Format']}")
        st.markdown(f"*{MatchDetails['Venue']}* | {MatchDetails['City']}")
        st.markdown(f"*{MatchDetails['Status']}* | {MatchDetails['State']}")

        st.markdown("---")

        c1,c2 = st.columns(2)
        

        with c1:
            st.markdown(f"**{Team1details_inn1['TeamName']}**")
            st.metric(label="Score", value=Team1details_inn1['Score'])
            c1_inner1, c1_inner2 = st.columns(2)
            c1_inner1.metric("Overs", Team1details_inn1['Overs'])
            c1_inner2.metric("Wickets", Team1details_inn1['wicket'])
            st.markdown("---")


        with c2:
            st.markdown(f"**{Team2details_inn1['TeamName']}**")
            st.metric(label="Score", value=Team2details_inn1['Score'])
            c2_inner1, c2_inner2 = st.columns(2)
            c2_inner1.metric("Overs", Team2details_inn1['overs'])
            c2_inner2.metric("Wickets", Team2details_inn1['wicket'])
            st.markdown("---")





   
