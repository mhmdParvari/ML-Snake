import pandas as pd
import tensorflow as tf

data = pd.read_csv('directions.csv')

data = data.sample(frac=1)
cut = round(len(data) * .85)
x_train = data[['x_diff', 'y_diff']][ :cut]
y_train = data['direction'][ :cut]
x_test = data[['x_diff', 'y_diff']][cut: ]
y_test = data['direction'][cut: ]

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, 'tanh', input_shape=(2,)),
    tf.keras.layers.Dense(8, 'tanh'),
    tf.keras.layers.Dense(4, 'softmax')
])
model.compile(tf.keras.optimizers.Adam(), 'sparse_categorical_crossentropy', metrics=['accuracy'])
output = model.fit(x_train, y_train, epochs=200)

print('evaluate:')
print(model.evaluate(x_test, y_test))

model.save('model.h5')