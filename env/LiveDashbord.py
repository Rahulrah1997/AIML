import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import time
import json
from collections import defaultdict 


class Live_Dashbord():
      
    
    def Get_Match_Details(self):
        matches = []
        
        
        url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

        headers = {
        "x-rapidapi-key": "a5528101fdmshd5d19c93da4909ep189b28jsnc2030d0871ae",
        "x-rapidapi-key": "e19f088f4emsh5939c6cc237aa1fp175797jsne25dc4cf301b",
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
                    }
        response = requests.get(url, headers=headers)
        data = response.json()

        # with open ('matchesdata.json','r',encoding='utf-8') as file:
        #     data = json.load(file)

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
        return matches
    

    def live_matches(self):   
        matches = self.Get_Match_Details()
        st.title("Live Match Dashboard 🏏",width='stretch')
        selected_match = st.selectbox('Select a Match',options=matches,
                    format_func=lambda m: f"{m['series_name']} ({m['team1_sname']} vs {m['team2_sname']})")
        
        if selected_match['state'] == 'Complete':
            st.balloons()
        
        url = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{selected_match['match_id']}/scard"

        headers = {
            "x-rapidapi-key": "e19f088f4emsh5939c6cc237aa1fp175797jsne25dc4cf301b",
            "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
        }
        
        response = requests.get(url, headers=headers)
        
        score = response.json()
        
        structured_data_by_innings = defaultdict(lambda: {"batsman_data": [], "bowler_data": [], "extras": {}, "fow": []})

        for scorecard in score.get('scorecard', []):
            innings_id = scorecard.get('inningsid')
            if innings_id is None:
                continue
          
            fow_data = scorecard.get('fow', {}).get('fow', [])
            for batsman in scorecard.get('batsman', []):
                batsman_id = batsman.get('id')
             
                overs_at_dismissal = None
                if isinstance(fow_data, list):
                    for fow in fow_data:
                        if isinstance(fow, dict) and fow.get('batsmanid') == batsman_id:
                            overs_at_dismissal = fow.get('overnbr')
                            break

                batsman_record = {
                    'batsman_name': batsman.get('name'),
                    'batsman_runs': batsman.get('runs'),
                    'batsman_balls': batsman.get('balls'),
                    'batsman_fours': batsman.get('fours'),
                    'batsman_sixes': batsman.get('sixes'),
                    'batsman_strikerate': batsman.get('strkrate'),
                    'batsman_is_captain': batsman.get('iscaptain'),
                    'batsman_out_description': batsman.get('outdec'),
                    'overs_at_dismissal': overs_at_dismissal
                }
                structured_data_by_innings[innings_id]["batsman_data"].append(batsman_record)
            
            bowler_list_raw = scorecard.get("bowler", [])
            if isinstance(bowler_list_raw, dict):
                bowler_list = bowler_list_raw.get("bowler", [])
            else:
                bowler_list = bowler_list_raw

            for bowler in bowler_list:
                bowler_record = {
                    'bowler_name': bowler.get('name'),
                    'bowler_overs': bowler.get('overs'),
                    'bowler_maidens': bowler.get('maidens'),
                    'bowler_wickets': bowler.get('wickets'),
                    'bowler_runs': bowler.get('runs'),
                    'bowler_economy': bowler.get('economy'),
                    'bowler_is_captain': bowler.get('iscaptain'),
                }
                structured_data_by_innings[innings_id]["bowler_data"].append(bowler_record)

            structured_data_by_innings[innings_id]["fow"] = fow_data
            structured_data_by_innings[innings_id]["extras"] = scorecard.get('extras', {})

            Innings_data = structured_data_by_innings

            innings_1= Innings_data[1]  
            innings_2= Innings_data[2] 
            innings_3= Innings_data[3] 
            innings_4= Innings_data[4] 
        
        
        
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
            
            Team2details_inn1 = {'Score':selected_match['team2score_inn1'],'Overs':selected_match['team2overs_inn1'],
                        'wicket':selected_match['team2wicket_inn1'],'TeamName':selected_match['team2_name']}
            
            if selected_match['team2score_inn2']:
                Team2details_inn2 = {'Score':selected_match['team2score_inn2'],'Overs':selected_match['team2overs_inn2'],
                                'wicket':selected_match['team2wicket_inn2'],'TeamName':selected_match['team2_name']}
        
            st.markdown(f"*{MatchDetails['Description']}* | {MatchDetails['Match_Format']}")
            st.markdown(f"*{MatchDetails['Venue']}🏟️* | {MatchDetails['City']}")
            st.markdown(f"*{MatchDetails['Status']}* | {MatchDetails['State']}")

            st.markdown("---")

            c1,c2 = st.columns(2)
            inn_details1 = False
            inn_details2 = False
            inn_details3 = False
            inn_details4 = False

            with c1:
                if selected_match['team1score_inn1']:
                    st.markdown(f"**{Team1details_inn1['TeamName']}|Innings1**")
                    st.metric(label="Score", value=Team1details_inn1['Score'])
                    c1_inner1, c1_inner2 = st.columns(2)
                    c1_inner1.metric("Overs", Team1details_inn1['Overs'])
                    c1_inner2.metric("Wickets", Team1details_inn1['wicket'])
                    st.markdown("---")
                

            

                if selected_match['team1score_inn2']:
                    st.markdown(f"**{Team1details_inn2['TeamName']}|Innings2**")
                    st.metric(label="Score", value=Team1details_inn2['Score'])
                    c1_inner1, c1_inner2 = st.columns(2)
                    c1_inner1.metric("Overs", Team1details_inn2['Overs'])
                    c1_inner2.metric("Wickets", Team1details_inn2['wicket'])
                    st.markdown("---")

                if selected_match['team1score_inn1']:                  
                    inn_details1= st.button(f"**{Team1details_inn1['TeamName']}|Innings1Scorecard**")
                
                if selected_match['team1score_inn2']:
                    inn_details3 = st.button(f"**{Team1details_inn2['TeamName']}|Innings2ScoreCard**")
                    


                

            if inn_details1:
                st.markdown("Batting Details:")
                st.dataframe(pd.DataFrame(innings_1['batsman_data']),hide_index=True)
                st.markdown("Bowling Details:")
                st.dataframe(pd.DataFrame(innings_1['bowler_data']),hide_index=True)
                st.markdown("Extras:")
                st.dataframe(pd.DataFrame([innings_1['extras']]),hide_index=True)
                

            
            if inn_details3:
                st.markdown("Batting Details:")
                st.dataframe(pd.DataFrame(innings_3['batsman_data']),hide_index=True)
                st.markdown("Bowling Details:")
                st.dataframe(pd.DataFrame(innings_3['bowler_data']),hide_index=True)
                st.markdown("Extras:")
                st.dataframe(pd.DataFrame([innings_3['extras']]),hide_index=True)
                
            with c2:
                if selected_match['team2score_inn1']:
                    st.markdown(f"**{Team2details_inn1['TeamName']}|Innings1**")
                    st.metric(label="Score", value=Team2details_inn1['Score'])
                    c2_inner1, c2_inner2 = st.columns(2)
                    c2_inner1.metric("Overs", Team2details_inn1['Overs'])
                    c2_inner2.metric("Wickets", Team2details_inn1['wicket'])
                    st.markdown("---")               
                

                if selected_match['team2score_inn2']:
                    st.markdown(f"**{Team2details_inn2['TeamName']}|Innings2**")
                    st.metric(label="Score", value=Team2details_inn2['Score'])
                    c1_inner1, c1_inner2 = st.columns(2)
                    c1_inner1.metric("Overs", Team2details_inn2['Overs'])
                    c1_inner2.metric("Wickets", Team2details_inn2['wicket'])
                    st.markdown("---")

                if selected_match['team2score_inn2']:                  
                    inn_details2 = st.button(f"**{Team2details_inn1['TeamName']}|Innings1ScoreCard**")
                if selected_match['team2score_inn2']:
                    inn_details4 = st.button(f"**{Team2details_inn2['TeamName']}|Innings2ScoreCard**")

                
            if inn_details2:
                st.markdown("Batting Details:")
                st.dataframe(pd.DataFrame(innings_2['batsman_data']),hide_index=True)
                st.markdown("Bowling Details:")
                st.dataframe(pd.DataFrame(innings_2['bowler_data']),hide_index=True)
                st.markdown("Extras:")
                st.dataframe(pd.DataFrame([innings_2['extras']]),hide_index=True)

            if inn_details4:
                st.markdown("Batting Details:")
                st.dataframe(pd.DataFrame(innings_4['batsman_data']),hide_index=True)
                st.markdown("Bowling Details:")
                st.dataframe(pd.DataFrame(innings_4['bowler_data']),hide_index=True)
                st.markdown("Extras:")
                st.dataframe(pd.DataFrame([innings_4['extras']]),hide_index=True)
                    
        
