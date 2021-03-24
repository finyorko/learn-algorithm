from sort import generate_random_list


def bucket_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    arr_len = len(arr)
    # 桶的大小
    bucket_range = (max_num - min_num) / arr_len
    # 生成桶数组
    bucket_list = [[] for i in range(arr_len + 1)]
    for i in arr:
        bucket_list[int((i - min_num) // bucket_range)].append(i)
    # 清空原数组
    arr = []
    for i in bucket_list:
        # i为每个桶，需要进行排序,然后将排完序的数字依次加到原数组中
        for j in sorted(i):
            arr.append(j)
    return arr


if __name__ == '__main__':
    test_arr = generate_random_list(10, 20)
    print(test_arr)
    result = bucket_sort(test_arr)
    print(result)
