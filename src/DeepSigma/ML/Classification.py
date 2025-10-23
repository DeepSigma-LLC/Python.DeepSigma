from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier


class Classification:
    
    @staticmethod
    def logistic_regression(x: list[list[float]], y: list[int], c: float = 1.0, max_iter: int = 100):
        """
        Train a logistic regression model.

        :param x: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param c: Inverse of regularization strength; smaller values specify stronger regularization.
        :param max_iter: Maximum number of iterations for the solver to converge.
        :return: Trained LogisticRegression model.
        """
        model = LogisticRegression(C=c, max_iter=max_iter)
        model.fit(x, y)
        return model
    
    @staticmethod
    def support_vector_classifier(x: list[list[float]], y: list[int], kernel: str = 'rbf', c: float = 1.0):
        """
        Train a Support Vector Classifier (SVC).

        :param x: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param kernel: Specifies the kernel type to be used in the algorithm.
        :param c: Regularization parameter. The strength of the regularization is inversely proportional to c.
        :return: Trained SVC model.
        """
        model = SVC(kernel=kernel, C=c)
        model.fit(x, y)
        return model
    
    @staticmethod
    def gaussian_naive_bayes(x: list[list[float]], y: list[int]):
        """
        Train a Gaussian Naive Bayes classifier.

        :param x: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :return: Trained GaussianNB model.
        """
        model = GaussianNB()
        model.fit(x, y)
        return model
    
    @staticmethod
    def decision_tree_classifier(x: list[list[float]], y: list[int], max_depth: int = None):
        """
        Train a Decision Tree Classifier.

        :param x: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param max_depth: Maximum depth of the tree. If None, nodes are expanded until all leaves are pure.
        :return: Trained DecisionTreeClassifier model.
        """
        model = DecisionTreeClassifier(max_depth=max_depth)
        model.fit(x, y)
        return model
    
    @staticmethod
    def random_forest_classifier(x: list[list[float]], y: list[int], n_estimators: int = 100):
        """
        Train a Random Forest Classifier.

        :param x: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param n_estimators: Number of trees in the forest.
        :return: Trained RandomForestClassifier model.
        """
        model = RandomForestClassifier(n_estimators=n_estimators)
        model.fit(x, y)
        return model
    
    @staticmethod
    def gradient_boosting_classifier(x: list[list[float]], y: list[int], n_estimators: int = 100, learning_rate: float = 0.1):
        """
        Train a Gradient Boosting Classifier.

        :param x: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param n_estimators: Number of boosting stages to be run.
        :param learning_rate: Learning rate shrinks the contribution of each tree.
        :return: Trained GradientBoostingClassifier model.
        """
        model = GradientBoostingClassifier(n_estimators=n_estimators, learning_rate=learning_rate)
        model.fit(x, y)
        return model
    
    @staticmethod
    def ada_boost_classifier(x: list[list[float]], y: list[int], n_estimators: int = 50):
        """
        Train an AdaBoost Classifier.

        :param x: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param n_estimators: Number of estimators to use in the ensemble.
        :return: Trained AdaBoostClassifier model.
        """
        model = AdaBoostClassifier(n_estimators=n_estimators)
        model.fit(x, y)
        return model