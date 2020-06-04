import tensorflow as tf
import numpy as np

def test():
    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])
    predictions = model(x_train[:1]).numpy()
    # predictions
    tf.nn.softmax(predictions).numpy()
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    loss_fn(y_train[:1], predictions).numpy()
    model.compile(optimizer='adam',
                  loss=loss_fn,
                  metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=5)
    model.evaluate(x_test, y_test, verbose=2)
    probability_model = tf.keras.Sequential([
        model,
        tf.keras.layers.Softmax()
    ])
    probability_model(x_test[:5])

def hello_world():
    graph1 = tf.Graph()
    with graph1.as_default():
        a = tf.constant([2], name='constant_a')
        b = tf.constant([3], name='constant_b')
    # Printing the value of a
    sess = tf.Session(graph=graph1)
    result = sess.run(a)
    print(result)
    sess.close()
