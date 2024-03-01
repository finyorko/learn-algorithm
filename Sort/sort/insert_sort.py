# 插入排序
# 平均时间复杂度：O(n2)
# 最好时间复杂度：O(n)
# 最坏时间复杂度：O(n2)
# 空间复杂度：O(1)
# 稳定性：稳定


def insert_sort(arr):
    # 需要进行n-1次排序
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        # 如果arr[j] > temp，则arr[j]后移，直到结束
        # 最好时间复杂度分析：如果一开始有序，则下面的循环不会进入，所以只会有最外面一层循环，时间复杂度为O(n)
        while j > 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        # 此时arr[j] < temp, arr[j]后面一位为temp
        arr[j + 1] = temp
    return arr


if __name__ == '__main__':
    test_arr = [1, 12, 15, 5, 4, 6, 8, 7, 31, 46, 32]
    tmp_arr = insert_sort(test_arr)
    print(tmp_arr)
