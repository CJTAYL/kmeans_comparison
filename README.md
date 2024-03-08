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
├── seeds_EDA.ipynb
└── requirements.txt
```

## Results and Evaluation

The metrics used to compare the implementations of k-means clustering include internal metrics (e.g., Davies-Bouldin, Calinski-Harabasz) which do not include ground truth labels and external metrics (e.g., Adjusted Rand Index) which do include external metrics. A brief description of the three metrics is provided below.

- Davies-Bouldin Index (DBI): The DBI captures the trade-off between cluster compactness and the distance between clusters. Lower values of DBI indicate there are tighter clusters with more separation between clusters [2].
- Calinski-Harabasz Index (CHI): The CHI measures cluster density and distance between clusters. Higher values indicate that clusters are dense and well-separated [3].
- Adjusted Rand Index (ARI): The ARI measures agreement between cluster labels and ground truth. The values of the ARI range from -1 to 1. A score of 1 indicates perfect agreement between labels and ground truth; a scores of 0 indicates random assignments; and a score of -1 indicates worse than random assignment [4].

When comparing the two implementations, k-means informed by the silhouette score performed best on the two internal metrics, indicating more compact and separated clusters. However, k-means informed by the elbow plot performed best on the external metric (i.e., ARI) which indicating better alignment with the ground truth labels. 

Ultimately, the best performing implementation will be determined by the task. If the task requires clusters that are cohesive and well-separated, then internal metrics (e.g., DBI, CHI) might be more relevant. If the task requires the clusters to align with the ground truth labels, then external metrics, like the ARI, may be more relevant.

## References

[1] Charytanowicz, M., Niewczas, J., Kulczycki, P., Kowalski, P.A., Łukasik, S., & Zak, S. (2010). Complete Gradient Clustering Algorithm for Features Analysis of X-Ray Images.

[2] D. L. Davies, D.W. Bouldin, A Cluster Separation Measure (1979), IEEE Transactions on Pattern Analysis and Machine Intelligence https://doi:10.1109/TPAMI.1979.4766909

[3] T. Caliński, J. Harabasz, A Dendrite Method for Cluster Analysis (1974) Communications in Statistics https://doi:10.1080/03610927408827101

[4] N. X. Vinh, J. Epps, J. Bailey, Information Theoretic Measures for Clusterings Comparison: Variants, Properties, Normalization and Correction for Chance (2010), Journal of Machine Learning Research https://www.jmlr.org/papers/volume11/vinh10a/vinh10a.pdf


## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
