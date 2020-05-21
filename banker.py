# coding=utf-8
#!/usr/bin/python3


class DijkstraBanker(object):

    def __init__(self):

        message = "可执行的命令:\n1.初始化系统资源\n2.初始化进程信息\n3.模拟分配资源\n0.退出\n请输入要执行的命令: "

        self.res = (['A', 'B', 'C'], [5, 4, 3])
        self.process = [('P1', [[0, 0, 0], [1, 2, 3], [0, 0, 0]]),
                        ('P2', [[0, 0, 0], [2, 3, 4], [0, 0, 0]])]

        # self.res = None
        # self.process = None

        select = 1

        while select != 0:
            select = int(input(message))

            if select == 1:
                self.res = self.set_system_resources()
                print(self.res)

            if select == 2:
                if self.res is None:
                    print("\n----系统资源未初始化！----\n")
                else:
                    self.process = self.set_process_info()

            if select == 3:
                if self.process is None:
                    print("\n----进程信息未初始化！----\n")
                else:
                    self.distribution()

    def set_system_resources(self):
        count = int(input("请输入系统可用种类个数:"))
        resources_name = []
        resources_count = []
        for i in range(1, count+1):
            res_name = input("请输入第%d个资源的名称:" % i).upper()
            res_num = int(input("请输入第%d个资源的数量:" % i))
            resources_name.append(res_name)
            resources_count.append(res_num)
        return (resources_name, resources_count)

    def set_process_info(self):

        count = int(input("请输入进程总个数:"))
        process = []
        for i in range(1, count+1):

            process_name = "P" + str(i)
            # info下标分别为 0目前占有量 1最大需求量 2剩余需求量
            process_info = [[0 for i in range(len(self.res))]
                            for j in range(3)]
            print(process_info)

            for index, item in enumerate(process_info[1]):
                res_name = self.res[index][0]
                res_count = self.res[index][1]

                process_req = int(
                    input("\n请输入进程 %s 对 %s 资源的最大需求数量:" % (process_name, res_name)))

                if process_req > res_count:
                    print("最大需求数量超过系统资源数量,初始化失败!\n")
                    return None

                process_info[1][index] = process_req
                process_info[2][index] = process_req

            process.append((process_name, process_info))
        print(process)
        return process

    def distribution(self):
        process_select = int(input("请输入要分配第几个进程:"))

        pre_req = []
        for item in self.res[0]:
            name = item[0]
            num = input("请输入%s类型资源需要多少:" % name)
            pre_req.append([ame, num])
        print(pre_req)
        self.check_pre_allocation(process_select, pre_req)

    def check_pre_allocation(self, process_no, pre_res):

        pending_process = self.process[process_no]
        p_employ = pending_process[1][0]
        p_max = pending_process[1][1]
        # 检查占用资源和申请资源是否超过该进程最大资源需求量
        p_sum = [p_employ[i] + pre_res[i] for i in range(len(pre_res))]
        print(p_sum)
        pending_process[1][0]
        # 检查系统剩余资源是否满足分配要求



if __name__ == "__main__":
    # DijkstraBanker()
    a = [3,2,1,5,7,8,9,0]
    for index,item in enumerate(a):
        min_i = index
        for i in range(index+1, len(a)):
            print(i)
            if a[i] < a[min_i]:
                min_i = i
        temp = a[index]
        a[index] = a[min_i]
        a[min_i] = temp 
    print(a)
