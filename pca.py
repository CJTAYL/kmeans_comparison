# PCA
import numpy as np
from sklearn.decomposition import PCA

def conduct_pca(var, df_scaled):
    """
    Function to conduct PCA

    Parameters
    ----------
    var: float
        Percentage of variance
    df: dataframe
        Scaled dataframe

    Returns
    ----------
    reduced_features: dataframe
        Dataframe containing the principal components
    """
    pca = PCA(n_components=var)
    reduced_features = pca.fit_transform(df_scaled)
    return reduced_features
