import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

#df = pd.read_csv("D:\AIML\Project1\customers-100.csv")
#st.write(df)
#st.dataframe(df)
#st.table(df)

# jsondata = { "name"   : "John Smith",
#   "sku"    : "20223",
#   "price"  : 23.95,
#   "shipTo" : { "name" : "Jane Smith",
#                "address" : "123 Maple Street",
#                "city" : "Pretendville",
#                "state" : "NY",
#                "zip"   : "12345" },
#   "billTo" : { "name" : "John Smith",
#                "address" : "123 Maple Street",
#                "city" : "Pretendville",
#                "state" : "NY",
#                "zip"   : "12345" }
# }

# st.json(jsondata,expanded=False)

# st.metric("New Stock", value=897,delta="10.2")  
# st.metric("New Stock", value=897,delta="10.2",delta_color="inverse")
# st.metric("New Stock", value=897,delta="10.2",delta_arrow="down",delta_color="off")

# st.title("Plot")

# data = pd.DataFrame(
#     np.random.randn(50,3),
#     columns=['A','B','C']
# )
# st.write(data)
# st.line_chart(data)
#st.line_chart(data,y=['A','B'])
#st.area_chart(data, y=['A','B'])
#st.bar_chart(data)

# fig,ax = plt.subplots()
# ax.scatter(data['A'],data['C'])

# st.pyplot(fig)

# charts = alt.Chart(data).mark_circle().encode(x='A',y='B')
# st.altair_chart(charts,use_container_width=True)

# st.graphviz_chart("""
# digraph{
# watch -> like
# like -> share
# share -> create
# create -> watch                                                                
#                   }
                  
# """
# )

# data = pd.DataFrame({
#     'lat': [13.0337, 13.0036, 13.04, 13.04, 13.0616, 13.0825, 13.0532, 13.0008, 12.9745, 13.0],
#     'lon': [80.2699, 80.2293, 80.17, 80.17, 80.2453, 80.2078, 80.2246, 80.2596, 80.2209, 80.14]

# })

# st.map(data)

#st.image("C:/Users/rajam/Downloads/download.jpeg")

# st.image("data:image/png;base64,iV=")
#st.video("https://www.youtube.com/watch?v=52A6kTKXDzA&list=RD52A6kTKXDzA&start_radio=1")

#st.video("C:/Users/rajam/Downloads/02fa2131-1576-4393-a622-3b0ec9a9230f-1.mp4")
#st.audio()

# name = st.text_input("Enter your Name: ")
# address = st.text_area('address')

# if st.button("Click"):
#     st.write(name)
#     st.write(address)

# date = st.date_input('Date')
# st.time_input('Time')

# if st.checkbox('terms and conditions'):
#     st.write('thank you')

# r = st.radio('colours',['R','Y','B','G'],horizontal=True)
# st.write(r)

# sb = st.selectbox('colours',['R','Y','B','G'])
# sb = st.multiselect('colours',['R','Y','B','G'])

# st.slider('age',min_value=10,max_value=70,step=2)

# nu = st.number_input("salary",min_value=15000.0,max_value=40000.0,step=600.0)
# st.write(nu)

# fl = st.file_uploader('UPLOAD')
# if fl:
#     st.image(fl)

# # a = st.camera_input('Take a Pic')

# # if a:
# #     st.image(a)

# clr = st.color_picker("pick a colour:")
# if clr:
#     st.write(clr)

# data = {
#     'num':[x for x in range(1,13)],
#     'square':[x**2 for x in range(1,13)],
#     'twice':[x*2 for x in range(1,13)],
#     'thrice':[x*3 for x in range(1,13)]
# }

# df = pd.DataFrame(data)

# col = st.sidebar.selectbox("Select number",df.columns)

# fig,ax = plt.subplots()
# ax.plot(df['num'],df[col])

# ax.set_title(f'plot of {col} vs num')
# ax.set_xlabel('num')
# ax.set_ylabel(col)

# st.pyplot(fig)

# st.balloons()
# st.success('Success')
# st.error('Error')
# st.warning('Warining')
# st.exception('Exception')

st.title("title")

col1, col2 = st.columns(2,gap="medium",vertical_alignment="top")
col1.image("C:/Users/rajam/Downloads/download.jpeg")
col2.image("C:/Users/rajam/Downloads/download.jpeg")

tab1, tab2  = st.tabs(['image','video'])
tab1.image("C:/Users/rajam/Downloads/download.jpeg")
tab2.video("https://www.youtube.com/watch?v=52A6kTKXDzA&list=RD52A6kTKXDzA&start_radio=1") 

