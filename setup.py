from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='skip_thoughts',
    version='0.1.0',
    description='skip thoughts',
    long_description=readme,
    author='Google',
    author_email='',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'six==1.11.0',
        'tensorflow==1.9.0',
        'numpy==1.14.3',
        'nltk==3.3',
        'gensim==3.6.0',
        'scikit-learn==0.19.1',
    ],
)