import pandas as pd
import tensorflow as tf

data = pd.read_csv('directions.csv')

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, 'tanh', input_shape=(2,)),
    tf.keras.layers.Dense(8, 'tanh'),
    tf.keras.layers.Dense(4, 'softmax')
])
model.compile(tf.keras.optimizers.Adam(), 'sparse_categorical_crossentropy', metrics=['accuracy'])
output = model.fit(data[['x_diff', 'y_diff']], data['direction'], epochs=200)

model.save('model.h5')