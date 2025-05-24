# Fuel Consumption Predictor for Heavy Vehicles 🚛⛽

Welcome to the Fuel Consumption Predictor project! This machine learning app estimates the average fuel consumption (in liters per 100 km) of heavy vehicles using key parameters like kinetic energy, potential energy, speed, number of stops, and other important factors.

## Features

- **User-friendly web app** built with Streamlit for interactive fuel consumption prediction.
- **Explore the dataset** with overview stats, correlations, and data visualizations.
- **Detailed visuals** include feature distributions, scatter plots, and model-based feature importance.
- Easy to run locally or deploy on Streamlit Cloud.

## Folder Structure

fuel-consumption-predictor/
├── data/
│   └── heavy_vehicle_data.csv        # CSV dataset for training and visualization
├── models/
│   └── fuel_model.pkl                # Trained ML model (serialized with joblib)
├── src/
│   └── train_model.py                # Script to train and save the ML model
├── .gitignore                        # Specifies files/folders to ignore in Git
├── generate_data.py                  # Script to generate synthetic dummy data
├── README.md                         # Project overview and usage documentation
├── requirements.txt                  # List of Python dependencies
└── streamlit_app.py                  # Main Streamlit application for user interaction

---

## Getting Started

### Prerequisites

- Python 3.8+
- Git (for cloning the repo)
- Optional: Virtual environment tool like `venv`

### Installation & Running

1. **Clone this repository:**
   bash
   git clone https://github.com/SArshita/fuel-consumption-predictor.git
   cd fuel-consumption-predictor

2. (Optional) Create a virtual environment:
    bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install required packages:
    bash
    pip install -r requirements.txt

4. Run the Streamlit app:
    bash
    streamlit run app/streamlit_app.py

5. Open your browser to the URL shown (usually http://localhost:8501) and start predicting!

### Deployment
You can deploy this app on Streamlit Cloud easily:

1. Push your project to a GitHub repo.
2. Connect the repo on Streamlit Cloud.
3. Deploy and share your predictive web app with others instantly.

# Contributing
Feel free to fork this repo and submit pull requests. Whether it's improving the model, adding features, or enhancing visuals — contributions are welcome!

# Author
Arshita Satpute
Email: satputearshita@gmail.com
GitHub: SArshita

Thank you for checking out this project! 🚀
