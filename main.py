# Main script
from data_collection import fetch_seeds_data
from data_review import get_info, get_statistics
from data_cleaning import separate_ground_truth, scale_data
from pca import conduct_pca
from kmeans import implement_kmeans, get_centroids, get_labels
from evaluation import calculate_metrics

def main():
    data = fetch_seeds_data()
    # Info about dataframe and features
    get_info(data)
    get_statistics(data)
    ground_truth = separate_ground_truth(data)
    clean_data = scale_data(data)
    reduced_features = conduct_pca(0.95, clean_data)

    # Implementation using elbow plot
    ep_assignments = implement_kmeans(3, reduced_features, data)
    ep_centroids = get_centroids(3, reduced_features)
    ep_labels = get_labels(3, reduced_features)
    ep_metrics = calculate_metrics(reduced_features, ep_labels, ground_truth)

    # Implementation using silhouette score
    ss_assignments = implement_kmeans(2, reduced_features, data)
    ss_centroids = get_centroids(2, reduced_features)
    ss_labels = get_labels(2, reduced_features)
    ss_metrics = calculate_metrics(reduced_features, ss_labels, ground_truth)

    print('Elbow Plot Metrics')
    print('----------')
    print(ep_metrics)
    print()

    print('Silhouette Score Metrics')
    print('----------')
    print(ss_metrics)
    print()


if __name__ == "__main__":
    main()
