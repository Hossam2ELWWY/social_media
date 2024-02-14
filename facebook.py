import pandas as pd
import streamlit as st 
import plotly.express as px 
social_media = pd.read_csv(r"C:\Users\Maydoum\Downloads\Compressed\dummy_data.csv")
face = social_media[social_media['platform'] == 'Facebook']
st.title('Facebook')
st.image(r'https://cyrekdigital.com/static/5d5f92b08ea0b4b3ae29a30566ac35e0/23140/facebook-dla-marek-wszystko-o-marketingu-i-reklamie-na-fb.png' , caption="facebook" , use_column_width=True , width=100)
col1 ,col2 , col3 = st.columns(3)
card1 = col1.container(border= 1)
card2 = col2.container(border=1 )
card3 = col3.container(border=1)
card1.metric(label="Max_Time_spent" , value= "9 hours" )
card3.metric(label='Min_Time_spent' , value= "1 hour")
card2.metric(label="Avg_Time_spent" , value="5 hours")
st.subheader("Data Table")
st.write(face.head(5))

selection = st.selectbox("select column you want see visulaztion" ,  ['age' , "gender" ,"interests" , 'demographics' , 'income' ,'isHomeOwner','Owns_Car'])

st.plotly_chart(px.histogram(face , x= selection , template='plotly_dark' , color=selection , color_discrete_sequence=px.colors.sequential.Electric_r ))
# if selection == 'age' : 
#     st.plotly_chart(px.histogram(face , x= 'age' , template='plotly_dark'))
# elif selection == "gender"  :
#     st.plotly_chart(px.bar(face ,  x = 'gender' , template='plotly_dark'))
# elif selection == "interests"  :
#     st.plotly_chart(px.bar(face ,  x = 'interests' , template='plotly_dark'))
# elif selection == 'demographics'  :
#     st.plotly_chart(px.bar(face ,  x = 'demographics' , template='plotly_dark'))  
# elif selection == 'income'  :
#     st.plotly_chart(px.bar(face ,  x = 'income' , template='plotly_dark'))      
# elif selection == 'isHomeOwner'  :
#     st.plotly_chart(px.bar(face ,  x = 'isHomeOwner' , template='plotly_dark')) 
# elif selection == 'Owns_Car'  :
#     st.plotly_chart(px.bar(face ,  x = 'Owns_Car', template='plotly_dark')) 
# else:
#     st.write("No visualization available for this selection.")    

st.subheader("Data Table")
st.write(face)

# Data description
st.subheader("Data Description")
st.write(face.describe())

# Filter data based on user input
filter_value = st.selectbox("Filter data by profession:" , face["profession"].unique())
filtered_data = face[face['profession'].str.contains(filter_value, case=False)]
st.write(filtered_data)

chose = st.selectbox("select one colums " , face.select_dtypes(include="number").columns)
chose2  = st.selectbox('select one colums' , face.select_dtypes(exclude="number").columns)
st.plotly_chart(px.bar(face , x = chose2 , y = chose ,color=chose2 ,color_discrete_sequence=px.colors.sequential.Electric_r))










