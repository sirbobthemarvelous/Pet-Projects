import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv(r"C:\Users\robzh\Documents\python\Pet Projects Only For Fun (not Counting Nifty)\MultipleBooksClassification\Arc 1 Everyone.csv")
print(data.head())

# preprocessing.LabelEncoder() and then .fit_transform is good for when the data isn't on the same scale

name = (list(data["Name"]))
book1 = (list(data["Firestar"]))
book2 = (list(data["Graystripe"]))
book3 = (list(data["Bluestar"]))
book4 = (list(data["Tree"]))
book5 = (list(data["Sandstorm"]))
book6 = (list(data["Cloudtail"]))
booktotal= (list(data['Tallstar']))
# turn low medium high into 1,2,3, turning it into numpy arrays to transform them

predict = "class"

x = list(zip(book1, book2, book3, book4, book5, book6))
y = list(booktotal)
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


