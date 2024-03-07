# Comparison of Methods to Inform K-Means Clustering: A Brief Tutorial

The code created for this projected was used to create a [tutorial](https://medium.com/towards-data-science/comparison-of-methods-to-inform-k-means-clustering-a830cdc8db50) that was published in Towards Data Science.

## Description

The purpose of the project was to compare implementations of k-means clustering informed by an elbow plot and a silhouette score. Prior to conducting the comparison, an exploratory data analysis was conducted and the data were cleaned and transformed as appropriate. 

## Packages Used

The project was completed using Python 3.10 and included the following packages:

[![scikit-learn](https://img.shields.io/badge/scikit_learn-1.4.1-orange.svg)](https://scikit-learn.org/stable/) [![matplotlib](https://img.shields.io/badge/matplotlib-3.3.4-blue.svg)](https://matplotlib.org/) [![pandas](https://img.shields.io/badge/pandas-1.2.1-darkblue.svg)](https://pandas.pydata.org/) [![seaborn](https://img.shields.io/badge/seaborn-0.11.1-lightblue.svg)](https://seaborn.pydata.org/)

## Data

The data used in this project were retrieved from the University of California Irvines Machine Learning Repository. The data can be accessed through a .txt file located in the "data" folder of this repository. Additionally, the data may be accessed through the `fetch_seeds_data` function in the `data_collection.py` file. 

The original dataset was published in a study by Charytanowicz et al. (2010) [1] and contains information on the geometric properties of 210 wheat seeeds measured in millimeters. The variables in the dataset were:
- Area (A)
- Perimeter (P)
- Compactness (C), where C = $\frac{4 pi A}{P^2}$
- Length of Kernel
- Width of Kernel
- Assymmetry Coefficient
- Length of Kernerl Groove
- Seed Variety (i.e., Kama, Rosa, or Canadian)

## Structure of Repository 

```
├── data
│   ├── seed_dataset.txt
├── notebook
│   ├── kmeans_comparison.ipynb
├── Python.gitignore
├── README.md
├── data_cleaning.py
├── data_collection.py
├── data_review.py
├── evaluation.py
├── kmeans.py
├── main.py
├── pca.py
└── requirements.txt
```
## Results and Evaluation

The results of the project indicated that the implementation informed by the silhouette score performed better on the internal metrics and the elbow plot performed better on the external metric. 

## References

[1] Ch

## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
