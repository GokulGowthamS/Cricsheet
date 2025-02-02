import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df1_ipl = pd.read_csv("C:\\Users\\ADMIN\\Cricsheet\\PreProcessed_General_Datasets\\IPL_DATA.csv")
df2_ipl = pd.read_csv("C:\\Users\\ADMIN\\Cricsheet\\PreProcessed_Innings_Datasets\\IPL_DATA_INNINGS.csv")
df1_odi = pd.read_csv("C:\\Users\\ADMIN\\Cricsheet\\PreProcessed_General_Datasets\\ODI_DATA.csv")
df2_odi = pd.read_csv("C:\\Users\\ADMIN\\Cricsheet\\PreProcessed_Innings_Datasets\\ODI_DATA_INNINGS.csv")
df1_t20 = pd.read_csv("C:\\Users\\ADMIN\\Cricsheet\\PreProcessed_General_Datasets\\T20_DATA.csv")
df2_t20 = pd.read_csv("C:\\Users\\ADMIN\\Cricsheet\\PreProcessed_Innings_Datasets\\T20_DATA_INNINGS.csv")
df1_test = pd.read_csv("C:\\Users\\ADMIN\\Cricsheet\\PreProcessed_General_Datasets\\TEST_DATA.csv")
df2_test = pd.read_csv("C:\\Users\\ADMIN\\Cricsheet\\PreProcessed_Innings_Datasets\\TEST_DATA_INNINGS.csv")

st.title("Cricsheet Visualizations")

def ipl_info_1():

    st.subheader("Match Winners of IPL") 
    match_wins = df1_ipl["Match_Winner"].value_counts().reset_index()
    match_wins.columns = ["Match_Winner", "Match_Count"]    
    fig = px.bar(match_wins,x = "Match_Count", y = "Match_Winner", color = "Match_Winner", title = "Count of IPL Match Winners")
    fig.update_layout(xaxis_title = "Match Winners", yaxis_title = "Match Count", title_x = 0.3)
    st.plotly_chart(fig)

def ipl_info_2():    

    st.subheader("Toss Decisions of IPL")
    fig1 = px.histogram(df1_ipl, y = "Choose_To", color = "Choose_To", title = "Decision Count For IPL")
    fig1.update_layout(xaxis_title = "Decision", yaxis_title = "Total_Count", title_x = 0.3)
    st.plotly_chart(fig1)

def ipl_in_3():

    st.subheader("Total Batsman Score in IPL")
    batsman_score = df2_ipl.groupby("Batter")["Batter_runs"].sum().reset_index()
    fig2 = px.bar(batsman_score, x="Batter_runs", y="Batter", color="Batter", title="Total Runs Secured By Batsman in IPL")
    fig2.update_layout(xaxis_title = "Runs", yaxis_title = "Batsman", title_x = 0.3)
    st.plotly_chart(fig2)

def odi_info_4():

    st.subheader("Match Winners of ODI") 
    match_wins = df1_odi["Match_Winner"].value_counts().reset_index()
    match_wins.columns = ["Match_Winner", "Match_Count"]    
    fig3 = px.bar(match_wins,x = "Match_Count", y = "Match_Winner", color = "Match_Winner", title = "Count of ODI Match Winners")
    fig3.update_layout(xaxis_title = "Match Winners", yaxis_title = "Match Count", title_x = 0.3)
    st.plotly_chart(fig3)

def odi_info_5():    

    st.subheader("Toss Decisions of ODI")
    fig4 = px.histogram(df1_odi, y = "Choose_To", color = "Choose_To", title = "Decision Count For ODI")
    fig4.update_layout(xaxis_title = "Decision", yaxis_title = "Total_Count", title_x = 0.3)
    st.plotly_chart(fig4)

def odi_in_6():

    st.subheader("Total Batsman Score in ODI")
    batsman_score = df2_odi.groupby("Batter")["Batter_runs"].sum().reset_index()
    fig5 = px.bar(batsman_score, x="Batter_runs", y="Batter", color="Batter", title="Total Runs Secured By Batsman in ODI")
    fig5.update_layout(xaxis_title = "Runs", yaxis_title = "Batsman", title_x = 0.3)
    st.plotly_chart(fig5)

def t20_info_7():

    st.subheader("Match Winners of T20") 
    match_wins = df1_t20["Match_Winner"].value_counts().reset_index()
    match_wins.columns = ["Match_Winner", "Match_Count"]    
    fig6 = px.bar(match_wins,x = "Match_Count", y = "Match_Winner", color = "Match_Winner", title = "Count of T20 Match Winners")
    fig6.update_layout(xaxis_title = "Match Winners", yaxis_title = "Match Count", title_x = 0.3)
    st.plotly_chart(fig6)

def t20_info_8():    

    st.subheader("Toss Decisions of T20")
    fig7 = px.histogram(df1_t20, y = "Choose_To", color = "Choose_To", title = "Decision Count For T20")
    fig7.update_layout(xaxis_title = "Decision", yaxis_title = "Total_Count", title_x = 0.3)
    st.plotly_chart(fig7)

def t20_in_9():

    st.subheader("Total Batsman Score in ODI")
    batsman_score = df2_t20.groupby("Batter")["Batter_runs"].sum().reset_index()
    fig8 = px.bar(batsman_score, x="Batter_runs", y="Batter", color="Batter", title="Total Runs Secured By Batsman in T20")
    fig8.update_layout(xaxis_title = "Runs", yaxis_title = "Batsman", title_x = 0.3)
    st.plotly_chart(fig8)

def test_info_10():

    st.subheader("Match Winners of TEST") 
    match_wins = df1_t20["Match_Winner"].value_counts().reset_index()
    match_wins.columns = ["Match_Winner", "Match_Count"]    
    fig9 = px.bar(match_wins,x = "Match_Count", y = "Match_Winner", color = "Match_Winner", title = "Count of TEST Match Winners")
    fig9.update_layout(xaxis_title = "Match Winners", yaxis_title = "Match Count", title_x = 0.3)
    st.plotly_chart(fig9)

def test_info_11():    

    st.subheader("Toss Decisions of TEST")
    fig10 = px.histogram(df1_t20, y = "Choose_To", color = "Choose_To", title = "Decision Count For TEST")
    fig10.update_layout(xaxis_title = "Decision", yaxis_title = "Total_Count", title_x = 0.3)
    st.plotly_chart(fig10)

def test_in_12():

    st.subheader("Total Batsman Score in TEST")
    batsman_score = df2_t20.groupby("Batter")["Batter_runs"].sum().reset_index()
    fig11 = px.bar(batsman_score, x="Batter_runs", y="Batter", color="Batter", title="Total Runs Secured By Batsman in TEST")
    fig11.update_layout(xaxis_title = "Runs", yaxis_title = "Batsman", title_x = 0.3)
    st.plotly_chart(fig11)


ipl_info_1()
ipl_info_2()
ipl_in_3()
odi_info_4()
odi_info_5()
odi_in_6()
t20_info_7()
t20_info_8()
t20_in_9()
test_info_10()
test_info_11()
test_in_12()


