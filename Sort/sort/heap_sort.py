# 堆排序
# https://www.runoob.com/python3/python-heap-sort.html
# 第一步：先倒序构建大顶堆
# 构建完成之后，堆顶和堆尾交换，将最大值踢出
# 后面就一直一个一个换到最后
import math


def heap_sort(arr):
    build_max_heap(arr)
    arr_len = len(arr)
    # 每一次拿出最大堆的堆顶放到队列尾部
    for i in range(arr_len-1, 0, -1):
        # 此时最大元素已经在堆顶，先交换
        arr[0], arr[i] = arr[i], arr[0]
        # 第一次处理时：i=arr_len-1, 处理i个数据,因为最后一个元素已经是最大
        # 第一次处理时：i=arr_len-2, 处理i个数据，因为最后两个元素已经是最大
        heapify(arr, i, 0)
    return arr


# 开始构建大顶堆
def build_max_heap(arr):
    arr_len = len(arr)
    # 建立最大堆
    for i in range((arr_len - 1) // 2, -1, -1):
        heapify(arr, arr_len, i)


# 每一次维护最大堆的属性
def heapify(arr, n, i):
    # n: 未处理的堆的数组长度（此数组后面时已经交换完成的最大值）
    # i: 当前需要维护的堆顶点位置
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and arr[left] > arr[i]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


if __name__ == '__main__':
    test_arr = [1, 12, 15, 5, 4, 6, 8, 7, 31, 46, 32]
    heap_sort(test_arr)
    print(test_arr)
