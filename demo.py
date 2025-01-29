#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:58:15 2025

@author: vineshree
"""

import streamlit as st
import pandas as pd
#import textwrap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any

# Title of the app
st.image('./logo.png', width=200 )
st.title("Dark Energy Model Integration in CLASS (for DUMMIES)")
st.write("University of Cape Town")
# Collect basic information
# name = "Vineshree Pillay"
# field = "PhD in Applied Mathematics"
# institution = "University of Cape Town"

#subheader for document
st.subheader("CLASS housekeeping")
st.write("Troubleshooting CLASS installations can be a pain if done incorrectly on the first go. It's best to following the recommended guidelines. There are many links that take you to many different pages, but I suggest using the following link:")

# Display basic profile information
#st.header("Researcher Overview")
#st.write(f"**Name:** {name}")
#st.write(f"**Field of Research:** {field}")
#st.write(f"**Institution:** {institution}")



# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Need further help?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

#Adding code
st.code('for i in range(8): foo()')


# Add a section for publications
# st.header("Publications")
# uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

# if uploaded_file:
#     publications = pd.read_csv(uploaded_file)
#     st.dataframe(publications)

#     # Add filtering for year or keyword
#     keyword = st.text_input("Filter by keyword", "")
#     if keyword:
#         filtered = publications[
#             publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
#         ]
#         st.write(f"Filtered Results for '{keyword}':")
#         st.dataframe(filtered)
#     else:
#         st.write("Showing all publications")

# # Add a section for visualizing publication trends
# st.header("Publication Trends")
# if uploaded_file:
#     if "Year" in publications.columns:
#         year_counts = publications["Year"].value_counts().sort_index()
#         st.bar_chart(year_counts)
#     else:
#         st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "vineshree.pillay013@gmail.com"
#st.write(f"You can reach {name} at {email}.")

#Add subheader
#st.subheader("Qualifications")

#Adding a sidebar
#st.sidebar.("Resources")

#Add links to Linkedin 
st.download_button("Resume", "CV.pdf", 
                   file_name="CV.pdf", mime=None, key=None, 
                   help=None, on_click=None, args=None, kwargs=None, 
                   type="secondary", icon=None, disabled=False, use_container_width=False)

# #Custom theme
# def custom_theme() -> dict[str, Any]:
#     return {
#         "config": {
#             "axis": {
#                 "grid": False,
#                 "labelColor": "#7F7F7F",
#                 "labelFontSize": 14,
#                 "tickColor": "#7F7F7F",
#                 "titleColor": "#7F7F7F",
#                 "titleFontSize": 16,
#                 "titleFontWeight": "normal",
#             },
#             "legend": {
#                 "labelColor": "#7F7F7F",
#                 "labelFontSize": 14,
#             },
#             "view": {
#                 "height": 320,
#                 "width": 480,
#                 "stroke": False,
#             },
#         },
#     }
