#!/usr/bin/env python
# coding: utf-8

# In[138]:


# Importing the pandas lib and set it as pd.
import pandas as pd
# Importing the Decision Tree algorithm machine learning method from Scikit-Learn's tree lib.
from sklearn.tree import DecisionTreeClassifier
# Importing the training, testing and spliting func method from Scikit-Learn's model selection lib.
from sklearn.model_selection import train_test_split
# Importing the accuracy_score func method from Scikit_Learn's metrics lib. This is for testing the
# accuracy of the test data set.
from sklearn.metrics import accuracy_score


music_data = pd.read_csv("music.csv")   # from pd use the .read_csv() and pass in the csv filename, and assign to
                                        # var music_data.
#music_data    # client call var obj music_data
#print("")
X = music_data.drop(columns=["genre"])  # from music_data, drop the column of genre, and assign the result to X.
X    # client call var obj X
#print("")
y = music_data["genre"]
#y    # client call var obj y

# X-train and X_test are the input data sets for training and testing.
# y_train and y_test are the output data sets for training and testing.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)    # 0.2 means using test data size of 20%)

model = DecisionTreeClassifier()
#model.fit(X, y)
# To fit the X_train and y_train data sets into the training model.
model.fit(X_train, y_train)

# To find out what music does 21 yrs old make likes, and what 22 yrs old female likes,
# where 1 = male and 0 = female.
#predictions = model.predict([ [21, 1], [22, 0] ])
predictions = model.predict(X_test)    # X_test contains input values for testing.
#predictions    # client call var obj predictions.

score = accuracy_score(y_test, predictions)
score    # To keep re-running this output in Jupyter Notebook without returning a new line,
         # press Ctrl+Enter

