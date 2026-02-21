import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

jobkorea_df = pd.read_csv("data_jobkorea.csv")
saramin_df = pd.read_csv("data_saramin.csv")

df = pd.concat([jobkorea_df, saramin_df], ignore_index=True)

st.title("Title")

if st.button("Recruit Searching"):

    st.dataframe(df, use_container_width=True)

    count_df = df["Site"].value_counts().reset_index()
    count_df.columns = ["Site", "Count"]
    count_df["Ratio"] = round(count_df["Count"] / count_df["Count"].sum() * 100, 2)

    st.dataframe(count_df, use_container_width=False)

    st.subheader("Recruitment Ratio")

    fig, ax = plt.subplots(figsize=(6, 4))

    wedges, texts, autotexts = ax.pie(
        count_df["Ratio"],
        autopct="%.1f%%",
        startangle=222
    )

    ax.legend(
        wedges,
        count_df["Site"],
        loc="center left",
        bbox_to_anchor=(1.02, 0.5)
    )

    ax.axis("equal")
    st.pyplot(fig, use_container_width=False)