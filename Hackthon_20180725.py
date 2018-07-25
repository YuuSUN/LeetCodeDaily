#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:40:06 2018

@author: lifanhong

59+371+447+263+
"""

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.n = n
        self.next = 1
        self.mat = [[0 for i in range(n)] for i in range(n)]
        self.fillnext(0,0)
        return self.mat
        
    def fillnext(self,y,x):
        """
        when entering this function the point y,x is already
        sure to be put, so first do it
        """
        self.mat[y][x] = self.next
        if self.next == self.n * self.n:
            return
        self.next += 1
        if (x == 0 or self.mat[y][x - 1] != 0) and y != 0 and self.mat[y - 1][x] == 0:
            return self.fillnext(y - 1, x)
        elif x != self.n - 1 and self.mat[y][x + 1] == 0:
            return self.fillnext(y, x + 1)
        elif x == self.n - 1 or self.mat[y][x + 1] != 0:
            if y != self.n - 1 and self.mat[y + 1][x] == 0:
                return self.fillnext(y + 1, x)
            elif y == self.n - 1 or self.mat[y + 1][x] != 0:
                if x != 0 or self.mat[y][x - 1] == 0:
                    return self.fillnext(y, x - 1)
                elif x == 0 or self.mat[y][x - 1] != 0:
                    if self.mat[y - 1][x] == 0:
                        return self.fillnext(y - 1, x)
                    else:
                        return
        
#print(Solution().generateMatrix(6))

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in points:
            c = 0
            d = {}
            for j in points:
                dis = (j[0]-i[0])**2+(j[1]-i[1])**2
                if dis not in d:
                    d[dis] = 1
                else:
                    c += d[dis]
                    d[dis] += 1
            res += c
        return res * 2

#print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))                
                
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num % 5 == 0:
            num /= 5
        while num % 3 == 0:
            num /= 3
        while num % 2 == 0:
            num /= 2
        return False if num not in [1,2,3,5] else True
                
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        insert = []
        for i,char in enumerate(chars):
            if i != 0 and char != chars[i - 1]:
                insert.append(i)
        insert.append(len(chars))
        insert.reverse()
        insert.append(0)
        for i in range(len(insert) - 1):
            up = insert[i]
            low = insert[i+1]
            del chars[low + 1:up]
            chars[low+1:low+1] = list(str(up-low))
        return chars

print(Solution().compress(["a","a","b","b","c","c","c"]))
            
            
                
            
            
                        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                