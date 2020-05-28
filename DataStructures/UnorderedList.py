# coding=utf-8
# !/usr/bin/python3

# shift + alt + f


class Node(object):

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def append(self, item):
        current = self.head
        while current is not None:
            if current.get_next() is None:
                temp = Node(item)
                current.set_next(temp)
                break
            else:
                current = current.get_next()

    def index(self, item):
        index = -1
        current = self.head
        while current is not None:
            index += 1
            if item == current.get_data():
                return index
            else:
                current = current.get_next()
        return None

    def insert(self, pos, item):
        index = -1
        current = self.head
        previous = self.head

        if previous is None:
            temp = Node(item)
            temp.set_next(current)
            self.head = temp
        else:
            while previous is not None:
                index += 1
                print("index = ", index)
                if index == pos:
                    temp = Node(item)
                    temp.set_next(current)
                    previous.set_next(temp)
                    break
                else:
                    previous = current
                    if previous is not None:
                        current = current.get_next()

    def pop(self):
        current = self.head
        previous = self.head
        data = None
        while current is not None:
            if current.get_next() is None:
                data = current.get_data()
                current = None
                previous.set_next(None)
            else:
                previous = current
                current = current.get_next()
        return data

    def search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count


if __name__ == "__main__":
    u_list = UnorderedList()
    u_list.add(12)
    u_list.add(3)
    u_list.add(4)
    u_list.append(1)
    print("pop", u_list.pop())
    print("index", u_list.index(1))
    u_list.insert(3, 9)

    c = u_list.head
    while c is not None:
        print(c.get_data())
        c = c.get_next()
