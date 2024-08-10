import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from tensorflow.keras.losses import MeanAbsoluteError


# Load the synthetic data
x_train = np.loadtxt('x_train.txt')
y_train = np.loadtxt('y_train.txt')

y_train = y_train

scaling_factors = np.array([65, 1800, 105, 10, 450, 4.7, 1800, 17, 65, 400, 15, 365, 125, 40])

scaling_factors = scaling_factors+50
print(scaling_factors)
# Scale x_train by dividing each column by the corresponding scaling factor
x_train = x_train / scaling_factors



# Define the model
model = Sequential([
    Dense(units=1000, activation='relu'),  # Hidden layer with 1000 neurons
    Dense(units=14, activation='relu')  # Output layer with 14 neurons
])

# learning_rate = 0.005  # Adjust the learning rate as needed
# adam_optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

# Compile the model
model.compile(optimizer='adam', loss='mse')


# Train the model
model.fit(x_train, y_train, epochs=100)

print(np.round(model.predict(x_train[0:3]),2))

print(y_train[0:3])

model.save('trained_model.keras')