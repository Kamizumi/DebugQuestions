class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:

        #Gets values for rows and columns
        rows, cols = len(boxGrid), len(boxGrid[0])

        for r in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if boxGrid[r][col] == "#":
                    temp_col = col + 1
                    while temp_col < cols and boxGrid[r][temp_col] == '.': #While the temporary column is < real length and the current cell is a .
                        temp_col += 1
                    
                    boxGrid[r][col] = '.'
                    boxGrid[r][temp_col] = '#'
        

        result = []
        for c in range(cols):
            col = []
            for r in range(rows - 1, -1 ,-1):
                col.append(boxGrid[r][c])
            result.append(col)
        return result



def main():
    grid = [
    ["#",".","*","."],
    ["#","#","*","."]]

    for i in range(len(grid)):
        print(grid[i])
    print("\n")

    sol = Solution()
    result = sol.rotateTheBox(boxGrid = grid)

    for i in range(len(result)):
        print(f"{result[i]}")

main()
