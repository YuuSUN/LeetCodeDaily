#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:14:38 2018

@author: lifanhong

failed cases
100
01
10
"9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
"0"
"""

class Solution:
    
    d = dict()
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s in self.d.keys():
            return self.d[s]
        if not s or s[0] == '0':
            self.d[s] = 0
        elif len(s) == 1:
            self.d[s] = 1
        elif len(s) == 2:
            if 10 <= int(s) <= 26:
                if s[1] == '0':
                    self.d[s] = 1
                else:
                    self.d[s] = 2
            else:
                self.d[s] = self.numDecodings(s[1:])
        elif len(s) >= 3:
            if 10 <= int(s[:2]) <= 26:
                self.d[s] = self.numDecodings(s[2:]) + self.numDecodings(s[1:])
            else:
                self.d[s] = self.numDecodings(s[1:])
        return self.d[s]        
        
t1 = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"            
t2 = "0"
print(Solution().numDecodings(t2))