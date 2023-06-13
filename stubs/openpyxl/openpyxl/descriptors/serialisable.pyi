from _typeshed import Incomplete
from typing import Any, ClassVar
from typing_extensions import Final

from openpyxl.descriptors import MetaSerialisable

KEYWORDS: Final[frozenset[str]]
seq_types: Final[tuple[type[list[Any]], type[tuple[Any, ...]]]]

class Serialisable(metaclass=MetaSerialisable):
    # These dunders are always set at runtime by MetaSerialisable so they can't be None
    __attrs__: ClassVar[tuple[str, ...]]
    __nested__: ClassVar[tuple[str, ...]]
    __elements__: ClassVar[tuple[str, ...]]
    __namespaced__: ClassVar[tuple[tuple[str, str], ...]]
    idx_base: int
    @property
    # TODO: needs overrides in many sub-classes
    # @abstractmethod
    def tagname(self) -> str: ...
    namespace: Incomplete
    @classmethod
    def from_tree(cls, node): ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...
    def __iter__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self) -> int: ...
    def __add__(self, other): ...
    def __copy__(self): ...
