from . import abstract_base_
from .. import base_testing_
from .. import meta_
from typing import Type, Optional, Tuple, Callable
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


def initialemptiness_(s : Type[abstract_base_.AbstractStack], size : Optional[int]) -> Tuple[bool, str]:
    """Tests the first Stack invariant: a new Stack should be empty.
    
    Parameters
    ----------
    s : Type[abstract_base_.AbstractStack]
        The stack instance to undergo testing.
    size : Optional[int]
        The (optional) capacity of the stack.
    
    Returns
    -------
    bool
        Indicates success of test.
    str
        Success/Error message. If error, passed to warning.
    
    Warnings
    --------
    * This test tries to verify the notion that a newly instantiated stack should be empty. The stack is passed as an argument and therefore it is the user's responsibility to only pass new Stacks. Students extening this library should never need to touch this function.
    * If the returned `bool` is `False` the returned `str` is intended to be passed to `warnings.warn`.
    """                                                                                                  
    if s.isEmpty():
        return True, "Success"
    else:
        return False, f"Failed test: Newly created stack returned isEmpty == False."
def initialfullness_(s, size : Optional[int]):
    """Tests the second Stack invariant: a new Stack should not be full.
    
    Parameters
    ----------
    s : Type[abstract_base_.AbstractStack]
        The stack instance to undergo testing.
    size: Optional[int]
        The (optional) capacity of the stack.
    
    Returns
    -------
    bool
        Indicates success of test.
    str
        Success/Error message. If error, passed to warning.
    
    Warnings
    --------
    * This test tries to verify the notion that a newly instantiated stack should not be full. The stack is passed as an argument and therefore it is the user's responsibility to only pass new Stacks. Students extening this library should never need to touch this function.
    * If the returned `bool` is `False` the returned `str` is intended to be passed to `warnings.warn`.
    * Stacks (and any other data structures) miss their purpose if initialised with maximum size 0. It is up to programmers extending this library whether to include checks/warnings to prevent this, however this method assumes that the passed stack was instantiated with maximum size > 1.
    """                                                                                                  
    if not s.isFull():
        return True, "Success"
    elif size == 0:
        return True, "Stack of capacity 0 created."
    else:
        return False, f"Failed test: Newly created stack returned isFull == True."
def proceduralfullness_(s, size):
    """Tests the third Stack invariant: a Stack should remain unfull after pushing fewer times than its capacity, if a capacity has been specified.
    
    Parameters
    ----------
    s : Type[abstract_base_.AbstractStack]
        The stack instance to undergo testing.
    size : Optional[int]
        The capacity of the stack or None if unlimited.
    
    Returns
    -------
    bool
        Indicates success of test.
    str
        Success/Error message. If error, passed to warning.
    
    Warns
    -----
    * If `size is None` and verbose testing is enabled this function warns that no check is actually performed before returning success (as no number of pushes could ever fill the stack).

    Warnings
    --------
    * If the returned `bool` is `False` the returned `str` is intended to be passed to `warnings.warn`.
    * The passed stack is assumed to be empty initially. That is, there is an assumption that is not checked within the method that `s.isEmpty() == True`.
    * 5 elements are pushed and a warning potentially displayed (depending on meta_.__verbose_testing__) if `size is None`. 
    """                                                                                                  
    for i in range(size):
        if not s.isFull():
            s.push(i)
        else:
            return False, f"Failed test: stack became full after {i} pushes despite being initialised with maxsize={size}"
    if s.isFull():
        return True, "Success"
    else:
        return False, f"Failed test: stack was not full after maxsize={size} pushes."
def filo_(s, size):
    """Tests the fifth Stack invariant: a Stack is a last-in-first-out data structure.
    
    Parameters
    ----------
    s : Type[abstract_base_.AbstractStack]
        The stack instance to undergo testing.
    size : Optional[int]
        The capacity of the stack or None if unlimited.
    
    Returns
    -------
    bool
        Indicates success of test.
    str
        Success/Error message. If error, passed to warning.
    
    Warnings
    --------
    * If the returned `bool` is `False` the returned `str` is intended to be passed to `warnings.warn`.

    """                                                                                                  
    while not s.isEmpty():
        s.pop()

    n = 5 if size is None else max(size, 5)

    for i in range(n):
        s.push(i)
    
    for j in range(4,0,-1):
        x = s.pop()
        if x != j:
            return False, "Failed test: stack did not maintain LIFO ordering."
        
def proceduralemptiness_(s, size):
    """Tests the fourth Stack invariant: a Stack should remain unempty after popping fewer times than had previously been pushed.
    
    Parameters
    ----------
    s : Type[abstract_base_.AbstractStack]
        The stack instance to undergo testing.
    size : Optional[int]
        The capacity of the stack or None if unlimited.
    
    Returns
    -------
    bool
        Indicates success of test.
    str
        Success/Error message. If error, passed to warning.
    
    Warns
    -----
    * If `size is None` and verbose testing is enabled this function warns that the test assumes five elements had previously been pushed.

    Warnings
    --------
    * If the returned `bool` is `False` the returned `str` is intended to be passed to `warnings.warn`.
    * The passed stack is assumed to be empty initially. That is, there is an assumption that is not checked within the method that `s.isEmpty() == True`.
    * The stack is assumed to contain 5 elements and a warning potentially displayed (depending on meta_.__verbose_testing__) if `size is None`. 
    """
    n = 5 if size is None else max(size, 5)                                                                                                  
    for i in range(n):
        if s.isEmpty():
            return False, f"Failed test: stack was empty after only {i} pops and {n} pushes."
        else:
            s.pop()
    if s.isEmpty():
        return True, "Success"
    else:
        return False, f"Failed test: stack was still not empty after {n} pops following {n} pushes."

stack_tests = [
    initialemptiness_,
    initialfullness_,
    proceduralfullness_,
    proceduralemptiness_,
    filo_,
]

def test_invariants(s : abstract_base_.AbstractStack, size : Optional[int]):
    for t in stack_tests:
        passed, msg = base_testing_.test(t, size)
        if not passed:
            warn(msg)
            return False
        elif msg != "Success":
            warn(msg)
        return True