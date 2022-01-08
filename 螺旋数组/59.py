def generateMatrix(self, n: int) -> List[List[int]]:
        flag = 0
        if n % 2 == 1:
            flag = 1
        num = n ** 2
        arr = [[0]*n for _ in range(n)]
        number = 1
        left, right, up, down = 0, n - 1, 0, n - 1 
        while left < right and up < down:
            for x in range(left, right):
                arr[up][x] = number
                number += 1
            
            for x in range(up, down):
                arr[x][right] = number
                number += 1

            for x in range(right, left, -1):
                arr[down][x] = number
                number += 1
            
            for x in range(down, up, -1):
                arr[x][left] = number
                number += 1 

            left += 1
            right -= 1
            up += 1
            down -= 1
        if flag:
            arr[n//2][n//2] = number
        return arr
