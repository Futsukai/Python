# coding=utf-8
#!/usr/bin/python3

# 平衡因子 = 左子树高 - 右子树高
# 平衡因子 > 0 左倾，反之右倾 等于0时完全平衡
# -1，0，1都是认为是平衡的

from BinarySearchTree import BinarySearchTree
from TreeNode import TreeNode


class AVLTreeNode(TreeNode):
    def __init__(self, key, val, left=None, right=None, parent=None, factor=0):
        super().__init__(key, val, left=left, right=right, parent=parent)
        self.balance_factor = factor


class AVLTree(BinarySearchTree):

    def _put(self, key, val, current_node):
        if key == current_node.key:
            current_node.payload = val
            self.size = self.size - 1

        elif key < current_node.key:
            if current_node.has_left():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = AVLTreeNode(
                    key, val, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = AVLTreeNode(
                    key, val, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node: AVLTreeNode):
        if abs(node.balance_factor) > 1:
            self.rebalance(node)

        if node.parent != None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            else:
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, rot_root: AVLTreeNode):
        new_root = rot_root.right_child
        pass 
    #TODO 平衡术待完成
