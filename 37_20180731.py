#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:12:33 2018

@author: lifanhong
"""

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row, col, box, tofill = dict(), dict(), dict(), list()
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    box[(r//3,c//3)].add(board[r][c])
                else:
                    tofill.append((r,c))
        
        def fill():
            if not tofill:
                return True
            r, c = tofill[0]
            b = (r//3,c//3)
            for test in ['1','2','3','4','5','6','7','8','9']:
                if test not in row[r] and test not in col[c] and test not in box[b]:
                    board[r][c] = test
                    row[r].add(test)
                    col[c].add(test)
                    box[b].add(test)
                    tofill.popleft()
                    if fill():
                        return True
                    else:
                        board[r][c] = '.'
                        row[r].discard(test)
                        col[c].discard(test)
                        box[b].discard(test)
                        tofill.appendleft()
            return False
        
        fill()

    
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().solveSudoku(board))


























