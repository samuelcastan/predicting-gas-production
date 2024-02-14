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