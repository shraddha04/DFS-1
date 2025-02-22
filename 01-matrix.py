# Time Complexity : O(m*n)
# Space Complexity : O(m*n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

"""

Put all 0's in a queue and then do BFS, for all the 1's in the level, set the distance == level

"""
from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        if not mat:
            return mat

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        m = len(mat)
        n = len(mat[0])
        queue = deque()

        for i in range(0, m):
            for j in range(0, n):
                if mat[i][j] == 0:
                    queue.append([i, j])
                else:
                    mat[i][j] = -1

        distance = 1
        while queue:
            size = len(queue)
            for i in range(0, size):
                curr = queue.popleft()
                r = curr[0]
                c = curr[1]
                for dir in dirs:
                    nr = dir[0] + r
                    nc = dir[1] + c
                    if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                        queue.append([nr, nc])
                        mat[nr][nc] = distance
            distance += 1
        return mat