# predicting-gas-production
Predicting the cumulative twelve month gas production from a set of US gas wells


## Project structure

```
├── requirements.txt
├── model_card.md
├── main.py
├── data
│   └── bank_data.csv
├── notebooks
│   └── ydataprofiling.ipynb
│   └── eda.ipynb
│   └── modeling.ipynb
├── images
│   ├── eda
│   │   └── histograms
│   │   └── bar_plots
│   │   └── heatmaps
│   └── results
│       └── feature_importance.png
│       └── feature_importance.png
├── logs
│   └── main.log
├── models
│   └── inference_pipeline.pkl
└── README.md
```

## Install requirements
This instructions assume you're already have installed python (3.9)
- Create virtualenv with venv
```
pip install -r requirements.txt
```
- Install requirements for developing the solution
```
pip install -r requirements.txt
```


## Assumptions and constraints
- The production model assumes that there'll not be new or removed treatment companies and operators
- The date of extraction for training data is assumed to be 15/2/2024
- Inductive Conformal Prediction (ICP) will be used for modelling. 

"Like all other models from the conformal prediction family, ICP is model-agnostic in terms of the underlying point prediction model and data distribution and comes with automatic validity guarantees for final samples of any size."

"The ICP process involves splitting the dataset into a proper training set and a calibration set. The training set is used to create the initial point prediction model, while the calibration set is utilized to calculate conformity scores and produce the prediction intervals of the unseen points."

"ICP’s efficiency and flexibility have made it a popular choice for uncertainty estimation in various applications."