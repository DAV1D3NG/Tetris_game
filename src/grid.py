from src.config import *
from src.piece import Piece

def create_grid(locked_blocks_coordinates = None):
    """
    Create the grid based on locked block positions.
    :param locked_blocks_coordinates: dictionary containing coordinates and colors of locked blocks.
    :type locked_blocks_coordinates: dict.
    :returns: 2D matrix representing the game grid with colors.
    :rtype: list[list[tuple[int, int, int]]].
    """
    # If no arguments are passed (e.g., at the start of the game), initializes an empty dictionary
    locked_blocks_coordinates = locked_blocks_coordinates or {}

    # Creates the grid by checking each coordinate (r, c) in 'locked_blocks_coordinates'.
    # If found, it uses the piece's color; otherwise, it defaults to BLACK.
    return [[locked_blocks_coordinates.get((r, c), BLACK) for c in range(COLUMNS)] for r in range(ROWS)]

def convert_shape_to_positions(piece):
    """
    Convert the current piece shape into grid coordinates.
    :param piece: current falling piece.
    :type piece: Piece.
    :returns: iterable of coordinates occupied by the piece.
    :rtype: generator[tuple[int, int]].
    """
    # Returns the list of all coordinates occupied by the piece by mapping the piece's shape matrix onto the grid
    return ((piece.y + i, piece.x + j) for i, row in enumerate(piece.shape) for j, cell in enumerate(row) if cell == 'X')

def valid_space(piece, grid):
    """
    Check whether a piece is in a valid position inside the grid.
    :param piece: current piece to validate.
    :type piece: Piece.
    :param grid: current grid matrix.
    :type grid: list[list[tuple[int, int, int]]].
    :returns: True if the position is valid, otherwise False.
    :rtype: bool.
    """
    # Creates a set of all coordinates that are currently empty (BLACK)
    accepted_coordinates = {(r, c) for r in range(ROWS) for c in range(COLUMNS) if grid[r][c] == BLACK}

    # Gets the actual grid coordinates for the current piece shape
    actual_piece_coordinates = convert_shape_to_positions(piece)

    # Checks if all blocks of the piece are within boundaries and in empty spaces
    return all(0 <= c < COLUMNS and r < ROWS and (r < 0 or (r, c) in accepted_coordinates) for r, c in actual_piece_coordinates)

def check_lost(locked_blocks_coordinates):
    """
    Determine if the game is lost based on locked block positions.
    :param locked_blocks_coordinates: dictionary of locked blocks.
    :type locked_blocks_coordinates: dict.
    :returns: True if a block reached the top, otherwise False.
    :rtype: bool.
    """
    # Iterates through all the coordinates of the blocks already placed on the board
    for (r, c) in locked_blocks_coordinates:
        # If the row index 'r' is above or at the very first row of the grid, it means there is no more space to play (Game Over)
        if r < 1:
            return True

    # If no blocks are at the top, the game continues
    return False

def clear_rows(grid, locked_blocks_coordinates):
    """
    Remove full rows and update remaining block positions.
    :param grid: current grid matrix.
    :type grid: list[list[tuple[int, int, int]]].
    :param locked_blocks_coordinates: dictionary of locked blocks.
    :type locked_blocks_coordinates: dict.
    :returns: number of cleared rows and updated locked blocks.
    :rtype: tuple[int, dict].
    """
    # Initializes the counter for the rows full of locked blocks
    rows_cleared = 0

    # Scans rows from bottom to top (line by line) to find and delete full rows
    for r in range(ROWS - 1, -1, -1):
        # If the row is completely full (no BLACK cells), every block of it is removed from the locked dictionary
        if BLACK not in grid[r]:
            rows_cleared += 1
            for c in range(COLUMNS):
                if (r, c) in locked_blocks_coordinates:
                    del locked_blocks_coordinates[(r, c)]

    # If rows were cleared, updates the positions of the remaining blocks
    if rows_cleared > 0:
        # Initializes a new empty dictionary used for the new locked blocks coordinates
        new_locked_blocks_coordinates = {}

        # Initializes a counter that tracks how many positions down a block must fall
        shift_down = 0

        # Scans again from bottom to top to calculate the downward shift
        for r in range(ROWS - 1, -1, -1):
            # Checks if this row was one of the cleared ones
            if BLACK not in grid[r]:
                shift_down += 1
            else:
                # Moves blocks down by the number of cleared rows below them
                for c in range(COLUMNS):
                    if (r, c) in locked_blocks_coordinates:
                        # Adds the block to the new dictionary with updated row (r + shift_down)
                        new_locked_blocks_coordinates[(r + shift_down, c)] = locked_blocks_coordinates[(r, c)]

        return rows_cleared, new_locked_blocks_coordinates

    # If no rows were full, returns the original state
    return 0, locked_blocks_coordinates