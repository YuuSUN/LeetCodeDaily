#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 23:12:32 2018

@author: lifanhong
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l12 = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                l12.next = l1
                l1 = l1.next
            else:
                l12.next = l2
                l2 = l2.next
            l12 = l12.next
        l12.next = l1 if l1 else l2
        return head.next
