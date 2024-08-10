from tensorflow.keras.models import load_model
import numpy as np

model = load_model('trained_model.keras')

# Compile the model with the correct loss function
# model.compile(optimizer='adam', loss='mse')

x_train = np.loadtxt('x_train.txt')

y_train = np.loadtxt('y_train.txt')

scaling_factors = np.array([65, 1800, 105, 10, 450, 4.7, 1800, 17, 65, 400, 15, 365, 125, 40])

scaling_factors = scaling_factors+50

x_train = x_train / scaling_factors


print(np.round(model.predict(x_train[16].reshape(1,14)),2))
print(y_train[16])

