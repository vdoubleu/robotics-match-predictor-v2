import pandas as pd
import matplotlib as plt
import numpy as np
from make_frame import make_flat_dataframe
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = make_flat_dataframe()

dataIn = df[["red1wins", "red1losses", "red2wins", "red2losses", "blue1wins", "blue1losses", "blue2wins", "blue2losses"]].copy()

#red win => 1, blue win => 0
df["win"] = np.where((df["redScore"] > df["blueScore"]), 1, 0)

dataOut = df[["win"]].copy()

dataInTrain, dataInTest, dataOutTrain, dataOutTest = train_test_split(dataIn, dataOut, test_size=0.2)


model = RandomForestClassifier()
model.fit(dataInTrain, dataOutTrain.values.ravel())

acc = model.score(dataInTest, dataOutTest)
print(acc)
