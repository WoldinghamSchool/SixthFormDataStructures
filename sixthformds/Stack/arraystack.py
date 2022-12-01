"""Provides an implementation of array-based stacks."""

# You will need numpy for the underlying array.
import numpy as np
# In order to force you to implement proper stacks,
# here is a module with a specification of what you need to implement.
from . import abstract_base_

# the content of the parentheses indicates that your class extends the 
# abstract stack class we have imported above.
class ArrayStack(abstract_base_.AbstractStack):
    # You (may) need to add some parameters to this constructor.
    def __init__(self):
        # What needs to happen to create a new Stack?
        pass