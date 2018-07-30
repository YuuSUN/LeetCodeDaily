#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 19:52:47 2018

@author: lifanhong
"""

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = ['a','e','i','o','u','A','E','I','O','U']
        vsaver = []
        pos = []
        for i,char in enumerate(s):
            if char in v:
                vsaver.append(char)
                pos.append(i)
        vsaver.reverse()
        out = list(s)
#        print(out)
        for i,char in enumerate(vsaver):
#            print(i,char)
            out[pos[i]] = char
        return "".join(out)

print(Solution().reverseVowels("hello"))