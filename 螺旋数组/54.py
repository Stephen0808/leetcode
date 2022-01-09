def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col = len(matrix[0])
        row = len(matrix)
        l = col * row
        left, right, up, down = 0, col - 1, 0, row - 1
        num = []
        print(left, right, up, down)
        while left <= right and up <= down:
            for x in matrix[up][left:right]:
                num.append(x)
            if l == len(num):
                break
            for x in list(matrix[y][right] for y in range(up, down+1)):
                num.append(x)
            if l == len(num):
                break
            for x in matrix[down][right-1:left:-1]:
                num.append(x)
            if l == len(num):
                break
            for x in list(matrix[y][left] for y in range(down, up, -1)):
                num.append(x)
            if l == len(num):
                break
            left += 1
            right -= 1
            up += 1
            down -= 1
        return num
            
