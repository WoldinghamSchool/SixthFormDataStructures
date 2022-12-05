from . import abstract_base_
from .. import base_testing_
from .. import meta_
from typing import Type, Optional, Tuple, Callable
from warnings import warn

def instantiate_list(size: Optional[int], cl: Type[abstract_base_.AbstractList], verbose:bool = True) -> Tuple[Optional[abstract_base_.AbstractList], bool]:
    """Test whether the implementation of Lists that is being tested can be instantiated (contains an implementatiopn of each List method).
    
    Parameters
    ----------
    size : Optional[int]
        The size of list to create if successful. None if working with lists unlimited in size.
    cl : Type[abstract_base_.AbstractList]
        The implementation of lists to test.
    verbose : bool
        Whether to narrate the test and show success messages.
    
    Returns
    -------
    S : Optional[abstract_base_.AbstractList]
        Either a list with the given size or 
    success : bool
        Whether the class was succesfully instantiated.

    Warns
    -----
    Of unsuccessful creation of list implementation.
    """
    try:
        if verbose: print("Verifying presence of each method necessary for implementing lists.")
        S = cl(size)
        if verbose: print("List successfully created (each method has been implemented.)")
        success = True
        return S, success
    except TypeError as e:
        success = False
        warn("Warning: Encountered error when attempting to instantiate List class from Lists.list")
        warnmsg = f"""
        This is most likely because the implementation of the List class in Lists/lists.py 
        does not yet implement each of the four methods that are necessary for lists:
        * isEmpty   
        * isFull   
        * append  
        * __len__   
        * __contains__  
        * __iter__   
        * __next__   

        The abstract base class for lists is {meta_.__name__}.Lists.AbstractList.
        You may extend this class (implementing the four methods above) yourself.
        """
        warn(warnmsg)
        return None, success

