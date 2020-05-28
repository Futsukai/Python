# coding=utf-8
#!/usr/bin/python3


class Node(object):

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def lenght(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count
        
if __name__ == "__main__":
    n = Node(2)
    print(n.data)
