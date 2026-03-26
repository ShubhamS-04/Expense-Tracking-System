import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def analytics_by_month_tab():
    if st.button("Get Monthly Analytics"):
        response = requests.get(f"{API_URL}/monthly_analytics")
        response = response.json()

        df = pd.DataFrame(response)

        st.bar_chart(df.set_index("month_name")["total"])

        df["month"] = df["month"].map("{:.2f}".format)
        df["total"] = df["total"].map("{:.2f}".format)


        st.table(df)


