from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering


class Clustering:

    @staticmethod
    def kmeans(x: list[list[float]], n_clusters: int):
        """
        k-means clustering is a clustering algorithm that uses the Euclidean distance to find clusters.
        It is a type of unsupervised learning algorithm.
        :param x: Features, a list of lists where each inner list is a feature vector.
        :param n_clusters: Number of clusters to form.
        """
        model = KMeans(n_clusters=n_clusters)
        model.fit(x)
        return model

    @staticmethod
    def dbscan(x: list[list[float]], eps: float, min_samples: int):
        """
        DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a clustering algorithm.
        :param x: Features, a list of lists where each inner list is a feature vector.
        :param eps: The maximum distance between two samples for one to be considered as in the neighborhood of the other.
        :param min_samples: The number of samples (or total weight) in a neighborhood for a point to be considered as a core point.
        :return: Trained DBSCAN model.
        """
        model = DBSCAN(eps=eps, min_samples=min_samples)
        model.fit(x)
        return model

    @staticmethod
    def agglomerative_clustering(x: list[list[float]], n_clusters: int):
        """
        Agglomerative Clustering (AGGC) is a hierarchical clustering algorithm.
        It starts with each observation as a separate cluster and merges pairs of clusters.
        The merge is based on the distance between the clusters.

        :param x: Features, a list of lists where each inner list is a feature vector.
        :param n_clusters: Number of clusters to form.
        """
        model = AgglomerativeClustering(n_clusters=n_clusters)
        model.fit(x)
        return model
    
    @staticmethod
    def k_neighbors_classifier(x: list[list[float]], y: list[int], n_neighbors: int):
        """
        K-Nearest Neighbors Classifier (KNNC) is a supervised learning algorithm that uses the
        distance between each point and its neighbors to predict the class of the target variable.

        :param x: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param n_neighbors: Number of neighbors to use.
        :return: Trained KNeighborsClassifier model.
        """
        model = KNeighborsClassifier(n_neighbors=n_neighbors)
        model.fit(x, y)
        return model
    
    @staticmethod
    def k_neighbors_regressor(x: list[list[float]], y: list[float], n_neighbors: int):
        """
        K-Nearest Neighbors Regressor (KNNR) is a supervised learning algorithm that uses the
        distance between each point and its neighbors to predict the value of the target variable.
        It is a non-parametric regression algorithm that can be used for both classification and regression.
        Non-parametric algorithms are another type of machine learning algorithms that do not use parameters,
        but instead use the data itself.

        :param x: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param n_neighbors: Number of neighbors to use.
        :return: Trained KNeighborsRegressor model.
        """
        model = KNeighborsRegressor(n_neighbors=n_neighbors)
        model.fit(x, y)
        return model