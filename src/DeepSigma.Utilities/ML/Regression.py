from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.svm import SVR


class Regression:

    @staticmethod
    def linear_regression(X: list[float], y: list[float]):
        model = LinearRegression()
        model.fit(X, y)
        return model
    
    @staticmethod
    def ridge_regression(X: list[float], y: list[float], alpha: float = 1.0):
        model = Ridge(alpha=alpha)
        model.fit(X, y)
        return model
    
    @staticmethod
    def lasso_regression(X: list[float], y: list[float], alpha: float = 1.0):
        model = Lasso(alpha=alpha)
        model.fit(X, y)
        return model
    
    @staticmethod
    def polynomial_regression(X: list[float], y: list[float], degree: int = 2):
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        model.fit(X, y)
        return model
    
    @staticmethod
    def decision_tree_regression(X: list[float], y: list[float], max_depth: int = None):
        model = DecisionTreeRegressor(max_depth=max_depth)
        model.fit(X, y)
        return model
    
    @staticmethod
    def random_forest_regression(X: list[float], y: list[float], n_estimators: int = 100):
        model = RandomForestRegressor(n_estimators=n_estimators)
        model.fit(X, y)
        return model
    
    @staticmethod
    def gradient_boosting_regression(X: list[float], y: list[float], n_estimators: int = 100, learning_rate: float = 0.1):
        model = GradientBoostingRegressor(n_estimators=n_estimators, learning_rate=learning_rate)
        model.fit(X, y)
        return model
    
    @staticmethod
    def ada_boost_regression(X: list[float], y: list[float], n_estimators: int = 50):
        model = AdaBoostRegressor(n_estimators=n_estimators)
        model.fit(X, y)
        return model
    
    @staticmethod
    def support_vector_regression(X: list[float], y: list[float], kernel: str = 'rbf', C: float = 1.0, epsilon: float = 0.1):
        model = SVR(kernel=kernel, C=C, epsilon=epsilon)
        model.fit(X, y)
        return model
    
