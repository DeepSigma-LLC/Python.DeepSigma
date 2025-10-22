from sklearn.model_selection import train_test_split,  KFold, StratifiedKFold,TimeSeriesSplit, GroupKFold

class Preprocessing:

    @staticmethod
    def train_test_split(X: list[list[float]], y: list[int], test_size: float = 0.2, random_state: int = None):
        """
        Split the dataset into training and testing sets.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param test_size: Proportion of the dataset to include in the test split.
        :param random_state: Controls the shuffling applied to the data before applying the split.
        :return: Tuple of training and testing sets (X_train, X_test, y_train, y_test).
        """
        return train_test_split(X, y, test_size=test_size, random_state=random_state)

    @staticmethod
    def k_fold(X: list[list[float]], y: list[int], n_splits: int = 5, shuffle: bool = True, random_state: int = None):
        """
        Perform K-Fold cross-validation.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param n_splits: Number of folds.
        :param shuffle: Whether to shuffle the data before splitting into batches.
        :param random_state: Controls the randomness of the shuffling.
        :return: KFold object for cross-validation.
        """
        return KFold(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
    
    @staticmethod
    def stratified_k_fold(X: list[list[float]], y: list[int], n_splits: int = 5, shuffle: bool = True, random_state: int = None):
        """
        Perform Stratified K-Fold cross-validation.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param n_splits: Number of folds.
        :param shuffle: Whether to shuffle the data before splitting into batches.
        :param random_state: Controls the randomness of the shuffling.
        :return: StratifiedKFold object for cross-validation.
        """
        return StratifiedKFold(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
    
    @staticmethod
    def time_series_split(X: list[list[float]], y: list[int], n_splits: int = 5):
        """
        Perform Time Series Split cross-validation.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param n_splits: Number of splits.
        :return: TimeSeriesSplit object for cross-validation.
        """
        return TimeSeriesSplit(n_splits=n_splits)
    
    @staticmethod
    def group_k_fold(X: list[list[float]], y: list[int], groups: list[int], n_splits: int = 5):
        """
        Perform Group K-Fold cross-validation.

        :param X: Features, a list of lists where each inner list is a feature vector.
        :param y: Labels, a list of integers representing class labels.
        :param groups: Group labels for the samples used while splitting the dataset into train/test set.
        :param n_splits: Number of splits.
        :return: GroupKFold object for cross-validation.
        """
        return GroupKFold(n_splits=n_splits)

