from setuptools import setup, find_packages


setup(
    name="tsfel-scikit",
    version="0.1.0",
    author="Badr Ayour EL AMRI",
    author_email="badrayour.elamri@protonmail.com",
    description="A Python package for TSFEL feature extraction with scikit-learn integration",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/elamribadrayour/scikit-tsfel",
    packages=find_packages(),
    install_requires=[
        "tsfel",
        "pandas",
        "scikit-learn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
