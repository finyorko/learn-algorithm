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
    for i in range(arr_len - 1, 0, -1):
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
# 递归方式
def heapify_recursion(arr, n, i):
    # n: 未处理的堆的数组长度（此数组后面为已经交换完成的最大值）
    # i: 当前需要维护的堆顶点位置
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and arr[left] > arr[i]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        # 这里代表最大元素为子节点，需要继续对子节点维护大顶堆的性质
        arr[largest], arr[i] = arr[i], arr[largest]
        # 这里有一个递归，对处理的子节点继续处理，维护最大堆的属性
        heapify(arr, n, largest)


# 迭代方式，维护最大堆的属性
def heapify(arr, n, i):
    # n: 未处理的堆的数组长度（此数组后面为已经交换完成的最大值）
    # i: 当前需要维护的堆顶点位置
    # j表示i的左孩子
    j = 2 * i + 1
    while j < n:
        if j < n - 1:
            if arr[j] < arr[j + 1]:
                j = j + 1
        if arr[i] >= arr[j]:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i = j
            j = j * 2 + 1


if __name__ == '__main__':
    test_arr = [1, 12, 15, 5, 4, 6, 8, 7, 31, 46, 32]
    arr = [36, 18, 31, 16, 11, 21, 2, 13, 3, 81]
    build_max_heap(arr)
    print(arr)
    # heap_sort(test_arr)
    # print(test_arr)
