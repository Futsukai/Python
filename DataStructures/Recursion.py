# coding=utf-8
#!/usr/bin/python3

"""
递归三原则:
(1) 递归算法必须有基本情况;
(2) 递归算法必须改变其状态并向基本情况靠近;
(3) 递归算法必须递归地调用自己。
"""

from Stack import Stack


def to_str(n, base):
    convert_str = "0123456789ABCDEF"
    if n < base:
        return convert_str[n]
    else:
        return to_str(n // base, base) + convert_str[n % base]


r_stack = Stack()


def to_str_stack(n, base):
    # 调用栈的显式调用，返回值
    convert_str = "0123456789ABCDEF"
    if n < base:
        r_stack.push(convert_str[n])
    else:
        r_stack.push(convert_str[n % base])
        to_str_stack(n // base, base)


if __name__ == "__main__":
    t = to_str(100, 2)
    print(t)

    to_str_stack(100, 2)
    s = r_stack.pop()
    while not r_stack.is_empty():
        s += r_stack.pop()
    print("stack:", s)
