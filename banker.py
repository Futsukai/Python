# coding=utf-8
#!/usr/bin/python3


class DijkstraBanker(object):

    def __init__(self):

        message = "可执行的命令:\n1.初始化系统资源\n2.初始化进程信息\n3.模拟分配资源\n0.退出\n请输入要执行的命令: "

        self.res = [('A', 5), ('B', 4), ('C', 6)]
        self.process = [('P1', [[0, 0, 0], [1, 2, 3], [0, 0, 0]]), ('P2', [[0, 0, 0], [2, 3, 4], [0, 0, 0]])]

        # self.res = None
        # self.process = None
        
        select = 1

        while select != 0:
            select = int(input(message))

            if select == 1:
                self.res = self.set_system_resources()

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
        resources = []
        for i in range(1, count+1):
            res_name = input("请输入第%d个资源的名称:" % i).upper()
            res_num = int(input("请输入第%d个资源的数量:" % i))
            resources.append((res_name, res_num))
        print(resources)
        return resources

    def set_process_info(self):

        count = int(input("请输入进程总个数:"))
        process = []
        for i in range(1, count+1):

            process_name = "P" + str(i)
            # info下标分别为 0目前占有量 1最大需求量 2剩余需求量 
            process_info = [[0 for i in range(len(self.res))] for j in range(3)] 
            print(process_info)

            for index,item in enumerate(process_info[1]):
                res_name = self.res[index][0]
                res_count = self.res[index][1]

                process_req = int(input("\n请输入进程 %s 对 %s 资源的最大需求数量:" % (process_name, res_name)))

                if process_req > res_count :
                    print("最大需求数量超过系统资源数量,初始化失败!\n")
                    return None

                process_info[1][index] = process_req
                process_info[2][index] = process_req

            process.append((process_name, process_info))
        print(process)
        return process
    
    def distribution(self):
        process_select = int(input("请输入要分配第几个进程:"))
        process_info = self.process[process_select]
        print("")
        for target_list in expression_list:
            pass


if __name__ == "__main__":
    DijkstraBanker()
