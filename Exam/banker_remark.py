# coding=utf-8
#!/usr/bin/python3


class Res(object):

    def __init__(self, names=[], nums=[]):
        self.names = names.copy()
        self.nums = nums.copy()

    def is_empty(self):
        if len(self.names) == 0 or len(self.nums) == 0:
            return True
        return False

    def copy(self):
        t = Res()
        t.names += self.names
        t.nums += self.nums
        return t

    def check_negative(self):
        for item in self.nums:
            if item < 0:
                return True
        return False

    def of_sum(self):
        return sum(self.nums)

    def __add__(self, other):
        n = [self.nums[i] + other.nums[i] for i in range(len(self.nums))]
        return Res(names=self.names, nums=n)

    def __sub__(self, other):
        n = [self.nums[i] - other.nums[i] for i in range(len(self.nums))]
        return Res(names=self.names, nums=n)

    def __str__(self):
        text = ""
        if self.is_empty():
            return text
        for index, item in enumerate(self.names):
            text += str(item) + ":" + str(self.nums[index]) + " "
        return text


class Sys(object):
    def __init__(self):
        self.res = Res()
        self.name = "系统剩余资源"

    def is_empty(self):
        return self.res.is_empty()

    def __str__(self):
        return "%s: %s" % (self.name, self.res)


class Process(object):

    def __init__(self, name, max_res=Res()):
        self.name = name
        self.employ_res = max_res.copy()
        self.employ_res.nums = [0] * len(max_res.names)
        self.max_res = max_res
        self.need_res = max_res.copy()

    def copy(self):
        t = Process(self.name)
        t.employ_res = self.employ_res
        t.max_res = self.max_res
        t.need_res = self.need_res
        return t

    def __str__(self):
        return "进程 %s:目前占有量:%s 最大需求量:%s 剩余需求量:%s" % (
            self.name,
            self.employ_res,
            self.max_res,
            self.need_res
        )


