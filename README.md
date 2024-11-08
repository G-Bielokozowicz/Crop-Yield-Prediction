# Crop Yield Prediction

## Data Frame

| Column Name     | Description                                  |
|-----------------|----------------------------------------------|
| Rain Fall (mm)  | Rainfall in millimeters                      |
| Temperature (C) | Temperature in Celsius                       |
| Fertilizer (kg) | Fertilizer in kilograms                      |
| Nitrogen (N)    | Nitrogen macro nutrient                      |
| Phosphorous (P) | Phosphorous macro nutrient                   |
| Potassium (K)   | Potassium macro nutrient                     |
| Yield (Q/acres) | Crop yield Quintals per acre                 |

## Data cleanup
Two columns had typos in the name and were renamed. Missing values changed to a median of their respective colmuns.

## Exploratory Data Analysis (EDA)
The dataset probably represents two different crops, based on graphs of the rainfall, temperature and crop yield. 
![obraz](https://github.com/user-attachments/assets/4d28b0d4-3e27-4b71-82c0-d7ba75c8967d)

Usage of fertilizer is proportional to the crop yield. Rain fall and temperature each show two clusters, again indicating two different crops.
![obraz](https://github.com/user-attachments/assets/f38370e7-cd7d-4e83-9dec-36562126ffb3)

## Model and evaluation
In this project random forest regression was used, with GridSearch to find the best parameters. It achieved accuracy of 93%, with the most important features being rainfall, followed by temperature. 

![obraz](https://github.com/user-attachments/assets/3da86153-9959-44fa-ba84-d906b2a55b2b)
