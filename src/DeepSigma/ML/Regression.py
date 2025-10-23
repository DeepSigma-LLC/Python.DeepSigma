from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.svm import SVR


class Regression:

    @staticmethod
    def linear_regression(x: list[float], y: list[float]):
        """
        Linear Regression is a simple linear regression algorithm.
        It is used for predicting continuous values.

        :param x: Features, a list of floats representing feature values.
        :param y: Labels, a list of floats representing label values.
        """
        model = LinearRegression()
        model.fit(x, y)
        return model
    
    @staticmethod
    def ridge_regression(x: list[float], y: list[float], alpha: float = 1.0):
        """
        Ridge Regression is a linear regression algorithm that adds a penalty term to the loss function.
        It is used for predicting continuous values. It is a regularized version of Linear Regression.
        :param x: Features, a list of floats representing feature values.
        :param y: Labels, a list of floats representing label values.
        :param alpha: Regularization strength. Larger values specify stronger regularization.
        return: Trained Ridge model.
        """
        model = Ridge(alpha=alpha)
        model.fit(x, y)
        return model
    
    @staticmethod
    def lasso_regression(x: list[float], y: list[float], alpha: float = 1.0):
        """
        Lasso Regression is a linear regression algorithm that adds a penalty term to the loss function.
        It is used for predicting continuous values. It is a regularized version of Linear Regression.
        :param x: Features, a list of floats representing feature values.
        :param y: Labels, a list of floats representing label values.
        :param alpha: Regularization strength. Larger values specify stronger regularization.
        return: Trained Lasso model.
        """
        model = Lasso(alpha=alpha)
        model.fit(x, y)
        return model
    
    @staticmethod
    def polynomial_regression(x: list[float], y: list[float], degree: int = 2):
        """
        Polynomial Regression is a linear regression algorithm that fits a polynomial to the data.
        It is used for predicting continuous values.
        :param x: Features, a list of floats representing feature values.
        :param y: Labels, a list of floats representing label values.
        :param degree: Degree of the polynomial.
        return: Trained PolynomialRegression model.
        """
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        model.fit(x, y)
        return model
    
    @staticmethod
    def decision_tree_regression(x: list[float], y: list[float], max_depth: int = None):
        """
        Decision Tree Regression is a supervised learning algorithm that uses the distance between each point and
        its neighbors to predict the value of the target variable.
        It is a non-parametric regression algorithm that can be used for both classification and regression.
        :param x: Features, a list of floats representing feature values.
        :param y: Labels, a list of floats representing label values.
        :param max_depth: Maximum depth of the tree. If None, nodes are expanded until all leaves are pure.
        return: Trained DecisionTreeRegressor model.
        """
        model = DecisionTreeRegressor(max_depth=max_depth)
        model.fit(x, y)
        return model
    
    @staticmethod
    def random_forest_regression(x: list[float], y: list[float], n_estimators: int = 100):
        """
        Random Forest Regression is a supervised learning algorithm that combines multiple decision trees.
        It is a non-parametric regression algorithm that can be used for both classification and regression.
        It is an ensemble learning algorithm that combines multiple decision trees.
        :param x: Features, a list of floats representing feature values.
        :param y: Labels, a list of floats representing label values.
        :param n_estimators: Number of trees in the forest.
        return: Trained RandomForestRegressor model.
        """
        model = RandomForestRegressor(n_estimators=n_estimators)
        model.fit(x, y)
        return model
    
    @staticmethod
    def gradient_boosting_regression(x: list[float], y: list[float], n_estimators: int = 100, learning_rate: float = 0.1):
        model = GradientBoostingRegressor(n_estimators=n_estimators, learning_rate=learning_rate)
        model.fit(x, y)
        return model
    
    @staticmethod
    def ada_boost_regression(x: list[float], y: list[float], n_estimators: int = 50):
        model = AdaBoostRegressor(n_estimators=n_estimators)
        model.fit(x, y)
        return model
    
    @staticmethod
    def support_vector_regression(x: list[float], y: list[float], kernel: str = 'rbf', c: float = 1.0, epsilon: float = 0.1):
        model = SVR(kernel=kernel, C=c, epsilon=epsilon)
        model.fit(x, y)
        return model
    
