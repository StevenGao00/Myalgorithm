#/usr/bin/env python3
# -*- coding:utf-8 -*-

def minDistBT_re(i, j, dist, w, n):
    minDist = float('inf')
    def minDistBT(i, j, dist, w, n):
        if i==n-1 and j==n-1:
            nonlocal minDist
            if dist < minDist:
                minDist = dist
        if i < n-1:
            minDistBT(i+1, j, dist+w[i+1][j], w, n)
        if j < n-1:
            minDistBT(i, j+1,dist+w[i][j+1], w, n)
    minDistBT(i, j, dist, w, n)
    return minDist

if __name__=='__main__':
    w = [[1,3,5,9],
         [2,1,3,4],
         [5,2,6,7],
         [6,8,4,3]]
    min_Dist = minDistBT_re(0,0,1,w,4)
    print(min_Dist)
