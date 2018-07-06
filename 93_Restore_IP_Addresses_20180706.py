#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 21:14:35 2018

@author: lifanhong

A valid IP address must be in the 
form of xxx.xxx.xxx.xxx, 
where xxx is a number from 0-255.
"""
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        IP = []
        if len(s) > 12 or len(s) < 4:
            return []
        comb = self.combination(len(s))
        for item in comb:
            a,b,c,d = item[0],item[1],item[2],item[3]
            A,B,C,D = s[0:a],s[a:a+b],s[a+b:a+b+c],s[a+b+c:]
            isIP = True
            for digit in [A,B,C,D]:
                if int(digit) < 0 or int(digit) > 255\
                or digit[0] == '0' and len(digit) > 1:
                    isIP = False
            if isIP:
                IP.append('.'.join([A,B,C,D]))
        return IP
      
    def combination(self, n):
        a,b,c,d = 1,1,1,1
        comb = []
        while a <= 3:
            while b <= 3:
                while c<= 3:
                    while d <= 3:
                        if a+b+c+d == n:
                            comb.append([a,b,c,d])
                        d += 1
                    c += 1
                    d = 1
                b += 1
                c = 1
            a += 1
            b = 1
        return comb

#print(Solution().combination(11))
print(Solution().restoreIpAddresses("010010"))
