import tsfel
import pandas
from sklearn.base import BaseEstimator, TransformerMixin


class TSFELFeatureExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, fs: int = 100):
        self.fs = fs
        self.cfg = tsfel.get_features_by_domain()

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if not isinstance(X, pandas.DataFrame):
            X = pandas.DataFrame(data=X)
        features = tsfel.time_series_features_extractor(
            fs=self.fs,
            timeseries=X,
            config=self.cfg,
        )
        return features
