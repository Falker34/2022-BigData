import pandas as pd
import numpy as np
import pathlib
import tensorflow as tf
import os
from keras.callbacks import EarlyStopping



img_height = 56
img_width = 38
batch_size = 32
data_dir = pathlib.Path("C:/Users/NebutchadnezzaR/Documents/GitHub/2022-BigDat/_lab-6/movies_posters")
genres = pd.read_csv('C:/Users/NebutchadnezzaR/Documents/GitHub/2022-BigDat/_lab-6/movies_dataset.csv')
genres_set = set(genres['genres_list'])
genres_dict = dict(zip(genres_set, range(len(genres_set))))

#все картинки засовыываются датасет, потом он перемешивается в памяти, потому что у нас небольшой размер датасетов (ага, порядка 45 тысяч файлов)
def load_imgs(data_dir=data_dir):
    image_count = len(list(data_dir.glob('*.jpg')))
    list_ds = tf.data.Dataset.list_files(str(data_dir/'*'), shuffle=False)
    list_ds = list_ds.shuffle(image_count, reshuffle_each_iteration=False)
    return list_ds, image_count


#применяю ограничения
#мы создаём датасет для обучения,
train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
        label_mode="categorical")
    #мы создаём датасет для проверки
val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
        label_mode="categorical")
    #это уже идут слои нашей нейросетки(почему такие и почему столько - предстоит узнать)
model = tf.keras.models.Sequential([
        #Полносвязный слой
        #я не хочу два ляма параметров, поэтому сейчас порежу фильтры этот был 2128
        tf.keras.layers.Conv2D(input_shape=(img_height, img_width, 3),
                filters=50, kernel_size=batch_size,
                padding='same', activation='relu', ),
        #Слой от переобучения
        tf.keras.layers.BatchNormalization(),
        #Слой свёртки
        tf.keras.layers.MaxPool2D(pool_size=2, strides=None,
                padding='valid', data_format='channels_last'),
        #Слой от переобучения
        tf.keras.layers.Dropout(0.25),

        #я не хочу два ляма параметров, поэтому сейчас порежу фильтры этот был 768
        tf.keras.layers.Conv2D(filters=10, kernel_size=batch_size,
                padding='same', activation='relu',),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPool2D(pool_size=2, strides=None,
                padding='valid', data_format='channels_last'),
        tf.keras.layers.Dropout(0.25),
        # этот был 64
        tf.keras.layers.Conv2D(filters=10, kernel_size=batch_size,
                padding='same', activation='relu',),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPool2D(pool_size=2, strides=None,
                padding='valid', data_format='channels_last'),
        
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.5),

        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(20, activation='softmax'),

        #tf.keras.layers.Dense(len(genres_set))
    ])
    # начинаем обучение модели алгоритм оптимизации Адам, функция потерь "Бинарная кроссэнтропия", метрика будет показывать долю правильных ответов модели
model.compile(optimizer='adam', loss='categorical_crossentropy',
                metrics=['accuracy'])
    # тут сложно что-то понять, вроде как в конце каждого цикла происходит сохранение весов модели...
epoch = 0
PATH = f'checkpoint_{epoch}.ckpt'
    #подключаю Early_stopping чтобы избежать переобучения
early_stopping = EarlyStopping(monitor='val_loss', patience=2)

cp_callback = tf.keras.callbacks.ModelCheckpoint(
                                filepath=PATH,
                                save_weights_only=True, # If False, saves the full model
                                save_freq='epoch')
    #выводит сводку нейрокки в терминале
model.summary()
    #требует ввода чего-нибудь перед началом обучения нейронки
input()
model.fit(train_ds,
            validation_data=val_ds,
            validation_freq=[2, 5, 9],
            epochs=9,
            callbacks=[cp_callback, early_stopping],
            use_multiprocessing=True)

test_loss, test_accuracy = model.evaluate(val_ds)
print('Test accuracy:', test_accuracy)