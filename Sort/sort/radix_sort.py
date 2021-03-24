from sort import generate_random_list


# 基数排序，同样利用了桶，存整数位，
def radix_sort_lsd(arr):
    # 计算最大值的位数，循环次数和位数保持一致
    max_value_digit = len(str(max(arr)))
    # for k in range(max_value_digit-1, -1, -1):
    for k in range(max_value_digit):
        # 生成10个列表
        print("第{}轮".format(k))
        bucket_list = [[] for i in range(10)]
        for i in arr:
            bucket_list[i // (10 ** k) % 10].append(i)
        for i in bucket_list:
            print(i)
        arr = []
        for i in bucket_list:
            for j in i:
                arr.append(j)
        # arr = [j for i in bucket_list for j in i]
    # for i in bucket_list:
    #     print(i)
    # print(bucket_list)
    return arr


def radix_sort_msd(arr):
    max_num = max(arr)
    # digit代表当前位数
    digit = len(str(max_num))
    bucket_list = [[] for i in range(10)]
    for i in arr:
        # 向bucket0-1中添加数组
        bucket_list[i // (10 ** (digit - 1)) % 10].append(i)
        for bucket_item in bucket_list:
            if len(bucket_item) > 1:
                radix_sort_msd(bucket_item)
    return arr


if __name__ == '__main__':
    # test_arr = [17, 56, 71, 38, 61, 62, 48, 28, 57, 42]
    test_arr = generate_random_list(100, 10)
    print(test_arr)
    # result = radix_sort_lsd(test_arr)
    result = radix_sort_lsd(test_arr)
    print('result')
    print(result)
