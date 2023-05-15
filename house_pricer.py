'''After splitting the data into training and testing sets, we train an XGBoost regression model using the XGBRegressor class from the xgboost library. XGBoost is a popular gradient boosting algorithm known for its excellent predictive performance.

We then generate a new instance with simulated values for all the factors, including the average heights of commercial and residential buildings, and use the trained model to predict the housing price for that instance.

Finally, we evaluate the model's performance on the test set by calculating the mean squared error (MSE) between the predicted housing prices and the actual housing prices.

Please note that this is a simplified example, and in a real-world scenario, you would need to perform additional steps such as hyperparameter tuning, cross-validation, and further data preprocessing to optimize the model's performance.'''

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Simulated data in CSV format
data = pd.DataFrame({
    'Distance_to_airport': np.random.uniform(0, 10, 100),  # Simulated distance to airport
    'Noise_level': np.random.uniform(0, 100, 100),  # Simulated noise level
    'Convenience_score': np.random.uniform(0, 5, 100),  # Simulated convenience score
    'Employment_opportunities': np.random.uniform(0, 10, 100),  # Simulated employment opportunities
    'Air_quality_index': np.random.uniform(0, 100, 100),  # Simulated air quality index
    'Average_height_commercial': np.random.uniform(1, 10, 100),  # Simulated average height of commercial buildings
    'Average_height_residential': np.random.uniform(1, 10, 100),  # Simulated average height of residential buildings
    'Housing_price': np.random.uniform(100000, 500000, 100)  # Simulated housing prices
})

# Split the data into features (X) and target variable (y)
X = data.drop('Housing_price', axis=1)
y = data['Housing_price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an XGBoost regression model
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# Generate a new instance with simulated factors
new_instance = pd.DataFrame({
    'Distance_to_airport': [5.2],
    'Noise_level': [75.8],
    'Convenience_score': [3.2],
    'Employment_opportunities': [7.6],
    'Air_quality_index': [65.4],
    'Average_height_commercial': [8.5],
    'Average_height_residential': [4.2]
})

# Predict housing price for the new instance
predicted_price = model.predict(new_instance)

print('Predicted housing price:', predicted_price)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)
