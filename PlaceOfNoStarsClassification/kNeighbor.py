import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")
print(data.head())

optimusPrime = preprocessing.LabelEncoder()
buying = optimusPrime.fit_transform(list(data["buying"]))
maint = optimusPrime.fit_transform(list(data["maint"]))
doors = optimusPrime.fit_transform(list(data["doors"]))
persons = optimusPrime.fit_transform(list(data["persons"]))
lug_boot = optimusPrime.fit_transform(list(data["lug_boot"]))
safety = optimusPrime.fit_transform(list(data["safety"]))
assClass = optimusPrime.fit_transform(list(data["class"]))
# turn low medium high into 1,2,3, turning it into numpy arrays to transform them

predict = "class"

x = list(zip(buying, maint, doors, persons, lug_boot, safety))
y = list(assClass)
# zip creates tuple objects...the numpy array

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

print(x_train, y_test)

model = KNeighborsClassifier(n_neighbors=7)
# you can change the K value
model.fit(x_train, y_train)  # train the model
accuracy = model.score(x_test, y_test)
print(accuracy)

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]
# displaying the name rather than numbers

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
    # redisplay the data
    burp = model.kneighbors([x_test[x]], 9, True)
    # ensure that its just one result and it's not treated as two dimentional,
    # then number of neighbors, then ensure distance is true
    print("N: ", burp)


