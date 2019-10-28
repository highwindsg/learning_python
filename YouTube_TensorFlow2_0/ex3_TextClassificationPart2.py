#!/usr/bin/env python3

# What is an Embedding Layer?

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
To pass in param of num_words=10000 is look only at the most frequently used words of up to 10000."""
(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=10000)

# The output will be a list of integers that points to a certain word in the data set.
# But it is quite meaningless as there are no mappings to any actual words so far.
# print(train_data[0])

# To create own mappings for words with our own dictionary we have in tensorflow.
word_index = data.get_word_index()

word_index = {k: (v + 3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# Pre-processing of data to make the data into a form that our model can accept and consistent.
train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post",
                                                        maxlen=250)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding="post", maxlen=250)


# print(len(train_data), len(test_data))

def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])


# print(decode_review(test_data[0]))

# Building the architecture of the model down here.

model = keras.Sequential()
model.add(keras.layers.Embedding(10000, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))
"""We want the final output to be whether the review is good or bad.
And so the output neuron should be either 0 or 1, or somewhere in between there to give us kind of a probability.
We accomplish this by using sigmoid function because whatever our value is in between 0 and 1, it will test if our 
model is actually working properly and to get the value that we want."""

model.summary()
