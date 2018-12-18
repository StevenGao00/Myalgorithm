#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
排序算法：内部排序，外部排序
常见十大经典内部排序：
    （1）冒泡排序     （6）快速排序
    （2）选择排序     （7）堆排序
    （3）插入排序     （8）计数排序
    （4）希尔排序     （9）桶排序
    （5）归并排序     （10）基数排序
'''


'''
(1) 冒泡排序
    从后向前，相邻元素两两比较。如果第一个比第二个大，就交换他们两个。
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最前的元素会是最小的数。
    针对所有的元素重复以上的步骤，除了已经冒泡到最前面的数。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''
def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        flag = True
        for j in range(len(arr)-1-1,i-1,-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]   # 先计算等号右边表达式的值再赋值给左边
                flag = False
        if flag:
            break
    return arr

'''
(2) 选择排序
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    重复第二步，直到所有元素均排序完毕。
'''
def selectionSort(arr):
    for i in range(0,  len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

'''
(3) 插入排序
    将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
    从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
    （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
'''
def insertionSort(arr):
    for i in range(len(arr)-1):
        tmp = arr[i+1]
        for j in range(i,-1,-1):
            if arr[j] > tmp:
                arr[j+1] = arr[j]
            else:
                break
        arr[j] = tmp
    return arr

if __name__=="__main__":
    List = list(range(20,0,-1))
    List1 = bubbleSort(List[:])
    List2 = selectionSort(List[:])
    List3 = insertionSort(List[:])
    print(List, '\n', List1, '\n', List2, '\n', List3)