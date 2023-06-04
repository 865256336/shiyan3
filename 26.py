
from typing import List

def selection_sort(arr: List[int]):

    length = len(arr)
    if length <= 1:
        return

    for i in range(length):
        min_index = i
        min_val = arr[i]
        for j in range(i, length):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    import random
    random.seed(54)
    arr = [random.randint(0,100) for _ in range(10)]
    print("原始数据：", arr)
    selection_sort(arr)
    print("选择排序结果：", arr)
