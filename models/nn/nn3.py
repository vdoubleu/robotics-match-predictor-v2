import tensorflow as tf
from tensorflow import keras
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
import math
from make_frame import make_flat_dataframe

df = make_flat_dataframe()

dataIn = df[["red1vrating_rank", "red1vrating", "red2vrating_rank", "red2vrating", "blue1vrating_rank", "blue1vrating", "blue2vrating_rank", "blue2vrating"]].copy()

df["redWin"] = np.where((df["redScore"] > df["blueScore"]), 1, 0)
df["blueWin"] = np.where((df["blueScore"] > df["redScore"]), 1, 0)

dataOut = df[["redWin", "blueWin"]].copy()


dataInTrain, dataInTest, dataOutTrain, dataOutTest = train_test_split(dataIn, dataOut, test_size=0.2)

model = keras.Sequential([
    keras.layers.Input(shape=(len(dataInTrain.columns), )),
    keras.layers.Dense(64, activation="elu"),
    keras.layers.Dense(8, activation="elu"),
    keras.layers.Dense(2, activation="softmax")])

model.compile(optimizer="adam", loss=keras.losses.binary_crossentropy, metrics=["accuracy"])

model.fit(dataInTrain.values, dataOutTrain.values, epochs = 5)

test_loss, test_acc = model.evaluate(dataInTest.values, dataOutTest.values)


