# coding=utf-8
# !/usr/bin/python3


class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def de_queue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Deques(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def pal_checker(string):
    char_deques = Deques()
    for ch in string:
        char_deques.add_rear(ch)

    while char_deques.size() > 1:
        first = char_deques.remove_front()
        last = char_deques.remove_rear()
        if first != last:
            return False
    return True


if __name__ == "__main__":
    print(pal_checker("abcdecba"))
