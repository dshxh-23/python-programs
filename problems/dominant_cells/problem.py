"""
PROBLEM STATEMEMNT:

Given: A 2D list grid of integers (rows may have varying lengths).

Task: Write a function numCells(grid) that returns the number of dominant cells in the grid.

Definition: A cell at position (i, j) with value grid[i][j] is considered dominant if it is strictly greater than the value of every valid neighbor. Neighbors include all adjacent cells horizontally, vertically, and diagonally (so, there exists a maximum of 8 neighbours per cell). For edge or corner cells, only the neighbors that fall inside the grid are considered valid.
"""



def main():
    matrix = [[1,2,3], [4,9,5], [6,7,8], [9]]
    print(matrix)
    print()
    print(f"No. of dominant cells: {numCells(matrix)}")



def numCells(grid):

    # Initial count of dominant cells
    res = 0

    # To loop through each element of the grid
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            active_cell = grid[i][j]

            # Checking the cell is dominant or not by method of contradiction
            is_dominant = True

            # To iterate over each neighbour cell of the active cell
            for row_offset in (-1, 0, 1):
                neigh_row = i+row_offset
                for col_offset in (-1, 0, 1):
                    neigh_col = j+col_offset

                    # pass if the active cell and neighbour cell are the same
                    if row_offset == col_offset == 0:
                        continue

                    # Check if the neighbour cell exists or not
                    if (0 <= neigh_row < len(grid)) and (0 <= neigh_col < len(grid[neigh_row])):
                        neigh_cell = grid[neigh_row][neigh_col]
                        if not active_cell > neigh_cell:
                            is_dominant = False

                # Break outerloop early for faster execution
                if not is_dominant:
                        break   
                
            # If cell is still dominant after checking for each neighbour, the cell is indeed dominant
            if is_dominant:
                res += 1

    return res

if __name__ == "__main__":
    main()