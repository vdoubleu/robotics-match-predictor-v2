import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from make_frame import make_flat_dataframe
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


df = make_flat_dataframe()

dataIn = df.copy().drop(["redScore", "blueScore"], axis=1)

#red win => 1, blue win => 0
df["win"] = np.where((df["redScore"] > df["blueScore"]), 1, -1)

dataOut = df[["win"]].copy()


dataInTrain, dataInTest, dataOutTrain, dataOutTest = train_test_split(dataIn, dataOut, test_size=0.2)

#print(dataInTrain.values)
#print(dataOutTrain.values.flatten())


#plots the cumulative variance to help determine how many components are required
data = PCA().fit(dataInTrain.values)
plt.plot(np.cumsum(data.explained_variance_ratio_))
plt.xlabel('number of comp')
plt.ylabel('cum explained var')
plt.show()

"""
# tries with every possible number of components
for i in range(60):
    #reduce dimensionality
    model = PCA(i+1)
    PCA_data = model.fit_transform(dataInTrain.values)
    
    #create model using gaussianNB
    clf = GaussianNB()
    clf.fit(PCA_data, dataOutTrain.values.flatten())
    
    #reduce test data dimension
    score_model = PCA(i+1)
    score_PCA_data = model.fit_transform(dataInTest.values)
    
    #score test data
    acc = clf.score(score_PCA_data, dataOutTest.values.flatten())
    print("acc:", acc, "comp: ", i+1)
"""
