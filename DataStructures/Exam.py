# coding=utf-8
#!/usr/bin/python3

from timeit import Timer

from Stack import Stack
# 异序词检测


def anagram_solution(s1, s2):
    """
    清点法 O(n^2)
    """
    alist = list(s2)
    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
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

# 括号匹配算法


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


# 测试内容

    def test(self):
        t1 = Timer("anagram_solution(\"asdasdsdasdsadasdasdasdasdasdasd\",\"asdasdsdasdsadasdasdasdasdasdasd\")",
                   "from __main__ import anagram_solution")
        print("concat ", t1.timeit(number=1000), "milliseconds")

        t2 = Timer("anagram_solution2(\"asdasdsdasdsadasdasdasdasdasdasd\",\"asdasdsdasdsadasdasdasdasdasdasd\")",
                   "from __main__ import anagram_solution2")
        print("concat ", t2.timeit(number=1000), "milliseconds")


if __name__ == "__main__":
    print(par_checker("({[1]+(2+3)})", "([{", ")]}"))
