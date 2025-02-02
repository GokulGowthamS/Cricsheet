import streamlit as st
import pandas as pd
import mysql.connector as db

connection = db.connect(
        user='root',
        password='Iamgokul@123',
        host='localhost',
        database='cricsheet'
    )

cursor = connection.cursor()

st.title("Cricsheet Query View")


sql_queries = [
    "SELECT DISTINCT(Batter) as Batsman, SUM(Total_runs) AS Runs FROM cricsheet.ipl_data_innings GROUP BY Batsman ORDER BY Runs DESC LIMIT 10;",
    "SELECT DISTINCT(Batter) as Batsman, SUM(Total_runs) AS Runs FROM cricsheet.odi_data_innings GROUP BY Batsman ORDER BY Runs DESC LIMIT 10;",
    "SELECT DISTINCT(Batter) as Batsman, SUM(Total_runs) AS Runs FROM cricsheet.t20_data_innings GROUP BY Batsman ORDER BY Runs DESC LIMIT 10;",
    "SELECT DISTINCT(Batter) as Batsman, SUM(Total_runs) AS Runs FROM cricsheet.test_data_innings GROUP BY Batsman ORDER BY Runs DESC LIMIT 10;",
    "SELECT Bowler, COUNT(Type) AS Wickets FROM cricsheet.ipl_data_innings WHERE Type IS NOT NULL GROUP BY Bowler ORDER BY Wickets DESC LIMIT 10;",
    "SELECT Bowler, COUNT(Type) AS Wickets FROM cricsheet.odi_data_innings WHERE Type IS NOT NULL GROUP BY Bowler ORDER BY Wickets DESC LIMIT 10;",
    "SELECT Bowler, COUNT(Type) AS Wickets FROM cricsheet.t20_data_innings WHERE Type IS NOT NULL GROUP BY Bowler ORDER BY Wickets DESC LIMIT 10;",
    "SELECT Bowler, COUNT(Type) AS Wickets FROM cricsheet.test_data_innings WHERE Type IS NOT NULL GROUP BY Bowler ORDER BY Wickets DESC LIMIT 10;",
    "SELECT DISTINCT(Match_Winner), SUM(CASE WHEN Win_By_Runs IS NOT NULL OR Win_By_Innings IS NOT NULL OR Win_By_Wickets IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*) AS Win_Rate FROM cricsheet.ipl_data WHERE Match_Winner IS NOT NULL GROUP BY Match_Winner ORDER BY Win_Rate DESC;",
    "SELECT DISTINCT(Match_Winner), SUM(CASE WHEN Win_By_Runs IS NOT NULL OR Win_By_Innings IS NOT NULL OR Win_By_Wickets IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*) AS Win_Rate FROM cricsheet.odi_data WHERE Match_Winner IS NOT NULL GROUP BY Match_Winner ORDER BY Win_Rate DESC;",
    "SELECT DISTINCT(Match_Winner), SUM(CASE WHEN Win_By_Runs IS NOT NULL OR Win_By_Innings IS NOT NULL OR Win_By_Wickets IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*) AS Win_Rate FROM cricsheet.t20_data WHERE Match_Winner IS NOT NULL GROUP BY Match_Winner ORDER BY Win_Rate DESC;"
    "SELECT DISTINCT(Match_Winner), SUM(CASE WHEN Win_By_Runs IS NOT NULL OR Win_By_Innings IS NOT NULL OR Win_By_Wickets IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*) AS Win_Rate FROM cricsheet.test_data WHERE Match_Winner IS NOT NULL GROUP BY Match_Winner ORDER BY Win_Rate DESC;",
    "SELECT Batter AS Batsman, COUNT(CASE WHEN Batter_runs = 100 THEN 1 ELSE 0 END) AS Number_Of_Centuries FROM cricsheet.ipl_data_innings GROUP BY Batsman ORDER BY Number_Of_Centuries DESC;",
    "SELECT Batter AS Batsman, COUNT(CASE WHEN Batter_runs = 100 THEN 1 ELSE 0 END) AS Number_Of_Centuries FROM cricsheet.odi_data_innings GROUP BY Batsman ORDER BY Number_Of_Centuries DESC;",
    "SELECT Batter AS Batsman, COUNT(CASE WHEN Batter_runs = 100 THEN 1 ELSE 0 END) AS Number_Of_Centuries FROM cricsheet.t20_data_innings GROUP BY Batsman ORDER BY Number_Of_Centuries DESC;",
    "SELECT Batter AS Batsman, COUNT(CASE WHEN Batter_runs = 100 THEN 1 ELSE 0 END) AS Number_Of_Centuries FROM cricsheet.test_data_innings GROUP BY Batsman ORDER BY Number_Of_Centuries DESC;",
    "SELECT Date, City, Venue, Season, Teams_Participated, Win_By_Runs, Match_Winner, Man_Of_Match FROM cricsheet.ipl_data WHERE Win_By_Runs IS NOT NULL ORDER BY Win_By_Runs LIMIT 10;",
    "SELECT Date, City, Venue, Season, Teams_Participated, Win_By_Runs, Match_Winner, Man_Of_Match FROM cricsheet.odi_data WHERE Win_By_Runs IS NOT NULL ORDER BY Win_By_Runs LIMIT 10;",
    "SELECT Date, City, Venue, Season, Teams_Participated, Win_By_Runs, Match_Winner, Man_Of_Match FROM cricsheet.t20_data WHERE Win_By_Runs IS NOT NULL ORDER BY Win_By_Runs LIMIT 10;",
    "SELECT Date, City, Venue, Season, Teams_Participated, Win_By_Runs, Match_Winner, Man_Of_Match FROM cricsheet.test_data WHERE Win_By_Runs IS NOT NULL ORDER BY Win_By_Runs LIMIT 10;"
]

