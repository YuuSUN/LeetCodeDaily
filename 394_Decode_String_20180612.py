#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:55:44 2018

@author: lifanhong

Example
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        rep = 0
        content = ""
        record = False
        recursion = -1
        for i in range(len(s)):
            if i <= recursion:
                continue
            if s[i].isdigit() and record == False:
                #count the repeat time
                if rep == 0:
                    rep = int(s[i])
                else:
                    rep = rep * 10 + int(s[i])
            elif s[i].isdigit() and record == True:
                j = i
                column = {"[":0,"]":0}
                for j in  range(i,len(s)):
                    if s[j] == "[":
                        column["["] += 1
                    elif s[j] == "]":
                        column["]"] += 1
                    if column["["] == column["]"] and column["["] != 0:
                        break
                content = content + Solution().decodeString(s[i:j + 1])
                print(i,j)
                recurssion = j
            if i <= recursion:
                continue
            elif s[i] == "[" and record == False:
                record = True
            elif s[i].isalpha() and record == True:
                content = content + s[i]
            elif s[i].isalpha() and record == False:
                output = output + s[i]
            elif s[i] == "]" and record == True:
                record = False
                output = output + rep * content
                content = ""
                rep = 0
        return output

print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))