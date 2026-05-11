import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn

st.set_page_config(page_title = "viz Demo")

with open('models/df.pkl','rb') as file:
    df = pickle.load(file)

with open('models/pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)


st.header('Enter your input')

property_type = st.selectbox('Property Type', ['flat','house'])

sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

bedroom = float(st.selectbox('No of Bedroom',sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('No. of Bathrooms',sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('No. Of balconies',sorted(df['balcony'].unique().tolist()))

agePossession = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = st.number_input('Built Up Area')

servant_room = float(st.selectbox('Servant Room',[0.0,1.0]))

store_room = float(st.selectbox('Store Room',[0.0,1.0]))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))

luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))

floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    data = [[property_type,	sector,	bedroom, bathroom, balcony,	agePossession, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)


    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price-0.22
    high = base_price+0.22
    st.text('The price of the flat is between {} Cr and {} Cr'.format(round(low,2),round(high,2)))

