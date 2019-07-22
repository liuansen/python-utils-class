#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def heapify(nums, heap_size, root_index):
    # 设最大元素索引为根节点索引
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # 如果根节点的左子节点是有效索引， 并且元素大于当前最大元素， 则更新最大元素
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # 如果根节点的右子节点是有效索引， 并且元素大于当前最大元素， 则更新最大元素
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # 如果最大元素不再是根元素， 则交换它们
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # 调整堆以确保信的根节点元素是最大元素
        heapify(nums, heap_size, largest)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    # 我们经常使用列表的长度， 因此我们将它创建为变量方便使用
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length+right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # 我们检查每个列表的开头的哪个值最小， 如果左列表开头较小，将它添加到已排序的列表
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # 如果右列表开头的项较小， 将它添加到已排序的列表
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        # 如果已经达到左列表的末尾， 则调价右列表的元素
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # 如果已经达到右列表的末尾， 则调价左列表的元素
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


# 快速排序分区有不同的方法，下面实现了Hoare的分区方案， Tony Hoare还创建了快速排序算法
def partition(nums, low, high):
    # 我们选择中间元素作为基准值
    # 有些实现方法选择第一元素或最后一个元素为基准值
    # 有时将中间元素或一个随机元素作为基金值
    # 还有很多可以选择或者创建的方法
    pivot = nums[(low+high)//2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j

        # 如果i处的元素（在基准值左侧）大于j处的元素（在基准值的右侧），则交换它们
        nums[i], nums[j] = nums[j], nums[i]
