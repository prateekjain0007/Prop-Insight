import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(page_title = "viz Demo")

st.title('Analysis')


new_df = pd.read_csv('processed_data/data_viz1.csv')
feature_text = pickle.load(open('processed_data/feature_text.pkl','rb'))
group_df = new_df.groupby('sector')[['price', 'price_per_sq_ft', 'built_up_area', 'latitude', 'longitude']].mean()
st.header('Sector prices')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sq_ft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width = 1200, height = 700, hover_name = group_df.index)
st.plotly_chart(fig,use_container_width=True)

st.header('Feature Cloud')
plt.rcParams["font.family"] = "Arial"

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)
ax.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig)

st.header('Area vs Price')
property_type = st.selectbox('Select Property Type',['flat','house'])
if property_type == 'house':
    fig2 = px.scatter(new_df[new_df['property_type']=='house'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.scatter(new_df[new_df['property_type']=='flat'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig2, use_container_width=True)

st.header('BHK Piechart')
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')
selected_sector = st.selectbox('Select Sector',sector_options)
if selected_sector == 'overall':
    fig3 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig3, use_container_width=True)
else:
    fig3 = px.pie(new_df[new_df['sector']==selected_sector], names='bedRoom')
    st.plotly_chart(fig3, use_container_width=True)

st.header('Side by side BHK comparison')
fig4 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig4, use_container_width=True)

st.header('Side by side Distplot for property type')
fig5 = plt.figure(figsize = (10,4))
sns.histplot(new_df[new_df['property_type'] == 'house']['price'], label='House', kde=True,stat='density',element='step',fill=True,)
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], label='Flat', kde=True,stat='density',element='step',fill=True,)
plt.legend()
plt.xlabel('Price')
plt.ylabel('Density')
st.pyplot(fig5, use_container_width=True)

