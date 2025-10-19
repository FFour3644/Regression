
# Step 0: Import necessary libraries
import pandas as pd
import pickle

# Step 1: Load the model from "model-reg-xxx.pkl"
with open("model-reg-xxx.pkl", "rb") as file:
    model = pickle.load(file)

# Step 2: Create a new DataFrame with the input values
new_data = pd.DataFrame({
    "youtube": [50],
    "tiktok": [50],
    "instagram": [50]
})

# Step 3: Make predictions using the loaded model
predicted_sales = model.predict(new_data)

# Print the result
print("Predicted sales:", predicted_sales[0])