query_title = ['Top 10 Batsman in IPL Match','Top 10 Batsman in ODI Match','Top 10 Batsman in T20 Match','Top 10 Batsman in TEST Match','Leading wicket-takers in IPL Match','Leading wicket-takers in ODI Match','Leading wicket-takers in T20 Match','Leading wicket-takers in TEST Match','Team with Highest Win Rate in IPL Match','Team with Highest Win Rate in ODI Match',
               'Team with Highest Win Rate in T20 Match','Team with Highest Win Rate in TEST Match','Total Number of Centuries in IPL Match','Total Number of Centuries in ODI Match','Total Number of Centuries in T20 Match','Total Number of Centuries in TEST Match','Narrowest Win Margins in IPL Match','Narrowest Win Margins in ODI Match','Narrowest Win Margins in T20 Match','Narrowest Win Margins in TEST Match']

select_query = st.selectbox("Select A Query", query_title)

if select_query == "Top 10 Batsman in ODI Match":
    cursor.execute(sql_queries[0])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[0], connection)
    st.dataframe(df)
elif select_query == "Top 10 Batsman in IPL Match":
    cursor.execute(sql_queries[1])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[1], connection)
    st.dataframe(df)
elif select_query == "Top 10 Batsman in T20 Match":
    cursor.execute(sql_queries[2])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[2], connection)
    st.dataframe(df)
elif select_query == "Top 10 Batsman in TEST Match":
    cursor.execute(sql_queries[3])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[3], connection)
    st.dataframe(df)
elif select_query == "Leading wicket-takers in IPL Match":
    cursor.execute(sql_queries[4])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[4], connection)
    st.dataframe(df)
elif select_query == "Leading wicket-takers in ODI Match":
    cursor.execute(sql_queries[5])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[5], connection)
    st.dataframe(df)
elif select_query == "Leading wicket-takers in T20 Match":
    cursor.execute(sql_queries[6])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[6], connection)
    st.dataframe(df)
elif select_query == "Leading wicket-takers in TEST Match":
    cursor.execute(sql_queries[7])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[7], connection)
    st.dataframe(df)
elif select_query == "Team with Highest Win Rate in IPL Match":
    cursor.execute(sql_queries[8])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[8], connection)
    st.dataframe(df)
elif select_query == "Team with Highest Win Rate in ODI Match":
    cursor.execute(sql_queries[9])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[9], connection)
    st.dataframe(df)
elif select_query == "Team with Highest Win Rate in T20 Match":
    cursor.execute(sql_queries[10])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[10], connection)
    st.dataframe(df)
elif select_query == "Team with Highest Win Rate in TEST Match":
    cursor.execute(sql_queries[11])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[11], connection)
    st.dataframe(df)
elif select_query == "Total Number of Centuries in IPL Match":
    cursor.execute(sql_queries[12])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[12], connection)
    st.dataframe(df)
elif select_query == "Total Number of Centuries in ODI Match":
    cursor.execute(sql_queries[13])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[13], connection)
    st.dataframe(df)
elif select_query == "Total Number of Centuries in T20 Match":
    cursor.execute(sql_queries[14])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[14], connection)
    st.dataframe(df)
elif select_query == "Total Number of Centuries in TEST Match":
    cursor.execute(sql_queries[15])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[15], connection)
    st.dataframe(df)
elif select_query == "Narrowest Win Margins in IPL Match":
    cursor.execute(sql_queries[16])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[16], connection)
    st.dataframe(df)
elif select_query == "Narrowest Win Margins in ODI Match":
    cursor.execute(sql_queries[17])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[17], connection)
    st.dataframe(df)
elif select_query == "Narrowest Win Margins in T20 Match":
    cursor.execute(sql_queries[18])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[18], connection)
    st.dataframe(df)
elif select_query == "Narrowest Win Margins in TEST Match":
    cursor.execute(sql_queries[19])
    data = cursor.fetchall()
    df = pd.read_sql(sql_queries[19], connection)
    st.dataframe(df)