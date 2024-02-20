from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Conv2D, BatchNormalization, ReLU, AveragePooling2D, Dropout, Flatten, Dense

# Define the network
model = Sequential([
    InputLayer(input_shape=image_size),
    Conv2D(10, (8, 8), padding='same'),
    BatchNormalization(),
    ReLU(),
    AveragePooling2D(pool_size=(2, 2), strides=2),
    Conv2D(12, (16, 16), padding='same'),
    BatchNormalization(),
    ReLU(),
    AveragePooling2D(pool_size=(2, 2), strides=2),
    Conv2D(12, (32, 32), padding='same'),
    BatchNormalization(),
    ReLU(),
    AveragePooling2D(pool_size=(2, 2), strides=2),
    Conv2D(12, (32, 32), padding='same'),
    BatchNormalization(),
    ReLU(),
    AveragePooling2D(pool_size=(2, 2), strides=2),
    Conv2D(20, (32, 32), padding='same'),
    BatchNormalization(),
    ReLU(),
    Dropout(0.04),
    Flatten(),
    Dense(1, kernel_regularizer='l2'),  # Add L2 regularization to mimic 'WeightL2Factor' in MATLAB
])

# Compile the model
model.compile(optimizer='rmsprop', loss='mean_squared_error', metrics=['mse'])

# Display the model summary
model.summary()
