# SixthFormDataStructures
A template for Sixth-Form implementations of commonly used data structures.

## Purpose

Anyone may fork this repository and implement the abstract data types provided. 

In particular, the sixth-form Computer-Science students of Woldingham School are bound to do this.

The repository has been set up to provide a Python library with abstract classes representing verious abstract data structures; with skeleton files providing classes implementing these in different ways. You can install this library using `python -m pip install git+https://www.github.com/WoldinghamSchool/SixthFormDataStructures.git`.

## Structure

This repository provides a Python library `sixthformds` in the corresponding folder and follows the Python folder structure for modules. Each subfolder has a file `__init__.py` which allows Python to treat said folder as a package. Each subfolder has files `testing_` and `abstract_base_` providing implementation tests for each data structure (to verify the correctness of a student's implementation) and the abstract base class specifying which methods need to be implemented, respectively. 

The file `sixthformds/meta_.py` contains some information about the package that any student or programmer forking this package is encouraged to personalise. In fact, each student is encouraged to change the package name from `sixthformds` to something more personal. To achieve this, the following changes need to be made:
* the folder `sixthformds` needs to be renamed
* the line `__name__ = "sixthformds"` in `sixthformds/__init__.py` needs to be changed to reflect the change of folder name. 
* You need to keep the variables `__name__`, `__version__` and `__author__` up-to-date in `setup.py`. Students are encouraged to update `__version__` as they update their fork of the repository. 

The personalisation options in `sixthformds/meta_.py` are the following:
* `__author__           : str`
* `__name__             : str`
* `__testing__          : bool`
* `__verbose_testing__  : bool`
`__testing__` controls whether the library should test an implementation of these data structures when they are imported within any code using this library. `__verbose_testing__` controls whether any other text besides warnings is printed *if* `__testing__` is set to `True`. `__name__` **must** be identical to the name of the folder containing the file, so if one of the two is changed the other must be, too. 
