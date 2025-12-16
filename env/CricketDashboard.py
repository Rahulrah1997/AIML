import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import time
import json

matches = []

st.sidebar.title("Criket Dashboard")
#st.sidebar.header("Select a page to view details")
Pageselection =st.sidebar.selectbox("Select Match",['Live Matches','Player Stats','SQL Analytics','CRUD Operations'])

#@st.fragment(run_every=5)
def livematches():

    # url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    # headers = {
	# "x-rapidapi-key": "a5528101fdmshd5d19c93da4909ep189b28jsnc2030d0871ae",
    # "x-rapidapi-key": "e19f088f4emsh5939c6cc237aa1fp175797jsne25dc4cf301b",
	# "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    #             }
    # response = requests.get(url, headers=headers)
    # data = response.json()

    with open ('matchesdata.json','r',encoding='utf-8') as file:
     data = json.load(file)

    

    for type_match in data.get("typeMatches",[]):
        for series_match in type_match.get("seriesMatches",[]):
            series_data = series_match.get("seriesAdWrapper",{})
            series_id = series_data.get("seriesId")
            series_name = series_data.get("seriesName")

            for match in series_data.get("matches",[]):
                info = match.get("matchInfo",{})
                match_id = info.get("matchId")
                description = info.get("matchDesc")
                match_format = info.get("matchFormat")
                start_date = info.get("startDate")
                match_status = info.get("status")
                state = info.get("state")
                team1_name = info.get("team1",{}).get("teamName")
                team1_sname = info.get("team1",{}).get("teamSName")
                team2_name = info.get("team2",{}).get("teamName")
                team2_sname = info.get("team2",{}).get("teamSName")
                Ground_name = info.get("venueInfo",{}).get("ground")
                city = info.get("venueInfo",{}).get("city")
                matchScore = match.get('matchScore',{})
                team1score = matchScore.get('team1Score',{}).get('inngs1',{}).get('runs')
                team1wicket = matchScore.get('team1Score',{}).get('inngs1',{}).get('wickets')
                team1overs = matchScore.get('team1Score',{}).get('inngs1',{}).get('overs')
                team2score = matchScore.get('team2Score',{}).get('inngs1',{}).get('runs')
                team2wicket = matchScore.get('team2Score',{}).get('inngs1',{}).get('wickets')
                team2overs = matchScore.get('team2Score',{}).get('inngs1',{}).get('overs')

                matches.append({
                    'series_id': series_id,
                    'series_name': series_name,
                    'match_id': match_id,
                    'description': description,
                    'match_format': match_format,
                    'start_date': start_date,
                    'match_status': match_status,
                    'team1_name': team1_name,
                    'team1_sname': team1_sname,
                    'team2_name': team2_name,
                    'team2_sname': team2_sname,
                    'Ground_name': Ground_name,
                    'city': city,
                    'state':state,
                    'team1score':team1score,
                    'team1wicket':team1wicket,
                    'team1overs':team1overs,
                    'team2score':team2score,
                    'team2wicket':team2wicket,
                    'team2overs':team2overs
            }

            )
                
    return(matches)

#st.write(matches)

if Pageselection == 'Live Matches':

    livematches()
    st.title("Live Match Dashboard",width='stretch')
    selected_match = st.selectbox('Select a Match',options=matches,
                 format_func=lambda m: f"{m['series_name']} ({m['team1_sname']} vs {m['team2_sname']})")
    
    if selected_match:
        formatter = lambda n:f"Match Details: ({n['team1_name']} vs {n['team2_name']})"
        subheader_text = formatter(selected_match)
        st.subheader(subheader_text)

        description = selected_match['description']
        Match_Format = selected_match['match_format']
        Venue = selected_match['Ground_name']
        City = selected_match['city']
        Status = selected_match['match_status']
        State = selected_match['state']
        Team1_Score = selected_match['team1score']
        Team2_Score = selected_match['team2score']

        c1,c2 = st.columns(2)


        with c1:
            st.markdown(f"Match: {description}")
            st.markdown(f"Format: {Match_Format}")
            st.markdown(f"Venue: {Venue}")
            st.markdown(Team1_Score)

        with c2:
            st.markdown(f"City: {City}")
            st.markdown(f"Status: {Status}")
            st.markdown(f"State: {State}")
            st.markdown(Team2_Score)



   
