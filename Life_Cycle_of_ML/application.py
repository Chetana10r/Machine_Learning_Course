from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 

application = Flask(__name__)
app = application

# Load Ridge Regressor and Standard Scaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler_model = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')  # Main landing page (index.html)

@app.route("/predictdata", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Extract form inputs
        temperature = float(request.form.get("temperature"))
        precipitation = float(request.form.get("precipitation"))
        RH = float(request.form.get("RH"))
        FWC = float(request.form.get("FWC"))
        Wind_speed = float(request.form.get("Wind_speed"))
        VPD = float(request.form.get("VPD"))
        UTCI = float(request.form.get("UTCI"))
        Region = float(request.form.get("Region"))

        # Create a dataframe for the model
        input_data = pd.DataFrame([[temperature, precipitation, RH, FWC, Wind_speed, VPD, UTCI, Region]],
                                  columns=['temperature', 'precipitation', 'RH', 'FWC', 'Wind_speed', 'VPD', 'UTCI', 'Region'])

        # Scale the data
        scaled_data = standard_scaler_model.transform(input_data)

        # Make prediction
        result = ridge_model.predict(scaled_data)

        # Return prediction to HTML
        return render_template('home.html', result=round(result[0], 2))

    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
