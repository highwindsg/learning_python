#!/usr/bin/env python3

"""
Tutorial obtained from
https://www.youtube.com/watch?v=6g4O5UOH304&t=1648s
and
https://www.tensorflow.org/tutorials/keras/classification
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Using the keras API to load in datasets, and the name of the dataset is called fashion_mnist.
data = keras.datasets.fashion_mnist

"""To prepare some data from the dataset for training and testing. It is not supposed to use the whole dataset
for training and testing as it takes too long and the result maybe the program remembers the whole dataset
and may use it repeatedly for new dataset, which then gives incorrect result."""
(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# To shrink down the images for easier to work with in the training model later.
train_images = train_images / 255.0
test_images = test_images / 255.0

# print(train_images[0])  # This will show the pixel values in grey scale in a long list.
#
# # Showing the image in binary mode which is slightly clearer.
# plt.imshow(train_images[0], cmap=plt.cm.binary)
# plt.show()

# Building model with a sequence of layers.
model = keras.Sequential([
    # To flatten the data so that it is passable to the different layers of the neural network. Each image is
    # represented as 28 by 28 pixels.
    keras.layers.Flatten(input_shape=(28, 28)),

    # A dense layer is a fully connected layer, parsing in 128 connected neurons and activation value set to be a
    # rectified linear unit. You can use arbitrarily different activation method, but linear units is a very fast
    # activation unit to start with.
    keras.layers.Dense(128, activation="relu"),

    # Another dense connected layer with 10 neurons and activation value set to softmax. Softmax function
    # will pick values of each neurons so that all those values will add up to one. Therefore it is a probability
    # layer what the network thinks for each given class.
    keras.layers.Dense(10, activation="softmax")
])

# The params of optimizer, loss and metrics are arbitrary and will be explained later, or googled later.
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=5)  # epochs means how many times the model is going to see the same image
# and using epochs needs to be tried a few times to see how many times it will need to train more accurately.

# To see how this model works, we have to test it on the test images and test labels to see how many it gets correct.
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Tested Accuracy:", test_acc)

# Using the model to make predictions.
# The .predict() method will give you a group of predictions, so must pass in all the test images.
prediction = model.predict(test_images)

# The output will be all the different probabilities that the neural network has predicted.
# Since we got 10 ten neurons (T-shirt/top to Ankle boot), this will get the largest value and finds the index of
# that value.
# print(class_names[np.argmax(prediction[0])])
# You will get Ankle boot as the prediction instead of just getting a prediction in number arrays.

# Or you can loop through the prediction and show the images of what is the prediction and what is the actual image.
for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_labels[i]])
    plt.title("Prediction: " + class_names[np.argmax(prediction[i])])
    plt.show()
