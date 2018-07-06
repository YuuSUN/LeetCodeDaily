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
        if s == "0000":
            return ['0.0.0.0']
        comb = self.combination(len(s))
        print(comb)
        for item in comb:
            a,b,c,d = item[0],item[1],item[2],item[3]
            A,B,C,D = s[0:a],s[a:a+b],s[a+b:a+b+c],s[a+b+c:]
            if 0 <= int(A) <= 255 and \
               0 <= int(B) <= 255 and\
               0 <= int(C) <= 255 and\
               0 <= int(D) <= 255:
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
print(Solution().restoreIpAddresses("1111"))
