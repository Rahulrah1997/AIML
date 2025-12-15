import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

matches = []

st.sidebar.title("Criket Dashboard")
#st.sidebar.header("Select a page to view details")
Pageselection =st.sidebar.selectbox("Select Match",['Live Matches','Player Stats','SQL Analytics','CRUD Operations'])

def livematches():

    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    headers = {
	"x-rapidapi-key": "a5528101fdmshd5d19c93da4909ep189b28jsnc2030d0871ae",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
                }
    response = requests.get(url, headers=headers)
    data = response.json()

    

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
                team1_name = info.get("team1",{}).get("teamName")
                team1_sname = info.get("team1",{}).get("teamSName")
                team2_name = info.get("team2",{}).get("teamName")
                team2_sname = info.get("team2",{}).get("teamSName")
                Ground_name = info.get("venueInfo",{}).get("ground")

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
                    'team1_sname': team1_sname,
                    'Ground_name': Ground_name
            }

            )
                
    return(matches)

#st.write(matches)

if Pageselection == 'Live Matches':

    livematches()
    options = [m['series_name']for m in matches]
    st.title('Live Match Dashboard',width='stretch')
    st.selectbox('Select a Match',options)


   