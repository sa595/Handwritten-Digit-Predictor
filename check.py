import pickle
import numpy as np
# from knn_model import CustomKNN  # Crucial: Python needs the class definition to unpack it

# 1. Load the model back from disk
with open('knn_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

print("Model loaded perfectly into memory!")

# 2. Run a quick dummy test prediction to verify functionality
dummy_pixel_array = np.zeros((1, 784)) # Empty canvas test
prediction = loaded_model.predict(dummy_pixel_array)
print("Test prediction output:", prediction)