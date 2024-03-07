# Evaluation
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score, adjusted_rand_score

def calculate_metrics(reduced_features, labels, ground_truth):
    """
    Function to calculate three metrics for clustering algortihms.

    Parameters
    ----------
    reduced_features: array-like, shape(n_samples, n_features)
        Reduced dataset from PCA
    labels: array-like, shape (n_samples,)
        Clustering labels from clustering algorithm
    ground_truth (optional): array-like, (n_samples,), optional (default=None)
        True labels of the sample, if available. Used for calculating the Adjusted Rand Index

    Returns
    ----------
    metrics: dict
        Dictionary containing Davies-Bouldin Index, Calinski-Harabasz Index, and optionally the Adjusted Rand Index
    """
    metrics = {
            'Davies-Bouldin Index': davies_bouldin_score(reduced_features, labels),
            'Calinski-Harabasz Index': calinski_harabasz_score(reduced_features, labels),
        }

    if ground_truth is not None:
        metrics['Adjusted Rand Index'] = adjusted_rand_score(ground_truth, labels)

    return metrics
