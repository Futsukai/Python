# coding=utf-8
#!/usr/bin/python3

def binarySearch(list, item):
    first = 0
    last = len(list) - 1
    found = False
    count = 0
    while first <= last and not found:
        count += 1
        mid = (first + last) // 2
        print("mid", mid)

        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    print("次数", count)
    return found


l = [i for i in range(1, 1000)]
n = 100
print(binarySearch(l, n))


def bubble_sort(list_s):
    for pass_num in range(len(list_s)-1, 0, -1):
        exchanges = False
        # 修正为短冒泡排序,如果一趟循环下没有发生交换，则认为排序完成
        for i in range(pass_num):
            if list_s[i] > list_s[i+1]:
                exchanges = True
                list_s[i], list_s[i+1] = list_s[i+1], list_s[i]
        if not exchanges:
            break


def quick_sort(list_s):
    if len(list_s) < 2:
        return list_s
    else:
        pivot = list_s[0]
        less = [i for i in list_s[1:] if i <= pivot]
        greater = [i for i in list_s[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


t = [9999, 3, 4, 1, 5, 6, 61, 33, 422, 51, 1, 3,
     4, 5, 67, 8, 9, 56, 45, 3, 12, 32, 11, 0, 1]
f = quick_sort(t)
print(f)
