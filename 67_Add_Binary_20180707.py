#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 11:22:36 2018

@author: lifanhong
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a,b = b,a
        out = [0 for i in range(len(a)+1)]
        i = 1
        while i <= len(a) + 1:
            if i <= len(b):    
                out[-i] += int(a[-i]) + int(b[-i])
            elif i <= len(a):
                out[-i] += int(a[-i])           
            if out[-i] == 2:
                    out[-i],out[-i-1] = 0,1
            elif out[-i] == 2:
                    out[-i],out[-i-1] = 1,1
            i += 1
        return ''.join(str(x) for x in out[1:]) if out[0] == 0 else ''.join(str(x) for x in out)