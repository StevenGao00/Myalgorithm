#/usr/bin/env python3
# -*- coding: utf-8 -*-

def insertSort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        cur = arr[i]
        while preIndex >= 0 and arr[preIndex] > cur:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = cur

if __name__=="__main__":
    List = [-10,1,3,1,4,10,3,9,4,5,1]
    insertSort(List)
    print(List)
    print(List[-7])

