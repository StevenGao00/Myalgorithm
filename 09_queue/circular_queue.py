#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
circular Queue based upon array
"""
from typing import Optional
from itertools import chain

class CircularQueue:
    def __init__(self, capacity:int):
        self._capacity = capacity+1   # 默认最后一个不存储数据，浪费一个存储空间
        self._items = [None]*self._capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item:str) -> bool:
        if (self._tail+1) % self._capacity == self._head:   # 队满
            return False
        self._items[self._tail] = item
        self._tail = (self._tail+1) % self._capacity
        return True

    def dequeue(self) -> str:
        if self._head != self._tail:
            item =  self._items[self._head]
            self._head = (self._head+1) % self._capacity
            return  item

    def __repr__(self) -> str:
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head:self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))

if __name__ == "__main__":
    q = CircularQueue(10)
    for i in range(15):
        q.enqueue(str(i))
    print(q)
    q.dequeue()
    q.dequeue()
    print(q)
    q.enqueue(str(88))
    q.enqueue(str(99))
    q.enqueue(str(77))
    q.dequeue()
    q.enqueue(str(66))
    q.enqueue('a')
    print(q)