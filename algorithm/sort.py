#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

import utils as utils


# 冒泡排序法
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                # 交换元素
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True


# 选择排序
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# 插入排序
def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = item_to_insert


# 堆排序
def heap_sort(nums):
    n = len(nums)
    """
    利用列表创建一个最大堆， range的第二个参数表示我们将停在索引为-1的元素之间，既列表中的第一个元素
    range的第三个参数表示我们朝反方向迭代
    将i的值减少1
    """
    for i in range(n, -1, -1):
        utils.heapify(nums, n, 1)

    # 将最大堆的根元素移动到列表的末尾
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        utils.heapify(nums, i, 0)


# 归并排序
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return utils.merge(left_list, right_list)


# 快速排序
def quick_sort(nums):
    # 创建一个辅助函数来进行递归调用
    def _quick_sort(items, low, high):
        if low < high:
            split_index = utils.partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index+1, high)
    _quick_sort(nums, 0, len(nums)-1)


if __name__ == '__main__':
    random_list_of_nums = []
    for i in range(1000):
        random_list_of_nums.append(random.randint(1, 10000))

    # 校验冒泡排序的正确性
    bubble_sort(random_list_of_nums)
    print(random_list_of_nums)

    # 校验选择排序的正确性
    selection_sort(random_list_of_nums)
    print(random_list_of_nums)

    # 校验插入排序的正确性
    insertion_sort(random_list_of_nums)
    print(random_list_of_nums)

    # # 校验堆排序的正确性
    # heap_sort(random_list_of_nums)
    # print(random_list_of_nums)

    # 校验归并排序的正确性
    random_list_of_nums = merge_sort(random_list_of_nums)
    print(random_list_of_nums)

    # 校验快速排序的正确性
    quick_sort(random_list_of_nums)
    print(random_list_of_nums)

