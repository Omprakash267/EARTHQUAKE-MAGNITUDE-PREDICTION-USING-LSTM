# 🌍 Earthquake Magnitude Prediction using LSTM

## 📌 Overview

This project is a deep learning-based web application that predicts earthquake magnitude using geographical parameters such as latitude, longitude, and depth. The system uses an LSTM (Long Short-Term Memory) model to learn patterns from historical earthquake data and provides real-time predictions through a web interface.

---

## 🚀 Features

* LSTM-based deep learning model
* Data preprocessing (normalization, train-test split)
* Model evaluation using MSE and RMSE
* Flask-based backend API (`/predict`)
* Interactive frontend (HTML, CSS, JavaScript)
* Real-time prediction
* Training performance visualization (loss graph)

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* Flask
* Pandas, NumPy, Scikit-learn
* Matplotlib
* HTML, CSS, JavaScript

---

## 📂 Project Structure

```
earthquake_prediction/
├── app.py
├── model.py
├── train.py
├── earthquake_data.csv
├── earthquake_model.h5
├── accuracy_plot.png
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## ⚙️ Installation (Windows CMD)

### Step 1: Clone the repository

```
git clone https://github.com/your-username/earthquake_prediction.git
cd earthquake_prediction
```

### Step 2: Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install dependencies

```
pip install -r requirements.txt
```

---

## 🧠 Model Training

Run the following command to train the LSTM model:

```
python train.py
```

This will:

* Train the model
* Save the model as `earthquake_model.h5`
* Generate `accuracy_plot.png`

---

## ▶️ Run the Application

Start the Flask server:

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📥 Input Format

Enter the following values in the web interface:

* Latitude: (-90 to 90)
* Longitude: (-180 to 180)
* Depth: (1 to 700 km)

### Example Input

```
Latitude: 13.08
Longitude: 80.27
Depth: 10
```

---

## 📤 Output

The system will display:

```
Predicted Magnitude: <value>
```

---

## 📊 How It Works

1. Dataset is loaded and preprocessed
2. Features (latitude, longitude, depth) are normalized
3. LSTM model is trained on the dataset
4. Model is saved and used in Flask backend
5. User inputs are passed to the model
6. Predicted magnitude is returned and displayed

---

## 🎯 Applications

* Earthquake risk analysis
* Geophysical prediction systems
* Academic deep learning projects
* Real-time ML web applications

---

## ⚠️ Disclaimer

This project is for educational purposes only. Real-world earthquake prediction requires large-scale seismic data and advanced modeling techniques.

---

## 👨‍💻 Author

Your Name

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
