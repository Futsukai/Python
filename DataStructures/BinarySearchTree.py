# coding=utf-8
#!/usr/bin/python3

from TreeNode import TreeNode


class BinarySearchTree(object):

    """
    小于父节点的键在左子树，大于父节点的键在右子树，称为二叉搜索性
    """

    def __init__(self):
        # var type:TreeNode 变量标注
        self.root = None  # type:TreeNode
        self.size = 0

    def length(self):
        return self.size

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def put(self, key, val):

        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

        self.size = self.size + 1

    def _put(self, key, val, current_node):

        if key == current_node.key:
            current_node.payload = val
            self.size = self.size - 1

        elif key < current_node.key:
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

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.is_leaf():
            if currentNode == currentNode.parent.left_child:
                currentNode.parent.left_child = None
            else:
                currentNode.parent.right_child = None
        elif currentNode.has_both_children():
            succ = currentNode.find_successor()
            succ.splice_out()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            if currentNode.has_left():
                if currentNode.is_left_child():
                    currentNode.left_child.parent = currentNode.parent
                    currentNode.parent.left_child = currentNode.left_child
                elif currentNode.is_right_child():
                    currentNode.left_child.parent = currentNode.parent
                    currentNode.parent.right_child = currentNode.left_child
                else:
                    currentNode.replace_node_data(currentNode.left_child.key,
                                                  currentNode.left_child.payload,
                                                  currentNode.left_child.left_child,
                                                  currentNode.left_child.right_child)
            else:
                if currentNode.is_left_child():
                    currentNode.right_child.parent = currentNode.parent
                    currentNode.parent.left_child = currentNode.right_child
                elif currentNode.is_right_child():
                    currentNode.right_child.parent = currentNode.parent
                    currentNode.parent.right_child = currentNode.right_child
                else:
                    currentNode.replace_node_data(currentNode.right_child.key,
                                                  currentNode.right_child.payload,
                                                  currentNode.right_child.left_child,
                                                  currentNode.right_child.right_child)

    def __len__(self):
        return self.size

    def __iter__(self):
        # 迭代
        return self.root.__iter__()

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, k, v):
        self.put(k, v)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False


t = BinarySearchTree()
t.put("1", 123)
t.put("2", 222)
t.put("2", 999)
t.put("2", 000)
t.put("3", 444)
del t['2']


# print(t["2"])
print("len", t.length())

for i in t:
    print(i, t[i])
