"""
Week 2, Day 3: Flood Fill

An image is represented by a 2-D array of integers, each integer representing the pixel
value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood
fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel, plus any 
pixels connected 4-directionally to those pixels (also with the same color as the starting 
pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

E x a m p l e

Input:

    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2

Output: 

    [[2,2,2],[2,2,0],[2,0,1]]

Explanation:

    From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
    by a path of the same color as the starting pixel are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected
    to the starting pixel.

N o t e s

    - The length of image and image[0] will be in the range [1, 50].
    - The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
    - The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

H i n t

    - Write a recursive function that paints the pixel if it's the correct color, then
      recurses on neighboring pixels.

"""
from typing import List


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        self.image = image
        self._floodFill(sr, sc, newColor, oldColor)
        return image

    def _floodFill(self, sr: int, sc: int, newColor: int, oldColor: int) -> None:
        self.image[sr][sc] = -1
        up, right, down, left = sr - 1, sc + 1, sr + 1, sc - 1
        if up >= 0 and self.image[up][sc] == oldColor:
            self._floodFill(up, sc, newColor, oldColor)
        if right < len(self.image[0]) and self.image[sr][right] == oldColor:
            self._floodFill(sr, right, newColor, oldColor)
        if down < len(self.image) and self.image[down][sc] == oldColor:
            self._floodFill(down, sc, newColor, oldColor)
        if left >= 0 and self.image[sr][left] == oldColor:
            self._floodFill(sr, left, newColor, oldColor)
        self.image[sr][sc] = newColor 


if __name__ == '__main__':
    print(
        Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2),
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        sep='\n'
    )
    print('---')
    print(
        Solution().floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1),
        [[0, 0, 0], [0, 1, 1]],
        sep='\n'
    )
    print('---')

# last line of code
