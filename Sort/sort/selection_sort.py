def selection_sort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引,初始时选择第i个
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # i 不是最小数时，将 i 和最小数进行交换
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


if __name__ == '__main__':
    test_arr = [1, 12, 15, 5, 4, 6, 8, 7, 31, 46, 32]
    tmp_arr = selection_sort(test_arr)
    print(tmp_arr)
