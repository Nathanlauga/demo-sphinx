import getpass
import pickle
import joblib
from sklearn.base import BaseEstimator


# TODO : add logs
class BPCEModel(BaseEstimator):
    """Class that act as an abstract of any model that 
    follows scikit-learn API (fit, predict)

    The model has to be set with the estimator parameter

    Parameters
    ----------
    estimator : 
        estimator object

    Attributes
    ----------
    is_fitted: bool
        Whether the estimator
    estimator: 
        estimator object
    author: str
        author of the model (can be changed)
    input_cols: list
        List of columns used in .fit so that
        we conserve the which feature were used
        during the training
    estimator_details: dict
        Details of the estimator : module and version
    """

    is_fitted = False
    _author = None
    _input_cols = None
    _estimator = None

    def __init__(self, estimator, **kwargs):
        self.estimator = estimator
        self.set_params(**kwargs)
        self.author = getpass.getuser()

        self._set_details()

    def __str__(self):
        output_text = "BPCEModel:\n\tAuthor: {}\n\tBase estimator: {}\n".format(
            self.author,
            self.estimator
        )

        output_text += "\tEstimator module: {} ({})\n".format(
            self.estimator_details['module'],
            self.estimator_details['version']
        )

        if self.is_fitted:
            additionnal_text = "\tFitted on {} features (use '.input_cols')".format(
                len(self.input_cols)
            )
        else:
            additionnal_text = "Not fitted yet"

        return output_text + additionnal_text

    def __repr__(self):
        return str(self)

    def _set_details(self):
        """Set estimator_details attributes, retrieves the 
        module and the version of the estimator object
        """
        estimator_details = {}

        module = self.estimator.__module__.split('.')[0]
        version = 'No module version found'
        try:
            version = __import__(module).__version__
        except:
            pass

        estimator_details['module'] = module
        estimator_details['version'] = version

        self.estimator_details = estimator_details

    @property
    def input_cols(self):
        return self._input_cols

    @input_cols.setter
    def input_cols(self, value):
        self._input_cols = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def estimator(self):
        return self._estimator

    @estimator.setter
    def estimator(self, value):
        self._estimator = value

    def set_params(self, **kwargs):
        """Set the parameters of this estimator.

        The method works on simple estimators as well as on nested objects
        (such as sklearn.pipeline.Pipeline).

        Parameters
        ----------
        **params : dict
            Estimator parameters.

        Returns
        -------
        self : estimator instance
            Estimator instance.
        """
        params = dict()

        for key, item in kwargs.items():
            if key in self.estimator.get_params():
                params[key] = item

        self.estimator.set_params(**params)
        self.is_fitted = False

        return self

    def get_params(self, **kwargs):
        """Get parameters for this estimator.

        Parameters
        ----------
        deep : bool, default=True
            If True, will return the parameters for this estimator and
            contained subobjects that are estimators.

        Returns
        -------
        params : dict
            Parameter names mapped to their values.
        """
        return self.estimator.get_params(**kwargs)

    def fit(self, X, y, **kwargs):
        """Train the estimator based on X and y.
        Call estimator.fit() function

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The training input samples. Internally, its dtype will be converted
            to dtype=np.float32. If a sparse matrix is provided, it will be
            converted into a sparse csc_matrix.
        y : array-like of shape (n_samples,) or (n_samples, n_outputs)
            The target values (class labels in classification, real numbers in
            regression).
        **kwargs:
            Estimator fit argument

        Returns
        -------
        self : object
        """
        # TODO : set input cols outside ?
        self.input_cols = X.columns

        estimator = self.estimator
        estimator_ = estimator.fit(X, y, **kwargs)

        self.estimator = estimator_
        self.is_fitted = True

        return self

    def predict(self, X):
        """Prediction based on X.
        Call estimator.predict() function

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The input samples. Internally, its dtype will be converted to
            dtype=np.float32. If a sparse matrix is provided, it will be
            converted into a sparse csr_matrix.

        Returns
        -------
        y : ndarray of shape (n_samples,) or (n_samples, n_outputs)
            The predicted classes.

        Raises
        ------
        ValueError: 
            Model should be fitted before using predict
        """
        if self.is_fitted:
            return self.estimator.predict(X[self.input_cols])
        else:
            raise ValueError("Model should be fitted before using predict")

    def predict_proba(self, X):
        """Predict class probabilities for X.
        Call estimator.predict_proba() function

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The input samples. Internally, its dtype will be converted to
            dtype=np.float32. If a sparse matrix is provided, it will be
            converted into a sparse csr_matrix.

        Returns
        -------
        p : ndarray of shape (n_samples, n_classes), or a list of n_outputs
            such arrays if n_outputs > 1.

        Raises
        ------
        ValueError: 
            Model should be fitted before using predict
        """
        if self.is_fitted:
            return self.estimator.predict_proba(X[self.input_cols])
        else:
            raise ValueError(
                "Model should be fitted before using predict_proba")

    def score(self, X, y, **kwargs):
        """Score computed from estimator.score() method

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Test samples.
        y : array-like of shape (n_samples,) or (n_samples, n_outputs)
            True labels for `X`.
        **kwargs:
            Estimator score argument

        Returns
        -------
        score : float
            Score computed from estimator.score() method

        Raises
        ------
        ValueError
            Model should be fitted before using score
        """
        if self.is_fitted:
            return self.estimator.score(X[self.input_cols], y, **kwargs)
        else:
            raise ValueError(
                "Model should be fitted before using score")


    def save(self, fpath, lib='joblib', mode='wb', **kwargs):
        """Save model as a file object using joblib or pickle

        Parameters
        ----------
        fpath : str
            Path where to save the model
        lib : str, optional
            module to dump with, by default 'joblib'
            can only be 'joblib' or 'pickle'
        mode : str, optional
            writing mode, by default 'wb'
        **kwargs:
            dump parameters

        Raises
        ------
        ValueError
            lib must be joblib or pickle.
        """
        if lib not in ['joblib', 'pickle']:
            raise ValueError('lib must be joblib or pickle.')

        module = joblib if lib == 'joblib' else pickle

        with open(fpath, mode) as file:
            module.dump(self, file, **kwargs)


def load_model(fpath, lib='joblib', mode='rb', **kwargs):
    """Load model from a file using joblib or pickle

    Parameters
    ----------
    fpath : str
        Path where the model file is stored
    lib : str, optional
        module to load with, by default 'joblib'
        can only be 'joblib' or 'pickle'
    mode : str, optional
        reading mode, by default 'rb'
    **kwargs:
        load parameters

    Returns
    -------
    object:
        loaded model

    Raises
    ------
    ValueError
        lib must be joblib or pickle.
    """
    if lib not in ['joblib', 'pickle']:
        raise ValueError('lib must be joblib or pickle.')

    module = joblib if lib == 'joblib' else pickle

    with open(fpath, mode) as file:
        model = module.load(file, **kwargs)

    return model
