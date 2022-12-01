from . import abstract_base_
from typing import Type, Optional, Tuple
from warnings import warn
def instantiate_stack(size: Optional[int], cl: Type[abstract_base_.AbstractStack], verbose:bool = True) -> Tuple[Optional[abstract_base_.AbstractStack], bool]:
    """Test whether the implementation of Stacks that is being tested can be instantiated (contains an implementatiopn of each Stack method).
    
    Parameters
    ----------
    size : Optional[int]
        The size of stack to create if successful. None if working with stacks unlimited in size.
    cl : Type[abstract_base_.AbstractStack]
        The implementation of stacks to test.
    verbose : bool
        Whether to narrate the test and show success messages.
    
    Returns
    -------
    S : Optional[abstract_base_.AbstractStack]
        Either a stack with the given size or 
    success : bool
        Whether the class was succesfully instantiated.

    Warns
    -----
    Of unsuccessful creation of stack implementation.
    """
    try:
        if verbose: print("Verifying presence of each method necessary for implementing stacks.")
        S = cl(size)
        if verbose: print("Stack successfully created (each method has been implemented.)")
        success = True
        return S, success
    except TypeError as e:
        success = False
        warn("Warning: Encountered error when attempting to instantiate Stack class from Stacks.stack")
        warnmsg = """This is most likely because the implementation of the Stack class in Stacks/stacks.py does not yet implement each of the four methods that are necessary for stacks:
        * isFull
        * push
        * pop
        * isEmpty

        The abstract base class for stacks is danielsdatastructures.Stacks.AbstractStack.
        You may extend this class (implementing the four methods above) yourself.
        """
        warn(warnmsg)
        return None, success