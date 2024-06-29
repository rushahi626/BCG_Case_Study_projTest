from setuptools import setup, find_packages

setup(
    name="My BCG app",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pyspark",
        "pyyaml"
    ],
)
