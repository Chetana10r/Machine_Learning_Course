from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# LOAD THE SAVED MODEL
model = pickle.load(open("linear_model.pkl", "rb"))

@app.route("/")
def home():
    return "Flask server is running"

# PREDICT ROUTE
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # Example input: {"features": [34, 1, 2, 1, 0, 0]}
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"predicted_fare": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
