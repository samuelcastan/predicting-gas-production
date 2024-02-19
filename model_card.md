# Model Card: Regression Model

## Model Details
- **Model Version:** 1.0.0
- **Model Type:** Regression
- **Model Architecture:** Random Forest
- **Model Hyperparametrs:** Refer to [hyperparameters](results/quick_modeling/hyperparameters.json) file.
- **Metrics:** Because of time, R-squared was used for evaluating the model. More so, conformal prediction was used to obtain prediciton intervals with a 95% coverage.

## Model Performance

- **Performance on Training Data:**
  - R-squared (R2): 0.63
- **Performance on Test Data:**
  - R-squared (R2): 0.68

## Model Description
[Provide a brief description of the model, including its purpose, features used, and any specific characteristics.]

## Intended Use
[Describe the intended use cases for the model, including any limitations or constraints on its use.]

## Caveats and Known Limitations
- "Sufficient" model to start experimenting, but there's still a ton of room to improve performance.
- It is designed to only be used within the corresponding treatment companies and operators
- If needed, treatment company and operator could be removed if wanted to implement solution on a broader aspect.

## Responsible AI Considerations
Beware that this model is intended to be used on the treatment companies and operators. Model might be biased on giving more weight to a specific operator and/or company

## Authors
- Samuel David Castán Alejandre
- samuel.castan96@gmail.com

## Special thanks
- Conformal Prediction development was inspired on Valery Manokhin's book - Practical Guide to Applied Conformal Prediction in Python: Learn and apply the best uncertainty frameworks to your industry applications