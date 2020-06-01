# coding=utf-8
#!/usr/bin/python3

class Base(object): # make sure to inherit from object for super to work
    A = False
    B = 'bbb'
    C = 'ccc'

    def __iter__(self):
        yield 'a', self.A
        yield 'b', self.B
        yield 'c', self.C

class Data(Base):
    D = ''

    def __iter__(self):
        for x in super(Data, self).__iter__():
            yield x
        yield 'd', self.D


d = Data()

for i in d:
    print(i)