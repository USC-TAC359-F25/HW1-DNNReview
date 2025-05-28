import pandas as pd
import tensorflow as tf
import keras
import numpy as np
# Note: matplotlib.pyplot and sklearn.metrics imports are missing

# read the dataset
df = pd.read_csv("taxifares.csv", parse_dates=["pickup_datetime"])
print(df.head())

# drop key
df.drop("key", axis=1, inplace=True)
print(df.head())

# Extract time but NOT distance (missing distance calculation)
df["day_of_week"] = df["pickup_datetime"].dt.weekday
df["pickup_time"] = df["pickup_datetime"].dt.hour + df["pickup_datetime"].dt.minute/60
# No distance column calculated here

# drop columns (without dropping distance, since it's missing)
df.drop(['pickup_datetime'], axis=1, inplace=True)
print(df.head())

# set up features and target
X = df.drop('fare_amount', axis = 1)
y = df['fare_amount']

# build keras neural network — minimal, missing Dense layers and compile
model = keras.models.Sequential()
model.add(keras.Input(shape=(3,)))  # wrong input shape (3 instead of 4)
# No Dense layers, no compile, no summary

# no training step (no model.fit)

# no plotting code (missing plotting entirely)

# no prediction call at all

print("Model defined but incomplete.")
