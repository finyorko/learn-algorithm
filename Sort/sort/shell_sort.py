# 希尔排序
# 平均时间复杂度：O(nlogn)
# 最好时间复杂度：O(n(logn)2)
# 最坏时间复杂度：O(n(logn)2)
# 空间复杂度：O(1)
# 稳定性：不稳定


def shell_sort(arr):
    arr_len = len(arr)
    # 设置初始步长
    gap = int(arr_len / 2)
    while gap > 0:
        # 其实就是按照步长进行插入排序
        for i in range(gap, arr_len):
            # 插入排序
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = int(gap / 2)
    return arr


if __name__ == '__main__':
    test_arr = [1, 12, 15, 5, 4, 6, 8, 7, 31, 46, 32]
    tmp_arr = shell_sort(test_arr)
    print(tmp_arr)
