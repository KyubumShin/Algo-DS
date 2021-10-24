from dataclasses import dataclass
from typing import Union, Any, Optional
import enum


class Color(enum.Enum):
    RED = enum.auto()
    BLACK = enum.auto()


@dataclass
class Leaf:
    color = Color.BLACK


@dataclass
class Node:
    data: Any
    color: Color = Color.RED
    left: Union[Leaf, "Node"] = None
    right: Union[Leaf, "Node"] = None
    parent: Union[Leaf, "Node"] = None


class RedBlackTree:
    def __init__(self) -> None:
        self._NIL: Leaf = Leaf()
        self.root: Union[Node, Leaf] = self._NIL
        self.storage: list = []

    def __repr__(self) -> str:
        """tree visualize"""
        if self.root:
            return (
                f"{type(self)}\nroot={self.root}, \n"
                f"tree_height={str(self.get_height(self.root))}"
            )
        return "empty tree"

    def _grandparent(self, node: Node) -> Union[Node, Leaf]:
        if isinstance(node, Node) and isinstance(node.parent, Node):
            return node.parent.parent
        else:
            return self._NIL

    def _uncle(self, node: Node) -> Union[Node, Leaf]:
        grandparent = self._grandparent(node)
        if isinstance(grandparent, Leaf):
            return Leaf
        if node.parent == grandparent.left:
            return grandparent.right
        else:
            return grandparent.left

    def _sibling(self, node: Node) -> Union[Node, Leaf]:
        parent = node.parent
        if node == parent.left:
            return parent.right
        else:
            return parent.left

    def search(self, data: Any) -> Optional[Node]:
        current = self.root

        while isinstance(current, Node):
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:  # Key found
                return current
        # If the tree is empty or No Key
        return None

    def get_leftmost(self, node: Node) -> Node:
        current_node = node
        while isinstance(current_node.left, node):
            current_node = current_node.left
        return current_node

    def get_rightmost(self, node: Node) -> Node:
        current_node = node
        while isinstance(current_node.right, node):
            current_node = current_node.right
        return current_node

    def insert(self, data) -> None:
        """
        :param data:
        :return: None

        if key Duplicate
            raise KeyError
        """
        new_node = Node(data=data)
        parent: Union[Node, Leaf] = self._NIL
        current: Union[Node, Leaf] = self.root
        while isinstance(current, Node):
            parent = current
            if new_node.data > current.data:
                current = current.right
            elif new_node.data < current.data:
                current = current.left
            else:
                raise KeyError(key=new_node.data)
        new_node.parent = parent
        if not isinstance(parent, Leaf):
            if new_node.data < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node
        new_node.left = self._NIL
        new_node.right = self._NIL
        self._insert_fix(new_node)

    def _insert_fix(self, node) -> None:
        parent = node.parent
        if isinstance(parent, Leaf):  # Case 1
            node.color = Color.BLACK
            self.root = node
            return
        if parent.color == Color.RED:  # Case 2
            uncle = self._uncle(node)  # Case 3
            grandfather = self._grandparent(node)
            if isinstance(uncle, Node) and uncle.color == Color.RED:
                parent.color = Color.BLACK
                uncle.color = Color.BLACK
                grandfather.color = Color.RED
                self._insert_fix(grandfather)
            else:  # Case 4
                if node == parent.right and parent == grandfather.left:
                    self._left_rotate(parent)
                    node = node.left
                elif node == parent.left and parent == grandfather.right:
                    self._right_rotate(parent)
                    node = node.right
                grandfather = self._grandparent(node)  # Case 5
                parent = node.parent
                parent.color = Color.BLACK
                grandfather.color = Color.RED
                if node == parent.left:
                    self._right_rotate(grandfather)
                else:
                    self._left_rotate(grandfather)

    def replace_node(self, delete_node: Node, replace_node: Node) -> None:
        parent = delete_node.parent
        replace_node.parent = parent
        if isinstance(parent, Leaf):
            self.root = replace_node
        else:
            if parent.left == delete_node:
                parent.left = replace_node
            else:
                parent.right = replace_node

    def delete_node(self, data: Any) -> None:
        node = self.search(data)
        original_color = node.color
        if isinstance(node, Node):
            if isinstance(node.left, Node) and isinstance(node.right, Node):
                pass
            elif isinstance(node.left):
                pass
        else:
            raise KeyError

    def _delete_fix(self, node: Node) -> None:
        pass

    def _left_rotate(self, node_x : Node) -> None:
        print("left rotate")
        node_y = node_x.right
        if isinstance(node_y, Leaf):
            raise RuntimeError("Invalid left rotate, node.left is Leaf")
        node_x.right = node_y.left

        if isinstance(node_y.left, Node):
            node_y.left.parent = node_x
        node_y.parent = node_x.parent

        if isinstance(node_y.parent, Leaf):
            self.root = node_y

        elif node_x == node_x.parent.left:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y

        node_y.left = node_x
        node_x.parent = node_y

    def _right_rotate(self, node_x : Node) -> None:
        print("right rotate")
        node_y = node_x.left
        if isinstance(node_y, Leaf):
            raise RuntimeError("Invalid right rotate, node.right is Leaf")
        node_x.left = node_y.right

        if isinstance(node_y.right, Node):
            node_y.right.parent = node_x
        node_y.parent = node_x.parent

        if isinstance(node_y.parent, Leaf):
            self.root = node_y

        elif node_x == node_x.parent.right:
            node_x.parent.right = node_y
        else:
            node_x.parent.left = node_y

        node_y.right = node_x
        node_x.parent = node_y

    @staticmethod
    def get_height(node : Union[Leaf, Node]) -> int:
        if isinstance(node, Node):
            if isinstance(node.left, Node) and isinstance(node.right, Node):
                return max(RedBlackTree.get_height(node.left), RedBlackTree.get_height(node.right)) + 1
            if isinstance(node.left, Node):
                return RedBlackTree.get_height(node.left) + 1
            if isinstance(node.right, Node):
                return RedBlackTree.get_height(node.right) + 1
        return 0


if __name__ == "__main__":
    import random
    RB_sorted = RedBlackTree()
    RB_random = RedBlackTree()
    insert_element = [i for i in range(32)]
    insert_shuffle = [i for i in range(32)]
    random.shuffle(insert_shuffle)
    for i in insert_shuffle:
        RB_random.insert(i)
    else:
        print(RB_random)

    for i in insert_element:
        RB_sorted.insert(i)
    else:
        print(RB_sorted)
