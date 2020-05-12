# -*- coding:utf-8 -*-
# author：Anson
# @Time    : 2019/9/25 15:19
# @File    : example.py
from __future__ import unicode_literals

import random


temp = [i + 1 for i in range(35)]
random.shuffle(temp)
i = 0
r_list = []
while i < 7:
    r_list.append(temp[i])
    i = i + 1
r_list.sort()
print(*r_list[0:6], end="")
print('\t', end=" ")
print(r_list[-1])
