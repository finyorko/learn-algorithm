# 冒泡排序
# 平均时间复杂度：O(n2)
# 最好时间复杂度：O(n2)  可以降到O(n):已经排好序的情况下，增加一个标志位来实现
# 最坏时间复杂度：O(n2)
# 空间复杂度：O(1)
# 稳定性：稳定


def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_best(arr):
    # flag=1代表需要交换
    flag = 0
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            # i=1时，j全部走一遍，出现未排好顺序的情况，flag会置为1，只进行了n-1次，所以时间复杂度为O(n)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if flag == 0:
            return arr
    return arr


if __name__ == '__main__':
    test_arr = [1, 12, 15, 5, 4, 6, 8, 7, 31, 46, 32]
    tmp_arr = bubble_sort(test_arr)
    print(tmp_arr)
