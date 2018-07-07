#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 12:39:45 2018

@author: lifanhong

20180707 AC:
1.GHX
2.LFH
3.
4.

"""

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n % 4 == 0 else True