from abc import ABC, abstractmethod
from collections.abc import Iterable as IterCls
from typing import TypeVar, Iterable, Any

T = TypeVar("T")

class AbstractQueue(ABC):
    """An abstract class that provides an interface for
    Queues. It provides the following methods:

    Methods
    -------
    isEmpty(self) -> bool
        Returns True if Queue is empty.
    isFull(self) -> bool
        Returns True if Queue is full.
    enqueue(self, item: T) -> None
        Add an item onto a non-full queue.
    dequeue(self) -> T
        Remove and return the item from the front of the queue.
    """
    @abstractmethod
    def enqueue(self, item: T) -> None:
        """Adds an element to the back of a non-full queue.

        Parameters
        ----------
        item : T
            The element to be added to the queue.
        """
        pass
    @abstractmethod
    def dequeue(self) -> T:
        """Removes an element from a non-empty queue and removes it.

        Returns
        -------
        item : T
            the element formerly at the top of the queue.
        
        Warnings
        --------
        This method does not check that the queue is not empty before attempting to remove an element. User code should always call .isEmpty() first to determine whether the stack can be popped.
        """
        pass
    @abstractmethod
    def isEmpty(self) -> bool:
        """Checks if queue is empty.

        Returns
        -------
        bool
            True if the queue is empty False otherwise.
        """
        pass
    @abstractmethod
    def isFull(self) -> bool:
        """Checks if queue is full.
        
        Returns
        -------
        bool
            True if the queue is full False otherwise.
        """
        pass