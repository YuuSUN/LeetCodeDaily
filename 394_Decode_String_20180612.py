#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:55:44 2018

@author: lifanhong

Example
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

failed test case:
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef", return "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
s = "100[leetcode]"
    
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        rep = 0
        recursion = -1
        for i in range(len(s)):
            if i <= recursion:
                continue
            if s[i].isdigit():
                if rep == 0:
                    rep = int(s[i])
                else:
                    rep = rep * 10 + int(s[i])
            elif s[i] == "[":
                column = {"[":0,"]":0}
                for j in  range(i,len(s)):
                    if s[j] == "[":
                        column["["] += 1
                    elif s[j] == "]":
                        column["]"] += 1
                    if column["["] == column["]"] and column["["] != 0:
                        break
                output = output + rep * Solution().decodeString(s[i + 1:j])
                rep = 0
                recursion = j
            if i <= recursion:
                continue
            elif s[i].isalpha():
                output = output + s[i]
        return output

print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))