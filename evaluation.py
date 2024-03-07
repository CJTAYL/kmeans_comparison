# Evaluation
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score, adjusted_rand_score

def calculate_metrics(reduced_features, labels, ground_truth):
    metrics = {
        'Davies-Bouldin Index': davies_bouldin_score(reduced_features, labels),
        'Calinski-Harabasz Index': calinski_harabasz_score(reduced_features, labels),
        'Adjusted Rand Index': adjusted_rand_score(ground_truth, labels)
                }
    return metrics
