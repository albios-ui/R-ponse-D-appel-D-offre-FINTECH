import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, MaxPooling1D, Flatten
from tensorflow.keras.optimizers import Adam

# Generate the sample data
np.random.seed(42)
num_samples = 1000
time_steps = 10

speed = np.random.randint(30, 120, size=(num_samples, time_steps))
direction = np.random.randint(0, 360, size=(num_samples, time_steps))
wheel_rotation = np.random.randint(200, 1000, size=(num_samples, time_steps))
slow_down = np.zeros(num_samples)

# Simulate the vehicle acceleration
for i in range(num_samples):
    for t in range(1, time_steps):
        if speed[i, t] > speed[i, t-1]:  # Accelerate
            speed[i, t] += np.random.randint(0, 5)
        else:  # Decelerate
            speed[i, t] -= np.random.randint(0, 5)
            if speed[i, t] < 50:  # If speed becomes too low, slow down
                slow_down[i] = 1
                break

# Reshape the data for CNN input
X = np.stack([speed, direction, wheel_rotation], axis=2)  # (num_samples, time_steps, 3)
y = slow_down

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the CNN model
model = Sequential()
model.add(Conv1D(32, kernel_size=3, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print("Test accuracy:", accuracy)
