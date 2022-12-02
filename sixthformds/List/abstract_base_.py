from abc import ABC, abstractmethod
from collections.abc import Iterable as IterCls
from typing import TypeVar, Iterable, Any

class AbstractList(ABC, IterCls):
    """An abstract class that provides an interface for
    Lists. It provides the following methods:

    Methods
    -------
    isEmpty(self) -> bool
        Returns `True` if list is empty.
    isFull(self) -> bool
        Returns `True` if List is full.
    append(self, item: Any) -> None
        Add an item to the end of a non-full list.
    __len__(self) -> Any
        Determine the length of the list.
        Naming uses Python key terms to allow writing `len(l)` where `l` is a List object.
    __contains__(self, item : Any) -> bool
        Determine whether a given item is contained in the list.
        Naming uses Python keywords to allow writing `x in l` where `l` is a List object.
    __iter__(self) -> Iterable
        Allows the creation of iterators through a list.
    __next__(self) -> Any
        Returns the next element in the iterator version of the list.
    """
    @abstractmethod
    def append(self, item: Any) -> None:
        """Adds an element to the end of a non-full list.

        Parameters
        ----------
        item : T
            The element to be added to the list.
        """
        pass
    @abstractmethod
    def __len__(self) -> int:
        """Returns the length of the list.

        Returns
        -------
        int
            The number of elements currently in the list.
        """
        pass
    @abstractmethod
    def isEmpty(self) -> bool:
        """Checks if list is empty.

        Returns
        -------
        bool
            True if the list is empty False otherwise.
        """
        pass
    @abstractmethod
    def isFull(self) -> bool:
        """Checks if list is full.
        
        Returns
        -------
        bool
            True if the list is full False otherwise.
        """
        pass
    @abstractmethod
    def __iter__(self):
        """Returns an iterator based on the list instance.
        
        Returns
        -------
        self
            Itself after adding some attributes to set up iteration. 
            The programmer implementing these methods needs to write 
            code that sets up an element-by-element traversal of the list.
        """
        pass
    @abstractmethod
    def __next__(self):
        """Provides the next element in the iterator version of this list.

        Returns
        -------
        x : Any
            The next element in this list.
        """
        pass
    @abstractmethod
    def __contains__(self, x : Any) -> bool:
        """Returns a Boolean indicator for whether an item is contained in the list.
        Naming allows writing `v in l` where `l` is a List object and `v` is some expression.

        Returns
        -------
        bool
            `True` if `x` is contained in the list, `False` otherwise.
        """
        pass