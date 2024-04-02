def diagonalSum(self, mat: List[List[int]]) -> int:
        downsum = 0
        for index in range(len(mat)):
            downsum += mat[index][index]
        upsum = 0
        for i in range(len(mat)):
            if i != len(mat) - i - 1:
                upsum += mat[i][len(mat)-i-1]
        return downsum + upsum
    