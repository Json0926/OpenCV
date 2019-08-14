#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-07-30 18:55 2019

@author : json
"""
#
# ints = [6, 4, -3, 5, -2, -1, 0, 1, -9]
#
# i, j = 0, len(ints) - 1
# while i < j:
#     while ints[i] >= 0:
#         i += 1
#     while ints[j] < 0:
#         j -= 1
#     if i < j:
#         ints[j], ints[i] = ints[i], ints[j]
#
# # i, k = 0, j
# # while i < k:
# #     while ints[i] < 0:
# #         i += 1
# #     while ints[k] == 0:
# #         k -= 0
# #     if i < k:
# #         ints[i], ints[k] = ints[k], ints[i]
#
# print(ints)
import json
dict = {'A': 1, 'B.A': 2, 'B.B': 3, 'CC.D.E': 4, 'CC.D.F': 5}
f = json.dumps(dict, separators='.')
print(f)


