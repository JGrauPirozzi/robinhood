from setuptools import setup

setup(
    name="robinhood",
    version="0.1.3",
    author="Ben Kroop",
    author_email="benkroop@gmail.com",
    py_modules=['robinhood'],
    install_requires=[
        "requests>=2.7.0",
        "wheel>=0.24.0"
    ],
    description="""
        Automated, commission-free stock trading from Python using Robinhood's API.
    """,
    license="MIT License (See LICENSE)",
    long_description=open("README.rst").read(),
    url="https://github.com/benkroop/robinhood"
)
