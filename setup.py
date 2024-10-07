from setuptools import setup, find_packages


setup(
    version="0.1.0",
    name="tsfel-scikit",
    packages=find_packages(),
    author="Badr Ayour EL AMRI",
    author_email="badrayour.elamri@protonmail.com",
    url="https://github.com/elamribadrayour/scikit-tsfel",
    description="A Python package for TSFEL feature extraction with scikit-learn integration",
    install_requires=[
        "tsfel",
        "pandas",
        "scikit-learn",
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.11",
)
