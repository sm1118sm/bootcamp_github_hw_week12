import streamlit as st
import pandas as pd
import plotly.express as px

jobkorea_df = pd.read_csv("C:/Users/sm111/Desktop/bootcamp_github_hw_week12/data_tmp/data_jobkorea.csv")
saramin_df = pd.read_csv("C:/Users/sm111/Desktop/bootcamp_github_hw_week12/data_tmp/data_saramin.csv")

df = pd.concat([jobkorea_df, saramin_df], ignore_index=True)

st.title("Title")

if st.button("Recruit Searching"):

    st.dataframe(df, use_container_width=True)

    count_df = df["Site"].value_counts(ascending=True).reset_index()
    count_df.columns = ["Site", "Count"]
    count_df["Ratio"] = round(count_df["Count"] / count_df["Count"].sum() * 100, 2)

    st.dataframe(count_df, use_container_width=False)

    fig = px.pie(
        count_df,
        names="Site",
        values="Count",
        title="Recruitment Ratio"
    )

    st.plotly_chart(fig, use_container_width=True)