class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        left, right = 0, m*n - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid//m][mid % m]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1

        return False



        