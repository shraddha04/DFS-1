# Time Complexity : O(m*n)
# Space Complexity : O(m*n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

"""
Do BFS starting from sr,sc
"""
from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        if not image:
            return image

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(image)
        n = len(image[0])
        if image[sr][sc] == color:
            return image
        queue = deque()
        queue.append([sr, sc])
        orgColor = image[sr][sc]
        image[sr][sc] = color

        while queue:
            curr = queue.popleft()
            sr = curr[0]
            sc = curr[1]
            for dir in dirs:
                nr = dir[0] + sr
                nc = dir[1] + sc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == orgColor:
                    queue.append([nr, nc])
                    image[nr][nc] = color

        return image