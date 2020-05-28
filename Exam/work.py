# coding=utf-8
#!/usr/bin/python3

import re

class LRU(object):
    """LRU 模拟"""

    def __init__(self, num, seq):
        self.num = num
        self.seq = seq
        # 初始化内存记录单元
        self.cells = []
        # 缺页记录
        self.records = ["x"] * len(self.seq)
        # 模拟内存缓存区
        self.cache = [" "] * self.num
        self.processing()
        self.format_cells()
        self.print_string()

    def processing(self):
        for index, item in enumerate(self.seq):
            if item in self.cache:
                self.cache.pop(self.cache.index(item))
                self.cache.insert(0, item)
                self.records[index] = "o"
            else:
                self.cache.pop()
                self.cache.insert(0, item)

            self.cells.append(self.cache.copy())

    def format_cells(self):
        """内存记录单元格式化为输出横向格式"""
        temp = []
        i = 0
        while i < self.num:
            temp_content_str = ""
            for item in self.cells:
                temp_content_str += item[i]
            temp.append(temp_content_str)
            i = i+1
        self.cells = temp

    def print_string(self):
        print("内存空间为:", self.num)
        pattern = re.compile('.{1,1}')
        seq_str = '|'.join(pattern.findall(self.seq))
        print("调度序列为:")
        top_str = "|" + seq_str + "|"
        print("-" * (len(top_str)))
        print(top_str)
        print("-" * (len(top_str)))
        print("置换过程:")
        print("-" * (len(top_str)))

        for item in self.cells:
            cell_str = '|'.join(pattern.findall(item))
            con_str = "|" + cell_str + "|"
            print(con_str)
            print("-" * (len(con_str)))
        bottom_str = "|" + "|".join(self.records) + "|"
        print(bottom_str)
        print("-" * (len(bottom_str)))
        print("缺页数: ", self.records.count("x"))
        print("缺页率: %.1f%%" % (self.records.count("x") / len(self.records) * 100.0))

class main(object):
    """main"""

    def __init__(self):
        num = int(input("请输入存储区块数: "))
        seq = input("请输入作业调度序列: ")
        LRU(num, seq)
        input("Press Any Key Close")

if __name__ == '__main__':
    main()
