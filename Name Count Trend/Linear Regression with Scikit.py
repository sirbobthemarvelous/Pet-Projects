
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#use scikit-learn over sklearn
#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
import matplotlib.pyplot as pyplot
from matplotlib import style
from joblib import dump, load
#alternate version of pickle https://scikit-learn.org/stable/modules/model_persistence.html


data = pd.read_csv(r"C:\Users\robzh\Documents\python\Pet Projects Only For Fun (not Counting Nifty)\Name Count Trend\student-mat.csv.csv", sep=';')

print(data.head())

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
 # splitting the test samples as 10% of the data so they don't cheat by looking at the end

best = 0
for _ in range(300):

    linear = LinearRegression()

    linear.fit(x_train, y_train)
    # fits the data to find a best fit line
    accuracy = linear.score(x_test, y_test)
    print(accuracy)

    if accuracy > best:
        best = accuracy
        '''
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
            # save a pickle file in a directory """


pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

print('Co: \n', + linear.coef_)
print('Intercept: \n', + linear.intercept_)
'''

predictions = linear.predict(x_test)
#takes two dimentional arrays and makea bunch of predictions
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

style.use("ggplot")
# Drawing and plotting model
plot = "G1" # Change this to G1, G2, studytime or absences to see other graphs
pyplot.scatter(data[plot], data["G3"])
pyplot.legend(loc=4)
pyplot.xlabel(plot)
pyplot.ylabel("Final Grade")
pyplot.show()