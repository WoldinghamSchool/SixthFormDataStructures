from typing import Type, Callable, Tuple, Optional
from warnings import warn
from . import meta_

def test(f:Callable, s:Type[object], test_name:Optional[str]=None, *argv, **kwargs) -> None:
    try:
        passed, msg = f(s)
    except Exception as e:
        warn(f"Got exception during test {test_name}.")
