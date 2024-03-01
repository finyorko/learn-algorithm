from sort import test_is_sorted, generate_random_list
from sort import Stack


def partition1(arr, start, end):
    # 挖洞法
    # start, end代表列表开始和结束位置
    # left, right代表移动的左右指针
    if start >= end:
        return start
    left = start
    right = end
    pivot = arr[start]
    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot
    return left


def partition2(arr, start, end):
    # 左右指针法
    left = start
    right = end
    temp = arr[right]
    if left >= end:
        return left
    while left < right:
        # 要注意需要判断相等，不然不会继续进行
        # 从左边开始找大的
        while left < right and arr[left] <= temp:
            left += 1
        # 从右边开始找小的
        while left < right and arr[right] >= temp:
            right -= 1
        # 交换
        arr[left], arr[right] = arr[right], arr[left]
    # 最后left=right时的值一定比temp大，交换
    arr[left], arr[end] = arr[end], arr[left]
    return left


def partition3(array, start, end):
    # 单向扫描法（算法导论中的partition函数）
    temp = array[end]
    i = start - 1
    for j in range(start, end):
        # [i+1, j)都是比基准大的数
        if array[j] <= temp:
            # 在循环中，i一直指向左边已排序序列的最右边元素
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    # 返回基准值的位置
    return i + 1


def quick_sort(array, start, end):
    if start < end:
        q = partition2(array, start, end)
        quick_sort(array, start, q - 1)
        quick_sort(array, q + 1, end)


# 迭代法快速排序，partition通用
def quick_sort_iteration(arr):
    left = 0
    right = len(arr) - 1
    if left >= right:
        return
    piviots = [(left, right)]
    while len(piviots) > 0:
        piviot = piviots.pop(0)
        if piviot[0] < piviot[1]:
            # 相当于排序[left, right]
            piviot_num = partition1(arr, piviot[0], piviot[1])
            # 相当于排序[left,piviot_num-1]
            if piviot_num - 1 > piviot[0]:
                piviots.append((piviot[0], piviot_num - 1))
            # 相当于排序[piviot_num + 1, right]
            if piviot_num + 1 < piviot[1]:
                piviots.append((piviot_num + 1, piviot[1]))


# 利用栈实现，和quick_sort_iteration一个道理
def quick_sort_iter_stack(arr):
    start = 0
    end = len(arr) - 1
    if start >= end:
        return
    test_stack = Stack()
    test_stack.push(start)
    test_stack.push(end)
    while not test_stack.is_empty():
        right = test_stack.pop()
        left = test_stack.pop()
        piviot_num = partition1(arr, left, right)
        if piviot_num - 1 > left:
            test_stack.push(left)
            test_stack.push(piviot_num - 1)
        if piviot_num + 1 < right:
            test_stack.push(piviot_num + 1)
            test_stack.push(right)


if __name__ == '__main__':
    test_arr = [1, 12, 15, 5, 4, 6, 8, 7, 31, 46, 32]
    # arr = generate_random_list(100, 100)
    # quick_sort_iter_stack(test_arr)
    quick_sort(test_arr, 0, len(test_arr) - 1)
    print(test_arr)
