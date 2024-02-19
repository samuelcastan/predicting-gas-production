import pickle
import json
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

NUM_FEATURES = ["year_on_production", "md_ft", "proppant_volume", "total_number_of_stages", "azimuth", "isip", "porosity", "proppant_fluid_ratio", "pump_rate", "tvd_ft"]
CAT_FEATURES = ["treatment_company", "operator"]

# Load the saved sklearn pipeline
with open('models/inference_pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

# Load quantile error information from JSON file
with open('models/q_yhat_calib.json', 'r') as f:
    q_calib = json.load(f)

# New data for prediction
new_data = pd.read_csv("data/test_inference/data.csv")

new_data = new_data[NUM_FEATURES + CAT_FEATURES]

print(type(pipeline))

# Make prediction
# prediction = pipeline.predict(new_data)

# # Calculate prediction interval using quantile errors
# lower_quantile = 0.1  # Example: 10th percentile
# upper_quantile = 0.9  # Example: 90th percentile

# # Assuming quantile_errors is a dictionary where keys are quantiles and values are errors
# lower_error = quantile_errors.get(str(lower_quantile), 0)  # If quantile not found, assume 0 error
# upper_error = quantile_errors.get(str(upper_quantile), 0)  # If quantile not found, assume 0 error

# lower_bound = prediction - lower_error
# upper_bound = prediction + upper_error

# print("Prediction:", prediction)
# print("Prediction Interval:")
# print("Lower Bound:", lower_bound)
# print("Upper Bound:", upper_bound)
