# coding=utf-8
#!/usr/bin/python3
from turtle import *


def tree(branch_Len, t):
    if branch_Len > 5:
        t.forward(branch_Len)
        t.right(20)
        tree(branch_Len-15, t)
        t.left(40)
        tree(branch_Len-10, t)
        t.right(20)
        t.backward(branch_Len)


t = Turtle()
my_win = t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color("green")
tree(110, t)
my_win.extionclick()
