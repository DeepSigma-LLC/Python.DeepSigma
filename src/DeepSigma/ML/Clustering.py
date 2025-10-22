from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering


class Clustering:

    @staticmethod
    def kmeans(X: list[list[float]], n_clusters: int):
        model = KMeans(n_clusters=n_clusters)
        model.fit(X)
        return model

    @staticmethod
    def dbscan(X: list[list[float]], eps: float, min_samples: int):
        model = DBSCAN(eps=eps, min_samples=min_samples)
        model.fit(X)
        return model

    @staticmethod
    def agglomerative_clustering(X: list[list[float]], n_clusters: int):
        model = AgglomerativeClustering(n_clusters=n_clusters)
        model.fit(X)
        return model
    
    @staticmethod
    def k_neighbors_classifier(X: list[list[float]], y: list[int], n_neighbors: int):
        model = KNeighborsClassifier(n_neighbors=n_neighbors)
        model.fit(X, y)
        return model
    
    @staticmethod
    def k_neighbors_regressor(X: list[list[float]], y: list[float], n_neighbors: int):
        model = KNeighborsRegressor(n_neighbors=n_neighbors)
        model.fit(X, y)
        return model