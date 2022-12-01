from . import abstract_base_
from . import testing_
from .. import meta_
from warnings import warn
N_ = 100
AbstractStack = abstract_base_.AbstractStack

from . import arraystack

ArrayStack = arraystack.ArrayStack

if meta_.__testing__:
    
    S, success = testing_.instantiate_stack(size=N_, cl=arraystack.ArrayStack, verbose=meta_.__verbose_testing__)
    
    if success:
        success = testing_.test_invariants(s=S, size=N_)
        if success and meta_.__verbose_testing__: print("Import successful. Enjoy your stacks!")
        if not success:
            warn(f"You may use the class {meta_.name}.arraystack but we make no guarantees that it will work.")