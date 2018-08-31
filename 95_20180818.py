#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:46:22 2018

@author: lifanhong
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
#    def generateTrees(self, n):
#        """
#        :type n: int
#        :rtype: List[TreeNode]
#        """
#        def dfs(l,r):
#            if r<l:
#                return [None]
#            out = []
#            for m in range(l,r+1):
#                left = dfs(l,m-1)
#                right = dfs(m+1,r)
#                for lnode in left:
#                    for rnode in right:
#                        new = TreeNode(m)
#                        new.left = lnode
#                        new.right = rnode
#                        out.append(new)
#            return out
#        res = dfs(1,n)
#        return [] if res == [None] else res

#    def generateTrees(self, n):
#        def dfs(l, r):
#            if r < l: return [None]
#            arr = []
#            for m in range(l, r + 1):
#                left = dfs(l, m - 1)
#                right = dfs(m + 1, r)
#                for lNode in left:
#                    for rNode in right:
#                        new = TreeNode(m)
#                        new.left = lNode
#                        new.right = rNode
#                        arr.append(new)
#            return arr
#        res = dfs(1, n)
#        return [] if res == [None] else res
#            
#        if n == 0:
#            return []
#        return self.dfs(1,n)
        

    def generateTrees(self, n):
        if n == 0:
            return []
        return self.dfs(1,n)

    def dfs(self, l, r):
        """
        :type l, r: int
        :rtype: List[TreeNode]
        """
        if r < l:
            return [None]
        out = []
        for m in range(l,r+1):
            left = self.dfs(l,m-1)
            right = self.dfs(m+1,r)
            for lnode in left:
                for rnode in right:
                    new = TreeNode(m)
                    new.left = lnode
                    new.right = rnode
                    out.append(new)
        return out



print(Solution().generateTrees(3))
#print(Solution().dfs(1,2))