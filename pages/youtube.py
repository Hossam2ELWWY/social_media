import pandas  as pd 
import streamlit as st 
import plotly.express as px 
social_media = pd.read_csv(r"dummy_data.csv")
yout = social_media[social_media['platform'] == 'YouTube']
st.title('YouTube')
st.image(r'https://www.billboard.com/wp-content/uploads/2022/10/youtube-logo-2022-billboard-espagnol-1548.jpg?w=942&h=623&crop=1')
col1 ,col2 , col3 = st.columns(3)
card1 = col1.container(border= 1)
card2 = col2.container(border=1 )
card3 = col3.container(border=1)
card1.metric(label="Max_Time_spent" , value= "9 hours" )
card3.metric(label='Min_Time_spent' , value= "1 hour")
card2.metric(label="Avg_Time_spent" , value="4.5 hours")
st.subheader("Data Table")
st.write(yout.head(5).style.applymap(lambda x: 'color: white'))
selection = st.selectbox("select column you want see visulaztion" ,  ['age' , "gender" ,"interests" , 'demographics' , 'income' ,'isHomeOwner','Owns_Car'])
st.plotly_chart(px.histogram(yout, x= selection , template='plotly_dark' , color=selection , color_discrete_sequence=px.colors.sequential.Electric_r ))
st.subheader("Data Table")
st.write(yout)

# Data description
st.subheader("Data Description")
st.write(yout.describe())

# Filter data based on user input
filter_value = st.selectbox("Filter data by profession:" , yout["profession"].unique())
filtered_data = yout[yout['profession'].str.contains(filter_value, case=False)]
st.write(filtered_data)

chose = st.selectbox("select one colums " ,yout.select_dtypes(include="number").columns)
chose2  = st.selectbox('select one colums' , yout.select_dtypes(exclude="number").columns)
st.plotly_chart(px.bar(yout , x = chose2 , y = chose ,color=chose2 ,color_discrete_sequence=px.colors.sequential.Electric_r))