class DijkstraBanker(object):

    def __init__(self):

        message = "可执行的命令:\n1.初始化系统资源\n2.初始化进程信息\n3.模拟分配资源\n4.查看当前状态\n0.退出\n请输入要执行的命令: "
        select = 1
        self.sys = Sys()
        self.process_queue = []
        # self.sys.res = Res(names=["A"], nums=[9])
        # self.process_queue.append(
        #     Process("P1", Res(names=["A"], nums=[5])))
        # self.process_queue.append(
        #     Process("P2", Res(names=["A"], nums=[5])))
        # self.process_queue.append(
        #     Process("P3", Res(names=["A"], nums=[5])))
        # self.process_queue.append(
        #     Process("P4", Res(names=["A"], nums=[5])))
        # self.process_queue.append(
        #     Process("P5", Res(names=["A"], nums=[5])))

        while select != "0":
            select = input(message)
            print("\n")
            if select == "1":
                self.set_system_resources()

            if select == "2":
                print(self.sys)
                if self.sys.res.is_empty():
                    self.print_line("\n----系统资源未初始化----\n")
                else:
                    self.set_process_info()

            if select == "3":
                if len(self.process_queue) == 0:
                    self.print_line("\n----进程信息未初始化----\n")
                else:
                    self.distribution()

            if select == "4":
                self.print_status()

    def set_system_resources(self):
        count = int(input("请输入系统可用种类个数:"))
        self.sys = Sys()
        for i in range(1, count+1):
            res_name = input("请输入第%d个资源的名称:" % i).upper()
            res_num = int(input("请输入第%d个资源的数量:" % i))
            self.sys.res.names.append(res_name)
            self.sys.res.nums.append(res_num)
        self.print_line("系统初始化完成!")

    def set_process_info(self):
        count = int(input("请输入进程总个数:"))
        self.process_queue = []
        for i in range(1, count+1):
            process_name = "P" + str(i)
            res = Res()

            for index, item in enumerate(self.sys.res.names):
                process_req = int(
                    input("\n请输入进程 %s 对 %s 资源的最大需求数量:" % (process_name, item))
                )
                if process_req > self.sys.res.nums[index]:
                    print("最大需求数量超过系统资源数量,初始化失败!\n")
                    return
                res.names.append(item)
                res.nums.append(process_req)

            self.process_queue.append(Process(process_name, max_res=res))
        self.print_line("\n进程初始化完成!")

    def distribution(self):
        process_select = int(input("请输入要分配第几个进程:"))
        process_select -= 1
        pre_res = Res()
        pre_process = self.process_queue[process_select]
        for index, item in enumerate(pre_process.max_res.names):
            num = int(input("请输入%s类型资源需要多少:" % item))
            pre_res.names.append(item)
            pre_res.nums.append(num)

        self.print_status()
        self.print_line("预分配%s进程\n%s" % (pre_process.name, pre_res))

        # 检查占用资源和申请资源是否超过该进程最大资源需求量
        check_res = pre_process.max_res - (pre_process.employ_res + pre_res)
        if check_res.check_negative():
            self.print_line("申请超载!")
            return

        # 检查系统剩余资源是否满足分配要求
        check_res = self.sys.res - pre_res
        if check_res.check_negative():
            self.print_line("系统资源不足!")
            return

        # 检查系统进程安全性
        test_queue = []
        for item in self.process_queue:
            test_queue.append(item.copy())
        test_process = test_queue[process_select]
        test_process.employ_res += pre_res
        test_process.need_res -= pre_res

        # 对进程资源的需求数量进行排序
        test_queue = self.sort_process_queue(test_queue)

        for i in test_queue:
            print(i)

        can_test = True
        safe_seq = []
        """检查安全性
        p为safe_seq安全序列的记录点，如果开始和结束的p值相等，表示无法满足任何一个需求，can_test设置为False,中止检查

        检查方式为:
        1.测试系统变量test_sys_res取得预分配后的剩余系统资源数

        2.在排序后的测试进程序列里，逐一检查，系统资源减去需求资源
        如果出现负数，表示无法满足该项，检查下一项是否有可能满足(of_sum()资源总和小于等于)
        结束本次循环，重新开始检查

        如果没有负数，表示满足该进程，加入安全序列记录，并将该进程的最大资源数添加到测试系统资源数

        3.当整个检查结束后，安全序列的步骤和进程序列相等的话，表示全部测试通过，系统安全
        如果不相等，表示本次预分配会导致系统不安全

        """
        while(can_test):
            p = len(safe_seq)
            test_sys_res = self.sys.res - pre_res
            for index, item in enumerate(test_queue):
                if item.name in safe_seq:
                    continue
                test_sys_res -= item.need_res
                if test_sys_res.check_negative():
                    next_index = index + 1
                    if next_index > len(test_queue) or self.sys.res.of_sum() < test_queue[next_index].need_res.of_sum():
                        break
                else:
                    success_name = item.name
                    test_sys_res += item.max_res
                    if success_name not in safe_seq:
                        safe_seq.append(success_name)

            if p == len(safe_seq):
                can_test = False

        if len(safe_seq) == len(test_queue):
            self.sys.res -= pre_res
            process = self.process_queue[process_select]
            process.employ_res += pre_res
            process.need_res -= pre_res
            print("找到安全序列", ">".join(safe_seq))
            print("分配成功!")
            self.print_status()
        else:
            self.print_line("安全性检查不通过!")

    def sort_process_queue(self, process_queue):
        """进行进程需求排序"""
        test_queue = process_queue.copy()
        for index, item in enumerate(test_queue):
            min_index = index
            for i in range(index+1, len(test_queue)):
                if test_queue[i].need_res.of_sum() < test_queue[min_index].need_res.of_sum():
                    min_index = i
            temp = test_queue[index]
            test_queue[index] = test_queue[min_index]
            test_queue[min_index] = temp
        return test_queue

    def print_line(self, text):
        text = str(text)
        print("-" * 20)
        print(text)
        print("-" * 20)

    def print_status(self):
        print("-" * 20)
        print(self.sys)
        for item in self.process_queue:
            print(item)
            if item.need_res.of_sum() == 0:
                print(">" + item.name + "进程资源满足,即将释放资源<")
                self.sys.res += item.max_res
                temp = item.need_res
                item.need_res = item.employ_res
                item.employ_res = temp
        print("-" * 20)


if __name__ == "__main__":
    DijkstraBanker()
