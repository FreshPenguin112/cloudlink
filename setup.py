"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages

setup(
    name="cloudlink",
    author="urmom",
    author_email="hank@pythoncreate.com",
    description="Description of the project.",
    version="0.1.9.1",
    packages=find_packages(where=".", exclude=["tests"]),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.0",
        "Topic :: Utilities",
    ],
)
