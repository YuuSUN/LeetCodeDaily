#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 00:46:39 2018

@author: lifanhong

rectangle 1 (A,D) (C,D)
            (A,B) (C,B)
rectangle 2 (E,H) (G,H)
            (E,F) (G,F)

"""
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x = min(C,G) - max(A,E)
        y = min(D,H) - max(B,F)
        overlap = max(x,0)*max(y,0)
        output = (C-A)*(D-B) + (G-E)*(H-F) - overlap
        return output
        

        