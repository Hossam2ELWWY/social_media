import pandas  as pd 
import streamlit as st 
import plotly.express as px 
social_media = pd.read_csv(r"dummy_data.csv")
insta = social_media[social_media['platform'] == 'Instagram']
st.title('Instagram')
st.image(r'https://c.files.bbci.co.uk/1CC9/production/_126096370_gettyimages-1239414252.jpg')
col1 ,col2 , col3 = st.columns(3)
card1 = col1.container(border= 1)
card2 = col2.container(border=1 )
card3 = col3.container(border=1)
card1.metric(label="Max_Time_spent" , value= "9 hours" )
card3.metric(label='Min_Time_spent' , value= "1 hour")
card2.metric(label="Avg_Time_spent" , value="5 hours")
st.subheader("Data Table")
st.write(insta.head(5).style.applymap(lambda x: 'color: white'))
selection = st.selectbox("select column you want see visulaztion" ,  ['age' , "gender" ,"interests" , 'demographics' , 'income' ,'isHomeOwner','Owns_Car'])
st.plotly_chart(px.histogram(insta , x= selection , template='plotly_dark' , color=selection , color_discrete_sequence=px.colors.sequential.Electric_r ))
st.subheader("Data Table")
st.write(insta)

# Data description
st.subheader("Data Description")
st.write(insta.describe())

# Filter data based on user input
filter_value = st.selectbox("Filter data by profession:" , insta["profession"].unique())
filtered_data = insta[insta['profession'].str.contains(filter_value, case=False)]
st.write(filtered_data)

chose = st.selectbox("select one colums " ,insta.select_dtypes(include="number").columns)
chose2  = st.selectbox('select one colums' , insta.select_dtypes(exclude="number").columns)
st.plotly_chart(px.bar(insta , x = chose2 , y = chose ,color=chose2 ,color_discrete_sequence=px.colors.sequential.Electric_r))

