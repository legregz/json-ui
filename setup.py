from setuptools import setup, find_packages

setup(
    name='pyguin',
    version='0.1',
    packages=find_packages(),
    install_require=[
        'pygame>=2.6.0'
    ],
)