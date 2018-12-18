#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Queue based upon array
"""
from typing import Optional

class AarrayQueue:
    def __init__(self, capacity:int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0
    def enqueue(self, item:str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail-self._head):
                    self._items[i] = self._items[i+self._head]
                self._tail = self._tail - self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True
    def dequeue(self)->Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        return None
    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head:self._tail])

if __name__=="__main__":
    q = AarrayQueue(10)
    for i in range(0, 10):
        q.enqueue(str(i))
    q.dequeue()
    q.dequeue()
    print(q)
    q.enqueue(str(88))
    q.enqueue(str(99))
    q.enqueue(str(77))
    print(q)