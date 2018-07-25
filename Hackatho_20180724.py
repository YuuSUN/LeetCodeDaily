#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:59:02 2018

@author: lifanhong

50+69+274+162+205/242
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1:
            return x
        if n == 0 or x == 1:
            return 1
        if x == -1:
           return -1 if n % 2 == 1 else 1
        if n < 0:
            return self.myPow(1/x,-n)
        else:
            out = 1
            for i in range(n):
                out *= x
                if -0.00001 < out < 0.00001:
                    return 0
            return out
#            
#print(Solution().myPow(-1,2222))
    
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, up = 0, x
        while low <= up:
            mid = (low + up) // 2
            if mid ** 2 <= x < (mid+1) ** 2:
                return mid
            elif x >= (mid + 1) ** 2:
                low = mid + 1
            else:
                up = mid
        
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = len(citations)
        while h > 0:
            cite = 0
            for i, item in enumerate(citations):
                if item >= h:
                    cite += 1
            if cite >= h:
                return h
            h -= 1
        return 0
    
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        pass
        
        
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i+1] < nums[i]:
                    return i
            elif 0 < i < len(nums) - 1:
                if nums[i-1] < nums[i] and nums[i+1]<nums[i]:
                    return i
            else:
                if nums[i-1]<nums[i]:
                    return i
        
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """    
        
        
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """    
        return True if self.word_comp(s) == self.word_comp(t) else False
    
    def word_comp(self, word):
        alpha = dict()
        for i,item in enumerate(word):
            if item not in alpha:
                alpha[item] = 1
            else:
                alpha[item] += 1
        return alpha
        
#print(Solution().isAnagram("anagram","nagaram"))  
        
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """    
        s2t = dict()
        used = dict()
        for i, char in enumerate(s):
            if char not in s2t:
                if t[i] in used:
                    return False
                s2t[char] = t[i]
                used[t[i]] = 1
            else:
                if s2t[char] != t[i]:
                    return False
        return True
        
    
    

        
        
        
        
        
        
        
        
        
    