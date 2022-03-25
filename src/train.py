# this module contains feature engineering functions for the weather data
# preparation for the CNN model
from statistics import mode
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout, BatchNormalization
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping


def read_data():
    """
    function to read extracted data from the images
    """
    data = np.load('data.npy')
    labels = np.load('labels.npy')
    return data, labels




def prepare_for_cnn(data, labels):
    """
    function to prepare data for the CNN model
    """
    data = data.reshape(data.shape[0], 256, 256, 1)
    labels = labels.reshape(labels.shape[0], 1)

    # one hot encoding of labels
    encoder = OneHotEncoder(sparse=False)
    labels = encoder.fit_transform(labels)

    X_train,X_test,y_train,y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    return X_train,X_test,y_train,y_test




class Classifier():
    """
    Classifier class
    """
    def __init__(self, X_train, X_test, y_train, y_test):
        """
        Initialize classifier
        """
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.model = None
        
    def train(self):
        """
        Train the model
        """
        self.model = Sequential()
        self.model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', input_shape=(128, 128, 1)))
        self.model.add(Conv2D(32, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))
        self.model.add(Flatten())
        self.model.add(Dense(600, activation='relu'))
        self.model.add(Dropout(0.6))
        self.model.add(BatchNormalization())
        self.model.add(Dense(600, activation='relu'))
        self.model.add(Dropout(0.6))
        self.model.add(BatchNormalization())
        self.model.add(Dense(11, activation='sigmoid'))
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model.fit(self.X_train, self.y_train, batch_size=24,
                        epochs=300, verbose=1, validation_data=(self.X_test, self.y_test),
                        callbacks=[ModelCheckpoint('model.h5', monitor='val_accuracy', verbose=1, save_best_only=True, mode='max'),
                                      EarlyStopping(monitor='val_accuracy', patience=15, verbose=1, mode='max')]
                        )
        
    def predict(self):
        """
        Predict the labels for the test data
        """
        y_pred = self.model.predict(self.X_test)
        #y_pred = (y_pred > 0.5)
        return y_pred
    
    def evaluate(self):
        """
        Evaluate the model
        """
        score = self.model.evaluate(self.X_test, self.y_test, verbose=1)
        print('Test loss:', score[0])
        print('Test accuracy:', score[1])





if __name__ == '__main__':
    print('starting to read data')
    data, labels = read_data()
    print(np.shape(data))
    print(np.shape(labels))
    X_train,X_test,y_train,y_test = prepare_for_cnn(data, labels)
    model = Classifier(X_train, X_test, y_train, y_test)
    model.train()
    #print(data)

