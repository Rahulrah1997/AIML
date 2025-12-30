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
        ssql = "select name,battingstyle,bowlingstyle,playerrole from playerinfo;"
        self.mycursor.execute(ssql)
        sdat = self.mycursor.fetchall()
        columns = [desc[0] for desc in self.mycursor.description]
        df = pd.DataFrame(sdat,columns=columns)
        return df
    