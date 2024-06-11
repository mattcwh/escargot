from setuptools import setup, find_packages

setup(
    name='escargot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'scikit-learn',
        'matplotlib'
    ],
)