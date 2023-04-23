from tensorflow.keras import Sequential
from tensorflow.keras.layers import SimpleRNN, Dropout, Dense, Activation, BatchNormalization
from sklearn.preprocessing import OneHotEncoder

def simpleRNN1(input_shape, output_nodes, dropout):
    model = Sequential()
    model.add(BatchNormalization())
    model.add(SimpleRNN(128, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(dropout))
    model.add(SimpleRNN(128, return_sequences=True))
    model.add(Dropout(dropout))
    model.add(Dense(output_nodes))
    model.add(Activation('softmax'))

    return model

def simpleRNN2(input_shape, output_nodes, dropout):
    model = Sequential()
    model.add(BatchNormalization())
    model.add(SimpleRNN(128, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(dropout))
    model.add(SimpleRNN(128, return_sequences=True))
    model.add(Dropout(dropout))
    model.add(SimpleRNN(256))
    model.add(Dense(256))
    model.add(Dropout(dropout))
    model.add(Dense(output_nodes))
    model.add(Activation('softmax'))

    return model

def simpleRNN3(input_shape, output_nodes, dropout):
    model = Sequential()
    model.add(BatchNormalization())
    model.add(SimpleRNN(256, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(dropout))
    model.add(SimpleRNN(256, return_sequences=True))
    model.add(Dropout(dropout))
    model.add(SimpleRNN(256))
    model.add(Dropout(dropout))
    model.add(SimpleRNN(256))
    model.add(Dropout(dropout))
    model.add(Dense(256))
    model.add(Dropout(dropout))
    model.add(Dense(output_nodes))
    model.add(Activation('softmax'))

    return model