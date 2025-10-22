from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.manifold import TSNE, Isomap, LocallyLinearEmbedding


class DimensionalityReduction:
    
    @staticmethod
    def linear_discriminant_analysis(X: list[list[float]], y: list[int], n_components: int = None):
        """
        Perform Linear Discriminant Analysis (LDA) for dimensionality reduction.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param n_components: Number of components to use. If None, it defaults to the number of classes minus one.
        :return: Trained LinearDiscriminantAnalysis model.
        """
        model = LinearDiscriminantAnalysis(n_components=n_components)
        model.fit(X, y)
        return model
    
    @staticmethod
    def principal_component_analysis(X: list[list[float]], n_components: int = None):
        """
        Perform Principal Component Analysis (PCA) for dimensionality reduction.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param n_components: Number of components to keep. If None, it keeps all components.
        :return: Trained PCA model.
        """
        model = PCA(n_components=n_components)
        model.fit(X)
        return model
    
    @staticmethod
    def truncated_svd(X: list[list[float]], n_components: int = None):
        """
        Perform Truncated Singular Value Decomposition (SVD) for dimensionality reduction.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param n_components: Number of components to keep. If None, it keeps all components.
        :return: Trained TruncatedSVD model.
        """
        model = TruncatedSVD(n_components=n_components)
        model.fit(X)
        return model
    
    @staticmethod
    def tsne(X: list[list[float]], n_components: int = 2, perplexity: float = 30.0):
        """
        Perform t-Distributed Stochastic Neighbor Embedding (t-SNE) for dimensionality reduction.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param n_components: Number of dimensions to reduce to. Default is 2.
        :param perplexity: Perplexity parameter for t-SNE. Default is 30.0.
        :return: Transformed data after applying t-SNE.
        """
        model = TSNE(n_components=n_components, perplexity=perplexity)
        return model
    
    @staticmethod
    def isomap(X: list[list[float]], n_components: int = 2, n_neighbors: int = 5):
        """
        Perform Isomap for dimensionality reduction.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param n_components: Number of dimensions to reduce to. Default is 2.
        :param n_neighbors: Number of neighbors to consider for each point. Default is 5.
        :return: Transformed data after applying Isomap.
        """
        model = Isomap(n_components=n_components, n_neighbors=n_neighbors)
        return model

    @staticmethod
    def locally_linear_embedding(X: list[list[float]], n_components: int = 2, n_neighbors: int = 5):
        """
        Perform Locally Linear Embedding (LLE) for dimensionality reduction.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param n_components: Number of dimensions to reduce to. Default is 2.
        :param n_neighbors: Number of neighbors to consider for each point. Default is 5.
        :return: Transformed data after applying LLE.
        """
        model = LocallyLinearEmbedding(n_components=n_components, n_neighbors=n_neighbors)
        return model