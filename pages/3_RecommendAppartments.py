import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title = "Recommend Apartments")
location_df = pickle.load(open('processed_data/location_distance.pkl','rb'))
st.dataframe(location_df)

cosine_sim1 = pickle.load(open('processed_data/cosine_sim1.pkl','rb'))
cosine_sim2 = pickle.load(open('processed_data/cosine_sim2.pkl','rb'))
cosine_sim3 = pickle.load(open('processed_data/cosine_sim3.pkl','rb'))


def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 30 * cosine_sim1 + 20 * cosine_sim2 + 8 * cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df


# Test the recommender function using a property name
recommend_properties_with_scores('Ireo Victory Valley')
st.title('Select location at radius')
selected_location = st.selectbox('Location',sorted(location_df.columns.to_list()))
radius = st.number_input('Radius in kms')

if st.button('Search'):
    result_ser = location_df[location_df[selected_location]<radius*1000][selected_location].sort_values()
    if len(result_ser)==0:
        st.text('No properties')
    for key,val in result_ser.items():
        st.text(str(key) + " -> " + str(round(val/1000))+ 'kms')

st.title('Recommend Appartment')
selected_appartment = st.selectbox('SelectBox', sorted(location_df.index.to_list()))
if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_appartment)
    st.dataframe(recommendation_df)