#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/9/29 18:31 2019

@author : json
"""

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            raise LookupError('stack is empty!')

    def is_empty(self):
        return bool(self.stack)

    def top(self):
        return self.stack[-1]