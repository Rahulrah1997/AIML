import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json



class Player_Stats():
    
    def Player_Search(self):
        player_data = []
        PlayerName = None
        st.title("Cricket Player Statics")
        st.subheader("🔍 Search for a Player")
        PlayerName= st.text_input("Enter the Player Name:")
        

        if PlayerName:
            
            url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/search"

            querystring = {"plrN":PlayerName}

            headers = {
                "x-rapidapi-key": "1c54fc90demshfb84a587356dcf2p19a711jsn8a4fe5302ba4",
                "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            pldata = response.json()

            if not pldata.get('player'):
                st.write("Enter the valid player name")


        # if PlayerName:
        #     with open("playerstats.json","r",encoding="utf-8") as file:
        #         pldata = json.load(file)

            else:    
                for player in pldata.get('player',[]):
                    player_id = player.get('id')
                    player_name = player.get('name')
                    player_tname = player.get('teamName')

                    if player_name and player_tname:
                        player_data.append({
                            'player_id' : player_id,
                            'player_name':player_name,
                            'player_tname':player_tname
                        })

                    

                st.write(f"You found {len(pldata['player'])} matches for your search")

                selected_player = st.selectbox("Select a Player:",options=player_data,
                                format_func=lambda p: f"{p['player_name']} ({p['player_tname']})")
                
                st.header(f"📊{selected_player['player_name']} Profile")

                url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{selected_player['player_id']}"

                headers = {
                    "x-rapidapi-key": "1c54fc90demshfb84a587356dcf2p19a711jsn8a4fe5302ba4",
                    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
                }

                response = requests.get(url, headers=headers)

                playerinfo = response.json()

                url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{selected_player['player_id']}/batting"

                headers = {
                    "x-rapidapi-key": "1c54fc90demshfb84a587356dcf2p19a711jsn8a4fe5302ba4",
                    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
                }

                response = requests.get(url, headers=headers)
                battingstats = response.json()

                url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{selected_player['player_id']}/bowling"

                headers = {
                    "x-rapidapi-key": "1c54fc90demshfb84a587356dcf2p19a711jsn8a4fe5302ba4",
                    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
                }

                response = requests.get(url, headers=headers)
                bowlingstats = response.json()

                # with open("playerinfo.json","r",encoding="utf-8") as file:
                #     playerinfo =  json.load(file)

                # with open("batstats.json","r",encoding="utf-8") as file:
                #     battingstats  = json.load(file)

                # with open("bowlstat.json","r",encoding="utf-8") as file:
                #     bowlingstats  = json.load(file)

                Player_id = playerinfo.get('id')
                Batting_Style = playerinfo.get('bat')
                Bowling_Style = playerinfo.get('bowl')
                Player_Name = playerinfo.get('name')
                Player_nickname = playerinfo.get('nickName')
                Player_Height = playerinfo.get('height')
                Player_Role = playerinfo.get('role')
                BirthPlace = playerinfo.get('birthPlace')
                Intlteam  = playerinfo.get('intlTeam')
                Teams = playerinfo.get('teams')
                DateofBirth = playerinfo.get('DoB')
                ranking = playerinfo.get('rankings',{})
                batting = ranking.get('bat',{})
                Testrank_Bat = batting.get('testBestRank')
                ODIrank_Bat = batting.get('odiBestRank')
                T20rank_Bat = batting.get('t20BestRank')
                bowling = ranking.get('bowl',{})
                Testrank_Bowl = bowling.get('testBestRank')
                ODIrank_Bowl = bowling.get('odiBestRank')
                T20rank_Bowl = bowling.get('t20BestRank')
                Allround = ranking.get('all',{})
                Testrank_Allround = Allround.get('testBestRank')
                ODIrank_Allround = Allround.get('odiBestRank')
                T20rank_Allround = Allround.get('t20BestRank')

                Rankings = [{'Format':['Test','ODI','T20'],
                            'BatRanking':[Testrank_Bat,ODIrank_Bat,T20rank_Bat],
                            'BowlRank':[Testrank_Bowl,ODIrank_Bowl,T20rank_Bowl],
                            'Allround':[Testrank_Allround,ODIrank_Allround,T20rank_Allround]}]
                

                t1,t2,t3,t4 = st.tabs(['👤Profile','🏏Batting Stats','🏀Bowling Stats',"📊ICC Ranking"])

                with t1:
                    st.header("🎯Personal Information")
                    c1,c2,c3 = st.columns(3)
                    
                    with c1:
                        st.subheader("Carrier Details")
                        st.write(f"Role: {Player_Role}")
                        st.write(f"Batting Style: {Batting_Style}")
                        st.write(f"Bowling Style: {Bowling_Style}")
                        st.write(f"International Team: {Intlteam}")

                    with c2:
                        st.subheader("Personal Details")
                        st.write(f"Name: {Player_Name}")
                        st.write(f"Nick Name: {Player_nickname}")
                        st.write(f"Place of Birth: {BirthPlace}")
                        st.write(f"Date of Birth: {DateofBirth}")
                        st.write(f"Height: {Player_Height}")

                    with c3:
                        st.subheader("Teams played")
                        teams = [t.strip() for t in Teams.split(",")]
                        st.markdown("\n".join(f"- {team}" for team in teams))

                with t2:

                    headers = battingstats['headers']
                    rows = [row['values'] for row in battingstats['values']]
                    batting_stats = pd.DataFrame(rows,columns=headers)
                    st.subheader("🏏 Batting Statistics")
                    st.dataframe(batting_stats,hide_index=True)

                with t3:

                    headers = bowlingstats['headers']
                    rows = [row['values'] for row in bowlingstats['values']]
                    bowling_stats = pd.DataFrame(rows,columns=headers)
                    st.subheader("🏀 Bowling Statistics")
                    st.dataframe(bowling_stats,hide_index=True)

                with t4:
                    headers = Rankings[0]['Format']
                    ranking = pd.DataFrame({
                        'Format': Rankings[0]['Format'],
                        'Batting': Rankings[0]['BatRanking'],
                        'Bowling': Rankings[0]['BowlRank'],
                        'AllRound': Rankings[0]['Allround']})
                    st.dataframe(ranking,hide_index=True)

                


