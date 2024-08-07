from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='skip_thoughts',
    version='0.1.1',
    description='A pip installable version of skip_thoughts branched from tensorflow/research',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Julien Nyambal',
    author_email='jnyambal@retrorabbit.co.za',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'six==1.11.0',
        'tensorflow==2.11.1',
        'numpy==1.22.0',
        'nltk==3.6.6',
        'gensim==3.6.0',
        'scikit-learn==1.5.0',
    ],
    python_requires='>=2.7',
    url='https://github.com/RetroRabbit/skip_thoughts'
)
