from io import StringIO as StringIO
from typing import Any, Dict, Iterable, List, Tuple

PY2: bool
PYPY: bool
PYPY2: bool
PY37: bool
izip: Any
imap: Any
xrange: Any
basestring = str
unicode = str
buffer = bytes
int_types: Tuple[int, ...]

def cmp(a: Any, b: Any) -> int: ...
def iteritems(dict: Dict[Any, Any]) -> Iterable: ...
def itervalues(dict: Dict[Any, Any]) -> Iterable: ...
def items_list(dict: Dict[Any, Any]) -> List[Any]: ...
def values_list(dict: Dict[Any, Any]) -> List[Any]: ...
def with_metaclass(meta: Any, *bases: Any) -> Any: ...
