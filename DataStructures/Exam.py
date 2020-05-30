# coding=utf-8
# !/usr/bin/python3

# pip3 install virtualenv
# 
from timeit import Timer
from Stack import Stack


# 异序词检测


def anagram_solution(s1, s2):
    """
    清点法 O(n^2)
    """
    a_list = list(s2)
    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            a_list[pos2] = None
        else:
            still_ok = False
        pos1 = pos1 + 1
    return still_ok


def anagram_solution2(s1, s2):
    """
    计数法 O(n)
    """

    def check_sum(list):
        sum_list = [0] * 26
        for i in range(len(list)):
            pos = ord(list[i]) - ord('a')
            sum_list[pos] = sum_list[pos] + 1
        return sum_list

    c1 = check_sum(s1)
    c2 = check_sum(s2)

    j = 0
    while j < 26:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            return False
    return True


# 栈 括号匹配算法


def par_checker(string, left_rule, right_rule):
    stack = Stack()
    balanced = True
    for str in string:
        if str in left_rule:
            stack.push(str)
        else:
            if str in right_rule:
                if stack.is_empty():
                    balanced = False
                    break
                symbol = stack.pop()
                if left_rule.index(symbol) != right_rule.index(str):
                    balanced = False
                    break

    return balanced & stack.is_empty()


def binary_string(number):
    rem_stack = Stack()

    while number > 0:
        rem = number % 2
        rem_stack.push(rem)
        number = number // 2  # 保留整数除法

    bin_str = ""
    while not rem_stack.is_empty():
        bin_str += str(rem_stack.pop())
    return bin_str


def base_converter(number, base):
    if base < 2 or base > 16:
        return None
    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    while number > 0:
        rem = number % base
        rem_stack.push(rem)
        number = number // base

    c_str = ""
    while not rem_stack.is_empty():
        c_str += digits[rem_stack.pop()]
    return c_str


# 测试内容


def time_test(test, test_number, import_for):
    t = Timer(str(test), "from __main__ import " + import_for)
    print("function " + import_for + ":",
          t.timeit(number=test_number), "milliseconds")


def test_f():
    time_test(
        "anagram_solution(\"asdasdsdasdsadasdasdasdasdasdasd\",\"asdasdsdasdsadasdasdasdasdasdasd\")", 1000,
        "anagram_solution")
    time_test(
        "anagram_solution2(\"asdasdsdasdsadasdasdasdasdasdasd\",\"asdasdsdasdsadasdasdasdasdasdasd\")", 1000,
        "anagram_solution2")


if __name__ == "__main__":
    print(par_checker("({[1]+(2+3)})", "([{", ")]}"))
    print(binary_string(100))
    print(base_converter(1500, 16))
