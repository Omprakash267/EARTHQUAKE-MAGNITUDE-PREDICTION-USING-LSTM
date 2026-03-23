
from flask import Flask, request, jsonify, render_template
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import pickle

app = Flask(__name__)

model = load_model("earthquake_model.h5", compile=False)
# Load the scaler used during training
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[data['latitude'], data['longitude'], data['depth']]])
    features_scaled = scaler.transform(features)
    features_scaled = np.reshape(features_scaled, (features_scaled.shape[0], 1, features_scaled.shape[1]))
    prediction = model.predict(features_scaled)
    return jsonify({"predicted_magnitude": float(prediction[0][0])})

if __name__ == '__main__':
    app.run(debug=True)
