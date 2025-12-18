import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import time
import json

matches = []
class DataExtraction():
    
#@st.fragment(run_every=5)
    
    def livematches(self):
        
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
                    team1score_inn1 = matchScore.get('team1Score',{}).get('inngs1',{}).get('runs')
                    team1wicket_inn1 = matchScore.get('team1Score',{}).get('inngs1',{}).get('wickets')
                    team1overs_inn1 = matchScore.get('team1Score',{}).get('inngs1',{}).get('overs')
                    team2score_inn1 = matchScore.get('team2Score',{}).get('inngs1',{}).get('runs')
                    team2wicket_inn1 = matchScore.get('team2Score',{}).get('inngs1',{}).get('wickets')
                    team2overs_inn1 = matchScore.get('team2Score',{}).get('inngs1',{}).get('overs')
                    team1score_inn2 = matchScore.get('team1Score',{}).get('inngs2',{}).get('runs')
                    team1wicket_inn2 = matchScore.get('team1Score',{}).get('inngs2',{}).get('wickets')
                    team1overs_inn2 = matchScore.get('team1Score',{}).get('inngs2',{}).get('overs')
                    team2score_inn2 = matchScore.get('team2Score',{}).get('inngs2',{}).get('runs')
                    team2wicket_inn2 = matchScore.get('team2Score',{}).get('inngs2',{}).get('wickets')
                    team2overs_inn2 = matchScore.get('team2Score',{}).get('inngs2',{}).get('overs')

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
                        'team1score_inn1':team1score_inn1,
                        'team1wicket_inn1':team1wicket_inn1,
                        'team1overs_inn1':team1overs_inn1,
                        'team2score_inn1':team2score_inn1,
                        'team2wicket_inn1':team2wicket_inn1,
                        'team2overs_inn1':team2overs_inn1,
                        'team1score_inn2':team1score_inn2,
                        'team1wicket_inn2':team1wicket_inn2,
                        'team1overs_inn2':team1overs_inn2,
                        'team2score_inn2':team2score_inn2,
                        'team2wicket_inn2':team2wicket_inn2,
                        'team2overs_inn2':team2overs_inn2
                }

                )
                    
        return(matches)
                    
        
