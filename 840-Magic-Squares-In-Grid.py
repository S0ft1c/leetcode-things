from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(0, len(grid) - 2, 1):
            for j in range(0, len(grid[i]) - 2, 1):
                ss = {grid[i][j], grid[i + 1][j], grid[i + 2][j], grid[i][j + 1], grid[i + 1][j + 1],
                      grid[i + 2][j + 1], grid[i][j + 2], grid[i + 1][j + 2], grid[i + 2][j + 2]}
                if ss & {0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20} or len(ss) != 9:
                    continue
                first_diag = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                second_diag = grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]
                row1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                row2 = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]
                row3 = grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                col1 = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
                col2 = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
                col3 = grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]

                if len({first_diag, second_diag, row1, row2, row3, col1, col2, col3}) == 1:
                    ans += 1
        return ans


if __name__ == '__main__':
    print(
        Solution().numMagicSquaresInside(
            grid=[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
        )
    )

    print(
        Solution().numMagicSquaresInside(
            grid=[[8]]
        )
    )

    print(
        Solution().numMagicSquaresInside(
            grid=[[4, 7, 8], [9, 5, 1], [2, 3, 6]],
        )
    )

    print(
        Solution().numMagicSquaresInside(
            grid=[[5, 5, 5], [5, 5, 5], [5, 5, 5]],
        )
    )
