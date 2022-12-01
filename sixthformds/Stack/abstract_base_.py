from abc import ABC, abstractmethod
from typing import TypeVar
T = TypeVar('T')

class AbstractStack(ABC):
    """An abstract class that provides an interface for
    Stacks. It provides the following methods:

    Methods
    -------
    isEmpty(self) -> bool
        Returns True if Stack is empty.
    isFull(self) -> bool
        Returns True if Stack is full.
    push(self, item: T) -> None
        Add an item onto a non-full stack.
    pop(self) -> T
        Remove and return the item from the top of the stack.
    """
    @abstractmethod
    def push(self, item: T) -> None:
        """Adds an element to the top of a non-full stack.

        Parameters
        ----------
        item : T
            The element to be added to the stack.
        """
        pass
    @abstractmethod
    def pop(self) -> T:
        """Removes an element from a non-empty stack and removes it.

        Returns
        -------
        item : T
            the element formerly at the top of the stack.
        
        Warnings
        --------
        This method does not check that the stack is not empty before attempting to remove an element. User code should always call .isEmpty() first to determine whether the stack can be popped.
        """
        pass
    @abstractmethod
    def isEmpty(self) -> bool:
        """Checks if stack is empty.

        Returns
        -------
        bool
            True if the stack is empty False otherwise.
        """
        pass
    @abstractmethod
    def isFull(self) -> bool:
        """Checks if stack is full.
        
        Returns
        -------
        bool
            True if the stack is full False otherwise.
        """
        pass