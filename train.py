
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from model import build_model
import matplotlib.pyplot as plt
import math

data = pd.read_csv("earthquake_data.csv")

features = data[['latitude', 'longitude', 'depth']]
target = data['magnitude']

scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2)

X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

model = build_model((X_train.shape[1], X_train.shape[2]))

history = model.fit(X_train, y_train, epochs=10, batch_size=8, validation_data=(X_test, y_test))


# Save the scaler for use in prediction
import pickle
with open("scaler.pkl", "wb") as f:
	pickle.dump(scaler, f)


# Save the scaler for use in prediction
import pickle
with open("scaler.pkl", "wb") as f:
	pickle.dump(scaler, f)

model.save("earthquake_model.h5")

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.savefig("accuracy_plot.png")
