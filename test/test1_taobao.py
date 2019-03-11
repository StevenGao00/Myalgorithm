#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from typing import  List, Tuple, Optional

def full_reduction(values:List[int], w:int) -> Optional:
    n = len(values)
    states = [[-1]*(3*w+1) for i in range(n)]
    states[0][0] = 1
    if values[0] <= 3*w:
        states[0][values[0]] = 1
    for i in range(1, n):
        for j in range(w*3+1):
            if states[i-1][j] >= 0:
                states[i][j] = states[i-1][j]
                if j + values[i] <= 3*w:
                    states[i][j+values[i]] = 1
    tmp = -1
    for i in range(w, 3*w+1):
        if states[n-1][i] >= 0:
            tmp = i
            break
    if tmp == -1:
        return []
    select:List[int] = []
    for i in range(n-1, 0, -1):
        if states[i-1][tmp-values[i]] >= 0 and tmp - values[i] >=0:
            select.append((i, values[i]))
            tmp = tmp - values[i]
    if tmp > 0:
        select.append((0, values[0]))
    return select



if __name__=="__main__":
    values:List[int] = [123,88,56,74,89,136,99,211]
    select = full_reduction(values, 200)
    total_price = sum([i[1] for i in select])
    print(select)
    print(total_price)