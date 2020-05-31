# coding=utf-8
#!/usr/bin/python3

class BinaryTree(object):
    def __init__(self, root_v):
        self.root = root_v
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child:
            n = BinaryTree(new_node)
            n.left_child = self.left_child
            self.left_child = n
        else:
            self.left_child = BinaryTree(new_node)

    def insert_right(self, new_node):
        if self.right_child:
            n = BinaryTree(new_node)
            n.right_child = self.right_child
            self.right_child = n
        else:
            self.right_child = BinaryTree(new_node)

    def get_right(self):
        return self.right_child

    def get_left(self):
        return self.left_child

    def get_root(self):
        return self.root

    def set_root(self, val):
        self.root = val

    def printexp(self):
        s = "("
        if self.left_child:
            s = s + self.get_left().printexp()

        s = s + str(self.get_root())

        if self.right_child:
            s = s + self.get_right().printexp() 
        s += ')'
        return s


t = BinaryTree(10)
t.insert_left(5)
t.insert_right(3)
t.insert_left(2)
t.insert_right(1)
t.insert_left(4)
t.insert_right(0)

print(t.printexp())