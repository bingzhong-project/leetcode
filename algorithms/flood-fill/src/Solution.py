class Solution:
    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        def move(i, j):
            return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        def fill(image, i, j, old_color, new_color):
            if image[i][j] != old_color:
                return
            image[i][j] = new_color
            for m, n in move(i, j):
                if m < 0 or m > len(image) - 1 or n < 0 or n > len(
                        image[m]) - 1:
                    continue
                if image[m][n] == old_color:
                    fill(image, m, n, old_color, new_color)

        if newColor == image[sr][sc]:
            return image

        fill(image, sr, sc, image[sr][sc], newColor)

        return image
