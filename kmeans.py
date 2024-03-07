# kmeans
import pandas as pd
from sklearn.cluster import KMeans

def implement_kmeans(k, reduced_features, df):
    """
    Function to implement KMeans

    Parameters
    ----------
    k: Number of clusters
    reduced_features: Dataframe of principal components
    df: Dataframe of the original data

    Returns
    ----------
    sorted_assignments: Cluster assignments sorted by cluster
    """
    kmeans = KMeans(n_clusters=k, random_state=24, n_init='auto')
    clusters = kmeans.fit_predict(reduced_features)
    cluster_assignments = pd.DataFrame({'seed': df.index, 'cluster': clusters})
    # Sort value by cluster
    sorted_assignments = cluster_assignments.sort_values(by='cluster')
    # Convert assignments to same scale as 'variety'
    sorted_assignments['cluster'] = [num + 1 for num in sorted_assignments['cluster']]
    # Convert 'cluster' to categorical variables
    sorted_assignments['cluster'] = sorted_assignments['cluster'].astype('category')
    return sorted_assignments


def get_centroids(k, reduced_features):
    """
    Function to calculate cluster centers or centroids

    Parameters
    ----------
    k: Number of clusters
    reduced_features: Dataframe of principal components

    Returns
    ----------
    centroids: Centers of clusters
    """
    kmeans = KMeans(n_clusters=k, random_state=24, n_init='auto')
    clusters = kmeans.fit_predict(reduced_features)
    centroids = kmeans.cluster_centers_
    return('Centroids: \n', centroids)


def get_labels(k, reduced_features):
    """
    Function to retrieve labels

    Parameters
    ----------
    k: Number of clusters
    reduced_features: Dataframe of principal components

    Returns
    ----------
    labels: Label of each point
    """
    kmeans = KMeans(n_clusters=k, random_state=24, n_init='auto')
    clusters = kmeans.fit_predict(reduced_features)
    labels = kmeans.labels_
    return labels
