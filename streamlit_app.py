import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Paths to data and model files
DATA_PATH = os.path.join("data", "heavy_vehicle_data.csv")
MODEL_PATH = os.path.join("models", "fuel_model.pkl")

st.set_page_config(page_title="Fuel Consumption Predictor", page_icon="🚛", layout="wide")

# Load dataset with caching
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

# Load model with caching
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

def data_overview(df):
    st.header("📊 Data Overview")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Statistical Summary")
    st.write(df.describe())

    st.subheader("Correlation Heatmap")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(plt.gcf())
    plt.clf()

def visualizations(df, model):
    st.header("📈 Visualizations")

    tabs = st.tabs(["Distributions", "Feature vs Fuel Consumption", "Feature Importance"])

    with tabs[0]:
        st.subheader("Feature Distributions")
        features = df.columns.drop('average_fuel_consumption')
        for feature in features:
            plt.figure(figsize=(6, 3))
            sns.histplot(df[feature], kde=True, bins=30)
            plt.title(f"Distribution of {feature}")
            st.pyplot(plt.gcf())
            plt.clf()

        st.subheader("Fuel Consumption Distribution")
        plt.figure(figsize=(8, 4))
        sns.histplot(df['average_fuel_consumption'], bins=30, kde=True, color='orange')
        plt.title("Distribution of Average Fuel Consumption")
        plt.xlabel("Fuel Consumption (L/100km)")
        st.pyplot(plt.gcf())
        plt.clf()

    with tabs[1]:
        st.subheader("Feature vs Fuel Consumption Scatter Plots")
        features = df.columns.drop('average_fuel_consumption')
        for feature in features:
            plt.figure(figsize=(6, 3))
            sns.scatterplot(x=df[feature], y=df['average_fuel_consumption'], alpha=0.5)
            plt.xlabel(feature)
            plt.ylabel("Fuel Consumption (L/100km)")
            plt.title(f"{feature} vs Fuel Consumption")
            st.pyplot(plt.gcf())
            plt.clf()

    with tabs[2]:
        st.subheader("Feature Importance")
        if hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
            indices = np.argsort(importances)[::-1]
            features_sorted = df.columns.drop('average_fuel_consumption')[indices]

            plt.figure(figsize=(8, 4))
            sns.barplot(x=importances[indices], y=features_sorted, palette="viridis")
            plt.title("Feature Importances from Model")
            st.pyplot(plt.gcf())
            plt.clf()
        else:
            st.info("Feature importance not available for this model type.")

def prediction_page(model):
    st.header("🚛 Predict Fuel Consumption")

    inputs = {
        'kinetic_energy': st.number_input("🔸 Kinetic Energy (J)", min_value=0.0, value=20000.0, step=1000.0),
        'potential_energy': st.number_input("🔸 Potential Energy (J)", min_value=0.0, value=8000.0, step=500.0),
        'average_speed': st.number_input("🔸 Average Speed (km/h)", min_value=0.0, value=60.0, step=1.0),
        'stops_count': st.number_input("🔸 Number of Stops", min_value=0, value=3, step=1),
        'trip_duration': st.number_input("🔸 Trip Duration (min)", min_value=0.0, value=120.0, step=5.0),
        'idle_time': st.number_input("🔸 Idle Time (min)", min_value=0.0, value=15.0, step=1.0),
        'elevation_gain': st.number_input("🔸 Elevation Gain (m)", min_value=0.0, value=200.0, step=10.0),
        'vehicle_load': st.number_input("🔸 Vehicle Load (kg)", min_value=0.0, value=2500.0, step=100.0),
        'ambient_temperature': st.number_input("🔸 Ambient Temperature (°C)", value=25.0, step=1.0),
        'tire_pressure': st.number_input("🔸 Tire Pressure (psi)", value=32.0, step=1.0),
    }

    if st.button("🚀 Predict Fuel Consumption"):
        input_df = pd.DataFrame([inputs])
        prediction = model.predict(input_df)[0]
        st.success(f"✅ Estimated Fuel Consumption: **{prediction:.2f} L/100km**")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Data Overview", "Visualizations"])

    if not os.path.exists(DATA_PATH):
        st.error(f"Data file not found: {DATA_PATH}")
        return
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found: {MODEL_PATH}")
        return

    data = load_data()
    model = load_model()

    if page == "Home":
        prediction_page(model)
    elif page == "Data Overview":
        data_overview(data)
    elif page == "Visualizations":
        visualizations(data, model)

if __name__ == "__main__":
    main()
