# Model Card: Regression Model

## Model Details
- **Model Version:** 1.0.0
- **Model Type:** Regression
- **Model Architecture:** Random Forest
- **Model Hyperparameters:** Refer to the [hyperparameters](results/quick_modeling/hyperparameters.json) file.
- **Metrics:** Due to time constraints, R-squared was used for evaluating the model's performance. Additionally, conformal prediction was utilized to obtain prediction intervals with a 95% coverage.

## Model Performance

- **Performance on Training Data:**
  - R-squared (R2): 0.63
- **Performance on Test Data:**
  - R-squared (R2): 0.68

## Intended Use
This model aims to estimate the 12-month cumulative gas production (mmcf) of wells in the US given certain treatment companies, operators, and other measured characteristics of the reservoir.

## Caveats and Known Limitations
- This model is considered "sufficient" to begin experimentation, but there remains ample room for improvement in performance.
- It is designed for use only within the corresponding treatment companies and operators.
- If necessary, the treatment company and operator could be removed for implementation in a broader context.

## Responsible AI Considerations
It's important to note that this model is intended for use within specific treatment companies and operators. There's a risk of bias, as the model may give more weight to specific operators or companies.

## Authors
- Samuel David Castán Alejandre
- samuel.castan96@gmail.com

## Special Thanks
- The development of Conformal Prediction was inspired by Valery Manokhin's book - "Practical Guide to Applied Conformal Prediction in Python: Learn and apply the best uncertainty frameworks to your industry applications".
