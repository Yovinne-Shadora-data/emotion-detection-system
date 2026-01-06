import numpy as np
from tensorflow.keras.models import load_model

# Load your trained model
model = load_model("your_model.h5")  # replace with your actual model file

# Load your test data
X_test = np.load("X_test.npy")       # replace with your test features
y_test = np.load("y_test.npy")       # replace with your test labels

# Predict
y_pred_probs = model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)
y_true = np.argmax(y_test, axis=1)   # only if y_test is one-hot encoded

# Calculate accuracy
accuracy = np.mean(y_pred == y_true)
print(f"Test Accuracy: {accuracy*100:.2f}%")
