import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from analytics_bymonth_ui import analytics_by_month_tab

st.title("Expense Tracking System")


tab1, tab2, tab3 = st.tabs(["Add/Update","Analytics","Analytics By Month"]) # as st.tabs return tuple

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_by_month_tab()


