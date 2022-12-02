from setuptools import find_packages
from distutils.core import setup

#=====Personalise here!=====#
__version__ = "0.0.13"      #
__name__    = "sixthformds" #
__author__  = "Daniel Sääw" #
#===========================#
# Add any libraries your code needs to the list below!
__prereqs__ = ["numpy"]

print(f"Setting up package {__name__}v{__version__} by {__author__}.")

setup(
    name=__name__,
    version=__version__,
    description="A simple library of naively implemented data structures.",
    author=__author__,
    packages=find_packages(),
    requires=__prereqs__,
)
