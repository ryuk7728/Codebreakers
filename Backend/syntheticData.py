import numpy as np

# Define the thresholds and probabilities
parameters = [
    {"name": "Engine Oil Pressure", "low": 25, "high": 65, "prob_failure": 1.0},
    {"name": "Engine Speed", "low": 0, "high": 1800, "prob_failure": 0.5},
    {"name": "Engine Temperature", "low": 0, "high": 105, "prob_failure": 1.0},
    {"name": "Brake Control", "low": 1, "high": 10, "prob_failure": 0.5},
    {"name": "Transmission Pressure", "low": 200, "high": 450, "prob_failure": 0.5},
    {"name": "Pedal Sensor", "low": 0, "high": 4.7, "prob_failure": 0.2},
    {"name": "Water Fuel", "low": 0, "high": 1800, "prob_failure": 1.0},
    {"name": "Fuel Level", "low": 1, "high": 17, "prob_failure": 0.2},
    {"name": "Fuel Pressure", "low": 35, "high": 65, "prob_failure": 0.2},
    {"name": "Fuel Temperature", "low": 0, "high": 400, "prob_failure": 1.0},
    {"name": "System Voltage", "low": 12.0, "high": 15.0, "prob_failure": 1.0},
    {"name": "Exhaust Gas Temperature", "low": 0, "high": 365, "prob_failure": 1.0},
    {"name": "Hydraulic Pump Rate", "low": 0, "high": 125, "prob_failure": 0.5},
    {"name": "Air Filter Pressure Drop", "low": 20, "high": 40, "prob_failure": 0.5},
]

def generate_value(low, high):
        # Randomly decide whether the value is within or outside the range
        if np.random.rand() > 0.05:
            return max(np.random.uniform(low, high), 0)  # within range, ensure no negative values
        else:
            # Decide whether the value is below or above the range
            if np.random.rand() > 0.5 or low<10:
                return max(np.random.uniform(high + 1, high + 50), 0)  # above range, ensure no negative values
            else:
                return max(np.random.uniform(low - 10, low - 1), 0)  # below range, ensure no negative values

def generate_synthetic_data(num_samples):
    x_train = np.zeros((num_samples, len(parameters)))
    y_train = np.zeros((num_samples, len(parameters)))

    for i in range(num_samples):
        for j, param in enumerate(parameters):
            value = generate_value(param['low'], param['high'])
            x_train[i, j] = value
            # Check if the value is within the range
            if (value >= param['low']) and (value <= param['high']):
                y_train[i, j] = 0
            else:
                y_train[i, j] = param['prob_failure']

    return x_train, y_train


# Example usage
num_samples = 100000
x_train, y_train = generate_synthetic_data(num_samples)

np.savetxt('x_test.txt', x_train)

np.savetxt('y_test.txt', y_train)

print("X_train eg:", x_train[3])
print("Y_train eg:", y_train[3])


