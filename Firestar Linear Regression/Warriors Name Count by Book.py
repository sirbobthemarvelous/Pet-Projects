import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as pyplot
from matplotlib import style
from joblib import dump, load

data = pd.read_csv(r"C:\Users\robzh\Documents\python\Pet Projects Only For Fun (not Counting Nifty)\Name Count Trend\FirestarNamedrops.csv")

X = data['Main Book'].values.reshape(-1,1)
# you have to use array.reshape(-1,1) if its a single feature when using the predict function now
y = data['Firestars']
#print(data.head())

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2 ,random_state=1)
#test size is specifically 5 rather than a percentage, random stat is none by default tho
#actually it looks like even at 0 there's randomization in the test training split so, just go with percentage

linear = LinearRegression()
linear.fit(X_train,y_train) # creates the LIne of best fit....eqn

y_pred = linear.predict(X_test)
#print(y_pred)

style.use("ggplot")
# Drawing and plotting model
#The ACTUAL TRAINING SET and Line of Best Fit
pyplot.scatter(X_train, y_train, color='red') 
pyplot.plot(X_test, y_pred, color = 'blue')
pyplot.title('Number of Times Firestar is Namedropped by Book')
pyplot.xlabel('Mainline Book Number')
pyplot.ylabel("Number of Firestars")
pyplot.show()

# The ACTUAL TEST SET and Line of Best Fit
#pyplot.plot(x_test, predictions, label = "Linear Regression", color = 'b')
pyplot.scatter(X_test, y_test, color='red') 
pyplot.plot(X_test, y_pred, color = 'blue')
pyplot.title('Number of Times Firestar is Namedropped by Book')
pyplot.xlabel('Mainline Book Number')
pyplot.ylabel("Number of Firestars")
pyplot.show()

#model scoring
print(linear.score(X_test,y_test))