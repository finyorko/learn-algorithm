from sort import generate_random_list


# 计数排序稳定
# 局限性：1.当数列最大最小值差距过大时；2.当数列元素不是整数时
# 时间复杂度：O(N+k)
# 空间复杂度：O(k)
def counting_sort(arr):
    # 先寻找最小值，最大值
    min_num = min(arr)
    max_num = max(arr)
    len_arr = len(arr)
    # 索引数组初始化全零，长度为max_arr-min_arr + 1
    arr_index = [0] * (max_num-min_num + 1)
    # 初始化结果数组为全零，长度和需要排序的数组长度保持一致
    arr_result = [0]*len_arr
    # 先统计每个数字的个数，存在对应的索引下
    for i in range(len_arr):
        arr_index[arr[i] - min_num] += 1
    # 构建新索引数组，为了保持稳定性
    for i in range(1, len(arr_index)):
        arr_index[i] += arr_index[i - 1]
    # 倒序遍历，能通过arr_index能查到旧数组当前元素对应的位置是第几个（索引需要-1才行，因为从0开始）
    for i in range(len_arr-1, -1, -1):
        # 拿到当前元素
        item = arr[i]
        # 对应索引需要-1，后面匹配到相同的需要继续减
        arr_index[item-min_num] -= 1
        curr_index = arr_index[item-min_num]
        arr_result[curr_index] = item
    return arr_result


if __name__ == '__main__':
    test_arr = generate_random_list(10, 20)
    print(test_arr)
    result = counting_sort(test_arr)
    print(result)
