import streamlit as st
import pandas as pd
# import plotly.express as px
import plotly.express as px

# Load the data
# LITE FILE: https://drive.google.com/file/d/1BoezQAGeKSAo-61Bu2PPP3i_JaDamNhr/view?usp=drive_link
# Direct Drive Link:https://drive.google.com/uc?id=1BoezQAGeKSAo-61Bu2PPP3i_JaDamNhr

# Full Fat File: https://drive.google.com/file/d/1BoezQAGeKSAo-61Bu2PPP3i_JaDamNhr/view?usp=drive_link

# df =pd.read_csv("https://drive.google.com/uc?id=1BoezQAGeKSAo-61Bu2PPP3i_JaDamNhr",encoding="latin1") #"cp1252"
df =pd.read_csv("https://drive.google.com/uc?id=1BoezQAGeKSAo-61Bu2PPP3i_JaDamNhr",encoding="latin1", usecols=["StartDateTime", "Sailor", "Job", "Family", "Series"]) #"cp1252"

# Write the page heading and subtitle
st.title("KSC Safety Roster 2026")
st.write("Safety roster for the year 2026")

# Add the controls
st.header("Filters")
##sailors = ["All Sailors"] + sorted(df["Sailor"].unique())
sailors = ["All Sailors"] + sorted(df["Sailor"].dropna().astype(str).unique())
Selected_sailor = st.selectbox("Select Sailor", sailors)

##Family
Families = ["All Families"] + sorted(df["Family"].dropna().astype(str).unique())
Selected_family = st.selectbox("Select family", Families)


# Apply the filter
if Selected_family != "All Families":
    df = df[df["Family"] == Selected_family]
if Selected_sailor != "All Sailors":
    df = df[df["Sailor"] == Selected_sailor]

filtered_df = df.sort_values("Sailor",ascending=True)

# Display table
if filtered_df.empty:
    st.write("No data available for the selected filters.")
else:
    st.dataframe(filtered_df, width="stretch", hide_index=True)
    
# Display chart
st.subheader("Sailor Assignments")
sailor_df = df.groupby(["Sailor"], as_index=False)["StartDateTime"].count()

fig1 = px.bar(sailor_df, x="StartDateTime", y="Sailor", color="Sailor", title="Sailor Assignments")
fig1.update_yaxes(categoryorder="total ascending")

num_datapoints = len(sailor_df) 
pixel_per_bar = 25  # Space allowed for each row
dynamic_height = max(400, num_datapoints * pixel_per_bar)

fig1.update_layout(height=dynamic_height)

#fig2 = px.bar(sailor_df, x="Sailor", y="StartDateTime", color="Sailor", title="Sailor Assignments")
#fig2.update_xaxes(categoryorder="total descending")



st.plotly_chart(fig1, width="stretch") 
#st.plotly_chart(fig2, width="stretch") 

