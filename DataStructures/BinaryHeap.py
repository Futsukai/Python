# coding=utf-8
#!/usr/bin/python3

class BinaryHeap(object):
    """
    二叉堆，完全二叉树(除了最底层,每一层的节点都是满的)可以用列表来实现
    入队和出队均可达到O(logN)
    节点p的左子点在2p，右子点在2p+1
    父节点在p/2
    """

    def __init__(self, list_build=None):
        self.heap_list = [0]
        self.current_size = 0
        if list_build:
            self.build_heap_for_list(list_build)

    def build_heap_for_list(self, list_build):
        i = len(list_build) // 2
        self.current_size = len(list_build)
        # list_build[:]  切片的复制写法，复制一个list
        self.heap_list = [0] + list_build[:]
        while i > 0:
            self.per_down(i)
            i = i - 1

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.per_Up(self.current_size)

    def del_min(self):
        return_v = self.heap_list[1]
        # 由于是最小堆，所以最顶层第一个就是最小的，取出后将进行堆的重构，所以覆盖掉该元素，并执行重构子树
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        # 下沉
        self.per_down(1)
        return return_v

    def per_Up(self, i):
        """
        尝试上升指定的元素
        """
        while i // 2 > 0:
            father = i // 2
            if self.heap_list[i] < self.heap_list[father]:
                self.heap_list[i], self.heap_list[father] = self.heap_list[father], self.heap_list[i]
            i = father

    def per_down(self, i):
        """
        尝试重构指定元素的子树
        """
        print(i, self.heap_list)
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        """
        找出子节点中的最小位置
        """
        left = i * 2
        right = left + 1
        if right > self.current_size:
            return left
        else:
            if self.heap_list[left] < self.heap_list[right]:
                return left
            else:
                return right


a = [9, 6, 5, 2, 3]

print(BinaryHeap(a).heap_list)
