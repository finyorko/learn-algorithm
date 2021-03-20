import math


def merge(left, right):
    # 合并操作，将两个有序数组合并成一个大的数组
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


# 递归实现
def merge_sort_recursion(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    middle = math.floor(len(arr) / 2)
    merge_left = merge_sort_recursion(arr[0:middle])
    merge_right = merge_sort_recursion(arr[middle:])
    # 合并
    return merge(merge_left, merge_right)


# 迭代实现
def merge_sort_iteration(arr):
    arr_len = len(arr)
    # 每次的步长，1，2，4，···，直到超过arr_len
    i = 1
    while i < arr_len:
        # left_start为每一次处理的第一个数组的开始位置，每次处理两个数组
        # 处理完两个数组后，向列表后移动两个步长，继续处理两个数组，直到列表最后
        left_start = 0
        while left_start < arr_len - i:
            left_end = left_start + i
            right_start = left_end
            right_end = right_start + i
            if right_end > arr_len:
                right_end = arr_len
            left_arr = arr[left_start:left_end]
            right_arr = arr[right_start:right_end]
            merge_result = merge(left_arr, right_arr)
            arr[left_start:right_end] = merge_result
            left_start += i * 2
        i *= 2
    return arr


if __name__ == '__main__':
    test_arr = [1, 12, 15, 5, 4, 6, 8, 7, 31, 46, 32]
    tmp_arr = merge_sort_recursion(test_arr)
    print(tmp_arr)
    tmp_arr = merge_sort_iteration(test_arr)
    print(tmp_arr)
