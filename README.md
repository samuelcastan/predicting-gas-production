# predicting-gas-production
Predicting the cumulative twelve month gas production from a set of US gas wells

## Project structure

```
├── data
│   └── raw
│   └── clean
│   └── test_inference
├── models
│   └── q_yhat_calib.json
│   └── inference_pipeline.pkl
├── notebooks
│   └── basic_cleaning.ipynb
│   └── conformal_prediction.ipynb
│   └── eda.ipynb
│   └── quick_modeling.ipynb
├── results
│   ├── conformal_prediction
│   │   └── coverage.csv
│   │   └── actual_vs_predicted_with_interval.png
│   ├── eda
│   │   └── boxplots
│   │   └── countplots
│   │   └── histograms
│   │   └── missing_values
│   │   └── scatterplots
│   └── quick_modeling
│       └── features_importances.csv
│       └── grid_search_cv.csv
│       └── hyperparameters.json
├── test_pipeline.ipynb
├── developmemt_conclusions.md
├── model_card.md
└── README.md
├── requirements.txt
```
## Main files:
- requirements: Contains the library dependencies that the entire project uses.
- basic_cleaning.ipynb: Clean data appropiately for analysis.
- eda.ipynb: Obtain insights of features and target variable.
- quick_modeling.ipynb: Feature processing and enginering, hyperparameter tuning, and more.
- conformal_prediction: Apply conformal prediction to winner model to obtain prediction intervals.
- test_pipeline.ipynb: Test saved pipeline file with a single instance of data: Apply conformal prediction.

Input files:
- data: where the source data lives (the code is written to read a .csv file).

Output directories:
- results: Here it is stored all the EDA visualizations (countplost, histograms, scatterplots), model training and evaluation results.
- models: Here are the pickled pipeline and conformalized quantile value stored.

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

## Pending things to do (but not limited) and improve on next iterations
- Validate normality of residuals, presence of heteroscedasticity and other regression validations.
- Add feature domains for data validation when inferecing on new data.
- Modularize code using config file.
- Configure and add log files.
- Create src folder and move to python script instead of notebooks. they are good for development but not for production.
- Depending on productionization of solution, deploy model as an API or batch inference.
- Implement monitoring, retraining and redeployment.
- CI/CD
- Version artifacts and add remote storage.

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
- Inductive Conformal Prediction (ICP) will be used for modelling.
- The ICP process involves splitting the dataset into a proper training set and a calibration set. The training set is used to create the initial point prediction model, while the calibration set is utilized to calculate conformity scores and produce the prediction intervals of the unseen points."

