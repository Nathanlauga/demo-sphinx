from sklearn import datasets
import pandas as pd

def load_boston_as_df():
    """Load and return the boston house-prices dataset (regression).

    Source from scikit-learn : https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston

    Returns
    -------
    pd.DataFrame:
        Boston dataset as pandas DataFrame
    """
    _boston = datasets.load_boston()
    
    boston = pd.DataFrame(_boston.data, columns=_boston.feature_names)
    boston['target'] = _boston.target
    
    return boston

def load_iris_as_df():
    """Load and return the iris dataset (classification).

    The iris dataset is a classic and very easy multi-class classification dataset.

    Source from scikit-learn : https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris

    Returns
    -------
    pd.DataFrame:
        Iris dataset as pandas DataFrame
    """
    _iris = datasets.load_iris()
    
    iris = pd.DataFrame(_iris.data, columns=_iris.feature_names)
    iris['target'] = _iris.target
    
    return iris