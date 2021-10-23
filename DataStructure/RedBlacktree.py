from dataclasses import dataclass
from typing import Union, Any
import enum

class Color(enum.Enum):
    RED = enum.auto()
    BLACK = enum.auto()

@dataclass
class Leaf:
    color: Color.BLACK

@dataclass
class Node:
    data: Any
    color: Color.RED # Red = 1, Black = 0
    left: Union[Leaf, "Node"] = None
    right: Union[Leaf, "Node"] = None
    parent: Union[Leaf, "Node"] = None


class RedBlackTree:
    def __init__(self):
        self.root = None
        self._NIL = Leaf()

    def insert_case1(self, data):

