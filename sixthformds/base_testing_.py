from typing import Type, Callable, Tuple, Optional
from warnings import warn
from . import meta_

def test(f:Callable, s:Type[object], test_name:Optional[str]=None, *argv, **kwargs) -> None:
    passed, msg = f(s, *argv, **kwargs)
    return passed, msg

