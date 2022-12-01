from setuptools import find_packages
from distutils.core import setup

#=====Personalise here!=====#
__version__ = "0.0.11"      #
__name__    = "sixthformds" #
__author__  = "Daniel Sääw" #
#===========================#

print(f"Setting up package {__name__}v{__version__} by {__author__}.")

setup(
    name=__name__,
    version=__version__,
    description="A simple library of naively implemented data structures.",
    author=__author__,
    packages=find_packages()
)
