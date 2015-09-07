from setuptools import setup

setup(
    name="robinhood",
    version="0.1.0",
    author="Ben Kroop",
    author_email="benkroop@gmail.com",
    py_modules=['robinhood'],
    install_requires=[
        "requests>=2.7.0",
        "wheel>=0.24.0"
    ],
    description="""
        Use Robinhood API from Python
    """,
    license="MIT License (See LICENSE)",
    long_description=open("README.rst").read(),
    url="https://github.com/benkroop/robinhood"
)
