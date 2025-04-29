import sys

PY36 = sys.version_info[0:2] >= (3, 6)
PY37 = sys.version_info[0:2] >= (3, 7)
PY38 = sys.version_info[0:2] >= (3, 8)
PY39 = sys.version_info[0:2] >= (3, 9)
PY310 = sys.version_info[0:2] >= (3, 10)
PY311 = sys.version_info[0:2] >= (3, 11)

if PY38:
    from typing import Protocol
else:
    from typing_extensions import Protocol


if PY38:
    from typing import Literal
else:
    from typing_extensions import Literal


if PY38:
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


if PY310:
    from types import NoneType
else:
    NoneType = type(None)


if PY310:
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


if PY311:
    from typing import Self
else:
    from typing_extensions import Self


if PY311:
    from typing import TypeVarTuple
else:
    from typing_extensions import TypeVarTuple


if PY311:
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "Literal",
    "NoneType",
    "Protocol",
    "Self",
    "TypeAlias",
    "TypeVarTuple",
    "TypedDict",
    "Unpack",
)
