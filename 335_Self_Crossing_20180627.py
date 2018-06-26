#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 00:36:38 2018

@author: lifanhong
"""

class Solution:
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        
        P[0] = [0,0]
        P[1] = [0,x[0]]
        P[2] = [-x[1],x[0]]
        P[3] = [-x[1],x[0]-x[2]]
        P[4] = [-x[1]+x[3],x[0]-x[2]]
        P[5] = [-x[1]+x[3],x[0]-x[2]+x[4]]
        if n % 2 == 0:
            P[n] = [P[n-1][0] + x[n-1],P[n-1][1]]
        else:
            P[n] = [P[n-1][0],P[n-1][1] + x[n-1]]
        
        vertical:
            P[O-1],P[2-3],...P[2n],P[2n+1] with same x and different y
            which is 
            x = P[0][0] = P[1][0]
            y = P[0][1] and P[1][1]
        level:
            P[1-2],P[3-4],...P[2n+1],P[2n+2] with different x and same y
            x = P[1][0], P[2][0]
            y = P[1][1] = P[2][1]
            
        or just use vertical and level to represent dots
        
        vertical = [0, x[0], x[0]-x[2], x[0]-x[2]+x[4]...]
        level = [0, -x[1], -x[1]+x[3], -x[1]+x[3]-x[5]...]
        
        P[0] = [l[0],v[0]]
        P[1] = [l[0],v[1]] append v[1]
        P[2] = [l[1],v[1]] append l[1]
        P[3] = [l[1],v[2]]
        P[4] = [l[2],v[2]]
        P[5] = [l[2],v[3]]
        
        if n % 2 == 0:
            point[n] and point[n-1] is level
            then check if point[n][1] is between any vertical points
            if so check the vertical point's level to see if it's between
        else is vertical:
        """
#        v = [0]
#        l = [0]
#        P = dict()
#        if len(x) < 4:
#            return False
#        for n, step in enumerate(x):
#            if n % 2 == 0:
#                if n > 0:
#                    l.append(l[-1]+(-1)**(n//2)*x[n-1])
#                P[n] = [l[n//2],v[n//2]]
#                i = 1
#                while i < n/2:
#                    if (v[n/2]-v[i])*(v[n/2]-v[i-1]) <= 0:
#                        if (l[i-1]-l[n/2])*(v[i-1]-l[n/2-1]) <= 0:
#                            print(P)
#                            return True
#                    i += 1
#            elif n % 2 == 1:
#                v.append(v[-1]+(-1)**(n//2)*x[n-1])
#                P[n] = [l[n//2],v[n//2+1]]
#                i = 1
#                while i <= n/2:
#                    if (l[n//2]-l[i])*(l[n//2]-l[i-1]) <= 0:
#                        if (v[i]-v[n//2+1])*(v[i]-v[n//2]) <= 0:
#                            print(P)
#                            print(i)
#                            return True
#                    i += 1
#        return False
        path = {"0,0":1}
        a,b = 0,0
        for n, step in enumerate(x):
            for s in range(step):
                if n % 4 == 0:
                    b += 1
                elif n % 4 == 1:
                    a -= 1
                elif n % 4 == 2:
                    b -= 1
                else:
                    a += 1
                if str(a)+","+str(b) not in path:
                    path[str(a)+","+str(b)] = 1
                else:
                    return True
        return False

print(Solution().isSelfCrossing([1,2,3,4]))