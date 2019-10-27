#!/usr/bin/env python3

"""
Tutorial obtained from
https://www.youtube.com/watch?v=6g4O5UOH304&t=1648s
and
https://www.tensorflow.org/alpha/tutorials/keras/basic_text_classification
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np

# Using the keras API to load in datasets, and the name of the dataset is called imdb.
data = keras.datasets.imdb

"""To prepare some data from the dataset for training and testing. It is not supposed to use the whole dataset
for training and testing as it takes too long and the result maybe the program remembers the whole dataset
and may use it repeatedly for new dataset, which then gives incorrect result.
To pass in param of num_words=10000 is look only at the most frequently used words of up to 10000.
"""
(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=10000)
