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


## Columns Description
- **treatment company**: The treatment company who provides treatment service.
- **azimuth**: Well drilling direction.
- **md (ft)**: Measure depth.
- **tvd (ft)**: True vertical depth.
- **date on production**: First production date.
- **operator**: The well operator who performs drilling service.
- **footage lateral length**: Horizontal well section.
- **well spacing**: Distance to the closest nearby well.
- **porpoise deviation**: How much max (in ft.) a well deviated from its horizontal.
- **porpoise count**: How many times the deviations (porpoises) occurred.
- **shale footage**: How much shale (in ft) encountered in a horizontal well.
- **acoustic impedance**: The impedance of a reservoir rock (ft/s * g/cc).
- **log permeability**: The property of rocks that is an indication of the ability for fluids (gas or liquid) to flow through rocks
- **porosity**: The percentage of void space in a rock. It is defined as the ratio of the volume of the voids or pore space divided by the total volume. It is written as either a decimal fraction between 0 and 1 or as a percentage.
- **poisson ratio**: Measures the ratio of lateral strain to axial strain at linearly elastic region.
- **water saturation**: The ratio of water volume to pore volume.
- **toc**: Total Organic Carbon, indicates the organic richness (hydrocarbon generative potential) of a reservoir rock.
- **vcl**: The amount of clay minerals in a reservoir rock.
- **p-velocity**: The velocity of P-waves (compressional waves) through a reservoir rock (ft/s).
- **s-velocity**: The velocity of S-waves (shear waves) through a reservoir rock (ft/s).
- **youngs modulus**: The ratio of the applied stress to the fractional extension (or shortening) of the reservoir rock parallel to the tension (or compression) (giga pascals).
- **isip**: When the pumps are quickly stopped, and the fluids stop moving, these friction pressures disappear and the resulting pressure is called the instantaneous shut-in pressure, ISIP.
- **breakdown pressure**: The pressure at which a hydraulic fracture is created/initiated/induced.
- **pump rate**: The volume of liquid that travels through the pump in a given time. A hydraulic fracture is formed by pumping fluid into a wellbore at a rate sufficient to increase pressure at the target depth, to exceed that of the fracture gradient (pressure gradient) of the rock.
- **total number of stages**: Total stages used to fracture the horizontal section of the well.
- **proppant volume**: The amount of proppant in pounds used in the completion of a well (lbs).
- **proppant fluid ratio**: The ratio of proppant volume/fluid volume (lbs/gallon).
- **production**: The 12 months cumulative gas production (mmcf).

## Assumptions and constraints
- The production model assumes that there'll not be new or removed treatment companies and operators
- The date of extraction for training data is assumed to be 15/2/2024
- Inductive Conformal Prediction (ICP) will be used for modelling. 

"Like all other models from the conformal prediction family, ICP is model-agnostic in terms of the underlying point prediction model and data distribution and comes with automatic validity guarantees for final samples of any size."

"The ICP process involves splitting the dataset into a proper training set and a calibration set. The training set is used to create the initial point prediction model, while the calibration set is utilized to calculate conformity scores and produce the prediction intervals of the unseen points."

"ICP’s efficiency and flexibility have made it a popular choice for uncertainty estimation in various applications."


- PENDING TO ADD FEATURE DOMAINS FOR DATA VALIDATION WHEN INFERECING ON NEW DATA
- PENDING TO VALIDATE NORMALITY OF RESIDUALS, PRESENCE OF HETEROSCEDASTICITY 