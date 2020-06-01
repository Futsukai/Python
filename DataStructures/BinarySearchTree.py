# coding=utf-8
#!/usr/bin/python3

class BinarySearchTree(object):

    """
    小于父节点的键在左子树，大于父节点的键在右子树，称为二叉搜索性
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        # 迭代
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(
                    key, val, parent=current_node)
        else:
            if current_node.has_right():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(
                    key, val, parent=current_node)


class TreeNode():

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left(self):
        return self.left_child

    def has_right(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        # 先右后左，再否定 ，无子则是叶
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left():
            self.left_child.parent = self
        if self.has_right():
            self.right_child.parent = self
