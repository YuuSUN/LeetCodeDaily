#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 09:43:40 2018

@author: lifanhong
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1:
            return s
        start = 0
        max_len = 1
        for i in range(1, len(s)):
            if i-max_len-1 >= 0 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            if i-max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                start = i-max_len
                max_len += 1

        return s[start:start+max_len]
                
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))