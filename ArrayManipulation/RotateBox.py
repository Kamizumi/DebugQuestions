class Solution:

    def BruteForceRotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        '''
        Function to brute force solve rotating the box
        '''
        #Gets values for rows and columns
        rows, cols = len(boxGrid), len(boxGrid[0])

        for r in reversed(range(rows)):
            for col in reversed(range(cols)):
                if boxGrid[r][col] == "#":
                    temp_col = col + 1
                    while temp_col < cols and boxGrid[r][temp_col] == '.': #While the temporary column is < real length and the current cell is a .
                        temp_col += 1
                    
                    boxGrid[r][col] = '.'
                    boxGrid[r][temp_col] = '#'
        

        result = []
        for c in range(cols):
            col = []
            for r in reversed(range(rows)):
                col.append(boxGrid[r][c])
            result.append(col)
        return result
    #---------------------------------------------------------------------------------------------------
    def TwoPointerRotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])

        for r in range(rows):
            i = cols - 1
            for c in reversed(range(cols)):
                if boxGrid[r][c] == '#':
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    i -= 1
                elif boxGrid[r][c] == '*':
                    i = c - 1
        
        result = []
        for c in range(cols):
            col = []
            for r in reversed(range(rows)):
                col.append(boxGrid[r][c])
            result.append(col)

        return result



def main():
    grid = [
    ["#",".","*","."],
    ["#","#","*","."]]

   

    sol = Solution()
    result = sol.TwoPointerRotateTheBox(boxGrid = grid)

    for i in range(len(grid)):
        print(grid[i])
    print("")
    for i in range(len(result)):
        print(f"{result[i]}")



    #-------------------------------------
    '''result = sol.BruteForceRotateTheBox(boxGrid = grid)

    for i in range(len(grid)):
        print(grid[i])
    print("\n")

    for i in range(len(result)):
        print(f"{result[i]}")
    '''
     #-------------------------------------


if __name__ == "__main__":
    main()