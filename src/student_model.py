import pandas as pd
import tensorflow as tf
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# read the dataset
df = pd.read_csv("taxifares.csv", parse_dates=["pickup_datetime"])
print(df.head())

# drop key
df.drop("key", axis=1, inplace=True)
print(df.head())

# Extract time and distance
df["day_of_week"] = df["pickup_datetime"].dt.weekday
df["pickup_time"] = df["pickup_datetime"].dt.hour + df["pickup_datetime"].dt.minute/60
df["a"] = (df['dropoff_longitude'] - df['pickup_longitude']) * 54.6
df["b"] = (df['dropoff_latitude'] - df['pickup_latitude']) * 69.0
df["distance"] = (df["a"]**2. + df["b"]**2.) ** (0.5)

# drop columns
df.drop(['pickup_datetime', 'pickup_longitude', 'pickup_latitude',
         'dropoff_longitude', 'dropoff_latitude', 'a', 'b'], axis=1, inplace=True)
print(df.head())

# set up features and target
X = df.drop('fare_amount', axis = 1)
y = df['fare_amount']

# build keras neural network
model = keras.models.Sequential()
model.add(keras.Input(shape=(4,)))
model.add(Dense(50, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse', metrics=['mse'])
model.summary()

#train the model
hist = model.fit(X, y, validation_split=0.3, epochs=50, verbose=1)

#plot mean squared error
err = hist.history['acc']
val_err = hist.history['val_acc']
epochs = range(1, len(err) + 1)

plt.plot(epochs, err, '-', label='Training MSE')
plt.plot(epochs, val_err, ':', label='Validation MSE')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Mean Squared Error')
plt.legend(loc='upper right')
plt.show()

print("R squared score is ", r2_score(y, model.predict(X)))


