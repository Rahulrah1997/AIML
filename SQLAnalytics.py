import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import pymysql

class SQL_Analytics:
    def __init__(self):
        
        self.mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="rahul"
    )

        self.mycursor = self.mydb.cursor()
    def q1(self):
        self.mycursor.execute("use cricketdata;")
        sqlquery = "select name AS Name,battingstyle AS BatStyle,bowlingstyle AS BowlStyle,playerrole AS PlayerRole from playerinfo;"
        self.mycursor.execute(sqlquery)
        sdat = self.mycursor.fetchall()
        columns = [desc[0] for desc in self.mycursor.description]
        sqldata = pd.DataFrame(sdat,columns=columns)
        return sqldata
    
    def q2(self):
        self.mycursor.execute("use cricketdata;")
        sqlquery = """select matchtype AS MatchType,series_name AS SeriesName,match_description AS Description,
                    match_format AS Format,Start_date AS StartDate,End_date AS EndDate,
                    match_status AS Status,Team1_name AS Team1Name,Team2_name AS Team2Name,
                    match_state AS State,ground_name AS Ground ,city AS City  from matchdetails order  by Start_date desc"""
        self.mycursor.execute(sqlquery)
        sdat = self.mycursor.fetchall()
        columns = [desc[0] for desc in self.mycursor.description]
        sqldata = pd.DataFrame(sdat,columns=columns)
        return sqldata
