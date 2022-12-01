"""sixthformds - A good chance to revise data structures AND practise programming!

A package that provides abstract base classes for various data structures to be extended and implemented by... YOU!
"""
from . import meta_

__version__ = meta_.__version__
__name__    = meta_.__name__
__author__  = meta_.__author__
__testing__ = meta_.__testing__

# Only add something to this list 
# if you add a completely new family of data structures!
submodules = ["Graph",  "List", "Stack", "Map", "Queue", "Set", "Vector"]
# Don't change anything below this line.
__all__ = submodules + ["__version__", "__name__", "__author__"]
def turnOffTesting():
    global __testing__
    __testing__ = False

def turnOnTesting():
    global __testing__ 
    __testing__ = True


import importlib as _importlib

def __getattr__(name : str):
    if name in submodules:
        print(f"{__name__}.{name}")
        _importlib.import_module(f"{__name__}.{name}")
    else:
        try:
            return globals()[name]
        except KeyError:
            raise AttributeError(
                f"Module '{__name__}' has no attribute '{name}'"
            )