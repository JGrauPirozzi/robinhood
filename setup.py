from setuptools import setup, find_packages

setup(
    name="robinhood",
    version="0.1.0",
    author="Ben Kroop",
    author_email="benkroop@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.7.0",
        "wheel>=0.24.0"
    ],
    description="""
        Use Robinhood API from Python
    """,
    license="MIT License (See LICENSE)",
    long_description=open("README.md").read(),
    url="https://github.com/benkroop/robinhood"
)