# scikit-tsfel

[![PyPI version](https://badge.fury.io/py/scikit-tsfel.svg)](https://badge.fury.io/py/scikit-tsfel)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`scikit-tsfel` is a Python package that seamlessly integrates TSFEL (Time Series Feature Extraction Library) with Scikit-learn pipelines. It is designed to enhance the processing and analysis of time-series data by automating feature extraction.

## Features

- **Automated Feature Extraction**: Leverage TSFEL's comprehensive feature extraction capabilities within Scikit-learn pipelines.
- **Easy Integration**: Incorporate time-series feature extraction into your machine learning workflows effortlessly.
- **Customizable**: Configure sampling frequency and feature extraction settings according to your data needs.

## Installation

Install the package via pip:

```bash
pip install scikit-tsfel
```

## Usage

Here's a quick example of how to use `scikit-tsfel` in a Scikit-learn pipeline:

```python
import pandas
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from scikit_tsfel.feature_extractor import TSFELFeatureExtractor

# Sample data
data = pandas.DataFrame({
    'X': [/* time-series data */],
    'Y': [/* time-series data */],
    'Z': [/* time-series data */],
})

# Define your pipeline
pipeline = Pipeline([
    ('feature_extraction', TSFELFeatureExtractor(fs=100)),
    ('classifier', RandomForestClassifier())
])

# Fit the pipeline
pipeline.fit(data, labels)

# Make predictions
predictions = pipeline.predict(data)
print(predictions)
```

## Configuration

The `TSFELFeatureExtractor` can be customized to suit different datasets:
- **fs**: Sampling frequency of your time-series data.
- **Feature Configuration**: Modify the feature extraction settings within the `feature_extractor.py` file for advanced use.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact [Badr Ayour EL AMRI](mailto:badrayour.elamri@protonmail.com).

## Acknowledgements

- [Scikit-learn](https://scikit-learn.org) for the machine learning framework.
- [TSFEL](https://github.com/fraunhoferportugal/tsfel) for the feature extraction library.
