from setuptools import find_packages
from distutils.core import setup

from .sixthformds import meta_

__version__ = meta_.__version__
__name__    = meta_.__name__
__author__  = meta_.__author__

print(f"Setting up package {__name__}v{__version__} by {__author__}.")

setup(
    name=__name__,
    version=__version__,
    description="A simple library of naively implemented data structures.",
    author=__author__,
    packages=find_packages()
)
