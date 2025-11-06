"""
Create a dummy model for testing the Flask app
Run this if you don't have the actual trained model yet
"""
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
import os

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Create a simple dummy model with the same input/output structure
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification: 0=Normal, 1=Pneumonia
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Save the dummy model
model.save('models/oldModel.h5')
print("Dummy model created and saved to models/oldModel.h5")
print("You can now test the Flask app!")
print("Note: This is just a dummy model - predictions will be random!")