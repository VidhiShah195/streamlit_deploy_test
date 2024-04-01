# import streamlit as st
# import pandas as pd
# import altair as alt 
# import seaborn as sns
# import time
# st.title("Palmer's Penguins")
# st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

# penguin_file = st.file_uploader('Select Your Local Penguins CSV (default provided)')

# @st.cache_data
# def load_file(penguin_file):
#     time.sleep(5) 
#     if penguin_file is not None:
#         penguins_df = pd.read_csv(penguin_file)
#     else:
#         penguins_df = pd.read_csv('penguins.csv')
#     return(penguins_df)

# penguins_df = load_file(penguin_file)


# selected_x_var = st.selectbox('What do you want the x variable to be?',['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
# selected_y_var = st.selectbox('What about the y?',['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g'])
# selected_gender = st.selectbox('What gender do you want to filter for?',['all penguins', 'male penguins', 'female penguins'])


# # if selected_gender == 'male penguins':
# #     penguins_df = penguins_df[penguins_df['sex'] == 'male']
# # elif selected_gender == 'female penguins':
# #     penguins_df = penguins_df[penguins_df['sex'] == 'female']
# # else:
# #     pass
# alt_chart = (
#     alt.Chart(penguins_df, title="Scatterplot of Palmer's Penguins")
#     .mark_circle()
#     .encode(
#     x=selected_x_var,
#     y=selected_y_var,
#     color="species",
#     )
#     .interactive()
#     )
# st.altair_chart(alt_chart, use_container_width=True)

# LAYOUT COLUMNS
# import streamlit as st

# st.set_page_config(layout="wide")

# st.title('How to layout your Streamlit app')

# with st.expander('About this app'):
#   st.write('This app shows the various ways on how you can layout your Streamlit app.')
#   st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

# st.sidebar.header('Input')
# user_name = st.sidebar.text_input('What is your name?')
# user_emoji = st.sidebar.selectbox('Choose an emoji', ['','😄', '😆', '😊', '😍', '😴', '😕', '😱'])
# user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza']) 


# col1,col2,col3 = st.columns(3)

# with col1:
#     if user_name != '':
#         st.write(f'Hello {user_name}')
#     else:
#         set.write('Enter Your Name')

# with col2:
#     if user_emoji != '':
#         st.write(f"{user_emoji} is {user_name}'s favorite emoji")
#     else:
#         set.write('Choose an emoji')

# with col3:
#     if user_food != '':
#         st.write(f"{user_food} is {user_name}'s favorite food")
#     else:
#         set.write('Enter Your Favorite Food')

# LAYOUT TABS
import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['','😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza']) 


tab1,tab2,tab3 = st.tabs(["Name","Emoji","Food"])

with tab1:
    col1, col2, col3 = st.columns(2)
    with col1:
        if user_name != '':
            st.write(f'Hello {user_name}')
        else:
            set.write('Enter Your Name')
    with col2:
        st.write('This is my column 2')
    with col3:
        st.write('This is my column 2')
with tab2:
    if user_emoji != '':
        st.write(f"{user_emoji} is {user_name}'s favorite emoji")
    else:
        set.write('Choose an emoji')

with tab3:
    if user_food != '':
        st.write(f"{user_food} is {user_name}'s favorite food")
    else:
        set.write('Enter Your Favorite Food')