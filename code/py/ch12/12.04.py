from keras.models import Sequential
from keras.layers import *

my_model = Sequential()
my_model.add(Conv2D(filters=32, kernel_size=3, activation='relu',
                    input_shape=(28, 28, 1)))
my_model.add(MaxPooling2D(pool_size=2))
my_model.add(Dropout(rate=0.25)) # ドロップアウト
my_model.add(Flatten())
my_model.add(Dense(128, activation='relu'))
my_model.add(Dense(10, activation='softmax'))

from keras.models import Sequential
from keras.layers import *
from keras import regularizers

my_model = Sequential()
my_model.add(Conv2D(filters=32, kernel_size=3, activation='relu',
                    input_shape=(28, 28, 1)))
my_model.add(MaxPooling2D(pool_size=2))
my_model.add(Flatten())
my_model.add(Dense(128, activation='relu',
                   kernel_regularizer=regularizers.l2(0.001))) # Ridge回帰
my_model.add(Dense(10, activation='softmax'))

