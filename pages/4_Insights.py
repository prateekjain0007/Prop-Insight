import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("📊 Gurgaon Real Estate Insights")


df = pd.read_csv('processed_data/gurgaon_properties_post_feature_selection_v2.csv').drop(columns=['store room','floor_category','balcony'])


# Category-wise price insights
st.subheader("📊 Price differences by category")

category_cols = ['property_type', 'sector', 'furnishing_type', 'luxury_category']
numerical_cols = ['bedRoom', 'bathroom']
discrete_numeric_cols = ['servant room']
binned_numerical_cols = ['built_up_area']


for col in category_cols:
    st.markdown(f"### {col.replace('_', ' ').title()}")
    agg = df.groupby(col)['price'].mean()

    low_cat = agg.idxmin()
    low_price = agg.min()
    high_cat = agg.idxmax()
    high_price = agg.max()
    diff = high_price - low_price

    st.write(agg.sort_values())  # optional to show full table

    st.markdown(f"""
    - **Lowest**: `{low_cat}` → ₹{low_price:.2f} Cr  
    - **Highest**: `{high_cat}` → ₹{high_price:.2f} Cr  
    - **Difference**: ₹{diff:.2f} Cr
    """)

st.subheader("🔢 Price trends across numerical features (Direct Grouping)")

for col in numerical_cols:
    st.markdown(f"### {col.replace('_', ' ').title()}")

    agg = df.groupby(col)['price'].mean().sort_index()
    min_val = agg.index.min()
    max_val = agg.index.max()
    min_price = agg.loc[min_val]
    max_price = agg.loc[max_val]
    diff = max_price - min_price

    st.line_chart(agg)

    st.markdown(f"""
    - **Min** `{col}`: {min_val} → ₹{min_price:.2f} Cr  
    - **Max** `{col}`: {max_val} → ₹{max_price:.2f} Cr  
    - **Price Increase**: ₹{diff:.2f} Cr
    """)

st.subheader("📊 Price Trends for Discrete Numeric Columns")

for col in discrete_numeric_cols:
    st.markdown(f"### {col.replace('_', ' ').title()} (Grouped by Value)")

    agg = df.groupby(col)['price'].mean().sort_index()

    if agg.empty or len(agg) < 2:
        st.warning(f"Not enough variation in {col} for analysis.")
        continue

    min_val = agg.index[0]
    max_val = agg.index[-1]
    min_price = agg.iloc[0]
    max_price = agg.iloc[-1]
    diff = max_price - min_price

    st.bar_chart(agg)

    st.markdown(f"""
    - **{col} = {min_val}** → ₹{min_price:.2f} Cr  
    - **{col} = {max_val}** → ₹{max_price:.2f} Cr  
    - **Price Difference**: ₹{diff:.2f} Cr
    """)

st.subheader("📊 Binned Price Trends for Wide-Range Columns")

# You can define bin sizes per column
fixed_bins = {
    'built_up_area': 1000  # bin width in sqft
}

for col in binned_numerical_cols:
    st.markdown(f"### {col.replace('_', ' ').title()} (Binned by {fixed_bins[col]} sqft)")

    min_val = df[col].min()
    max_val = df[col].max()
    bin_width = fixed_bins[col]

    # Create bin intervals
    bins = pd.interval_range(start=min_val, end=max_val + bin_width, freq=bin_width, closed='right')

    # Bin the values
    df[f'{col}_bin'] = pd.cut(df[col], bins=bins)

    # Remove rows that didn't fall into any bin (NaNs)
    valid_df = df[~df[f'{col}_bin'].isna()].copy()

    # Convert bin intervals to strings for chart compatibility
    valid_df[f'{col}_bin'] = valid_df[f'{col}_bin'].astype(str)

    # Group by bin and calculate mean price
    agg = valid_df.groupby(f'{col}_bin')['price'].mean().sort_index()

    if agg.empty or len(agg) < 2:
        st.warning(f"Not enough variation in {col} for binning.")
        continue

    # Chart + insights
    st.bar_chart(agg)

    min_bin = agg.index[0]
    max_bin = agg.index[-1]
    min_price = agg.loc[min_bin]
    max_price = agg.loc[max_bin]
    diff = max_price - min_price

    st.markdown(f"""
    - **Lowest Range**: `{min_bin}` → ₹{min_price:.2f} Cr  
    - **Highest Range**: `{max_bin}` → ₹{max_price:.2f} Cr  
    - **Price Difference**: ₹{diff:.2f} Cr
    """)
