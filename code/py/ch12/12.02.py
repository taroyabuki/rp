x_train1d = x_train.reshape(-1, 784)
x_test1d = x_test.reshape(-1, 784)

from keras.models import Sequential
from keras.layers import Dense

my_model = Sequential()
my_model.add(Dense(units = 256, activation = "relu", input_dim = 784))
my_model.add(Dense(units = 10, activation = "softmax"))

my_model.compile(loss = 'sparse_categorical_crossentropy',
                 optimizer = 'rmsprop',
                 metrics = ['accuracy'])

from keras.callbacks import EarlyStopping
my_cb = [EarlyStopping(patience=5,                   # 訓練停止条件
                       restore_best_weights = True)] # 最善を保持

my_history = my_model.fit(
    x=x_train1d,          # 入力変数
    y=y_train,            # 出力変数
    validation_split=0.2, # 検証データの割合
    batch_size=128,       # バッチサイズ
    epochs=20,            # エポック数の上限
    callbacks=my_cb)      # エポックごとに行う処理

my_plot_loss_acc(my_history)

my_prob = my_model.predict(x_test1d)
my_pred = np.argmax(my_prob, axis=-1)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, my_pred)
#> array([[ 962,    0,    1,    4,    0,    3,    6,    1,    1,    2],
#>        [   0, 1109,    4,    1,    0,    1,    5,    2,   13,    0],
#>        [   8,    5,  938,   14,    4,    2,   12,   17,   30,    2],
#>        [   1,    1,   13,  954,    0,   10,    1,   11,   14,    5],
#>        [   2,    4,    2,    5,  911,    0,   15,    6,    6,   31],
#>        [   8,    2,    1,   35,    3,  812,    9,    7,   12,    3],
#>        [  12,    3,    3,    1,    8,   21,  903,    1,    6,    0],
#>        [   1,    6,   14,   10,    3,    1,    0,  972,    2,   19],
#>        [   6,    1,    8,   19,    6,   12,   10,   16,  891,    5],
#>        [  10,    5,    1,   15,   15,    4,    1,   26,    8,  924]])

(y_test == my_pred).mean()
#> 0.9376

my_model.evaluate(x=x_test1d, y=y_test)
#> [0.21355792880058289,
#>  0.9376000165939331]

