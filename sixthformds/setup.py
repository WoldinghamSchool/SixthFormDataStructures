from setuptools import find_packages
from distutils.core import setup

from . import meta_

__version__ = meta_.__version__
__name__    = meta_.__name__
__author__  = meta_.__author__

setup(
    name=__name__,
    version=__version__,
    description="A simple library of naively implemented data structures.",
    author=__author__,
    packages=find_packages()
)