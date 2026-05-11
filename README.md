
# 🏠 Real Estate Price Prediction & Analytics App

This app provides **property price predictions**, **market insights**, **recommendations**, and **analytics**, all through an interactive **Streamlit** interface.

> 🔗 **Live App:** [https://real-estate-app.onrender.com](https://prop-insight-orfl.onrender.com/)

---

## 📌 Project Highlights

### ✅ Modules Implemented:
1. **Price Prediction:** Predicts property price using machine learning.
2. **Recommendation Engine:** Suggests properties based on amenities, budget, and location.
3. **Analytics Dashboard:** Visualizes market trends via plots, maps, and word clouds.
4. **Insights Module:** Displays trends like price increases between bedroom types, sector-wise differences (%), and more.

---

## 🧠 Machine Learning Pipeline

- **Preprocessing:** Handles missing values, outliers, engineered features (luxury score, etc.).
- **Encoding & Scaling:** Uses StandardScaler, ColumnTransformer, OneHot, Ordinal, and Target encoding.
- **Model Comparisons:** Evaluated various models (Random Forest, Linear Regression, SVR, etc.).
- **Final Model:** Random Forest chosen for deployment due to balance of accuracy and interpretability.

---

## 📈 Exploratory Data Analysis (EDA)
- Univariate & bivariate visualizations
- Floor and area distribution plots
- Amenity word clouds
- Heatmaps and scatter charts for geographic price patterns

---

## 💡 Insights Module
- Compares segment-wise price differences **in Gurgaon**
- Calculates **percentage increases**, **absolute differences**
- Highlights "Lowest vs Highest" sectors and more

---

## 🚀 Deployment Details

- **Tech Stack:** Python 3.12.3, Streamlit, Scikit-learn, Plotly, Seaborn
- **Dependencies:** Listed in `requirements.txt`
- **Deployment Platform:** Render (Docker-free using `.python-version`)

---

## 🚀 Run Locally

```bash
git clone https://github.com/Anshuman-Chakraborty/real-estate-app.git
cd real-estate-app
pip install -r requirements.txt
streamlit run Home.py
```

Make sure `.python-version` is present (`3.12.3`) for Render compatibility.

---

## 🌐 Auto-Deploy Setup (Render)

1. Connect your GitHub repo to Render.
2. Enable **Auto-deploy** for the `main` branch.
3. Add a `.python-version` file with:
   ```
   3.12.3
   ```
4. Push changes → Render will deploy automatically.

---

## 📂 Folder Structure

```
real-estate-app/
├── raw-data/
│   └── apartments.csv
│   └── flats.csv
│   └── houses.csv
│   └── latlong.csv
├── processed-data/
├── data-prepocessing/
│   └── data-preprocessing-flats.ipynb
│   └── data-preprocessing-houses.ipynb
│   └── merge-flats-and-house.ipynb
│   └── data-preprocessing-level-2.ipynb
├── EDA/
│   └── eda-univariate-analysis.ipynb
│   └── eda-multivariate-analysis.ipynb
│   └── eda-pandas-profiling.ipynb
├── feature-engineering/
│   └── feature-engineering.ipynb
│   └── outlier-treatment.ipynb
│   └── missing-value-imputation.ipynb
│   └── feature-selection-and-feature-engineering.ipynb
│   └── feature-selection.ipynb
├── models/
│   └── baseline-model.ipynb
│   └── model-selection.ipynb
│   └── pipeline.pkl
│   └── df.pkl
├── others/
│   └── data-visualization.ipynb
│   └── recommender-system.ipynb
├── models/
│   └── 1_PricePredictor.py
│   └── 2_AnalysisApp.py
│   └── 3_RecommendAppartments.py
│   └── 4_Insights.py
├── Home.py
├── requirements.txt
├── .python-version
├── render.yaml
├── .gitignore
└── README.md
```

---

