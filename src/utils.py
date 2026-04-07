import random
from src.piece import Piece
from src.config import COLUMNS, SHAPES, high_score_file
from src.grid import create_grid, valid_space

def get_shape():
    """
    Generate a random piece at the starting position.
    :param: none.
    :type: none.
    :returns: newly created piece.
    :rtype: Piece.
    """
    # Selects a random index from the available shape types (0 to 6 for the 7 Tetrominos)
    shape_type = random.randrange(len(SHAPES))

    # Creates and returns the piece at the starting position (Top-Center)
    # x: Calculated to center the piece based on the grid's columns
    # y: Set to -2 so the piece starts slightly above the visible grid
    return Piece(COLUMNS // 2 - 2, -2, shape_type)

def get_ghost_position(current_piece, locked_blocks_coordinates):
    """
    Calculate the landing position of the current piece.
    :param current_piece: active piece.
    :type current_piece: Piece.
    :param locked_blocks_coordinates: dictionary of locked blocks.
    :type locked_blocks_coordinates: dict.
    :returns: piece representing the landing position.
    :rtype: Piece.
    """
    # Creates a 'clone' of the current piece with the same position and type
    ghost_piece = Piece(current_piece.x, current_piece.y, current_piece.shape_type)

    # Ensures the ghost_piece has the same rotation as the active piece
    ghost_piece.rotation = current_piece.rotation

    # Generates a temporary grid to check for collisions
    grid = create_grid(locked_blocks_coordinates)

    # Loops to simulate the piece falling rapidly
    while True:
        # Moves the ghost_piece down by one row
        ghost_piece.y += 1

        # Checks if the new position is invalid (hits a wall, floor, or another piece)
        if not valid_space(ghost_piece, grid):
            # Moves back up to the last valid position and stops the loop (found the landing spot)
            ghost_piece.y -= 1
            break

    return ghost_piece

def load_high_score():
    """
    Load the saved high score from file.
    :param: none.
    :type: none.
    :returns: stored high score value.
    :rtype: int.
    """
    try:
        # Opens the high score file in read mode
        with open(high_score_file, "r") as file:
            return int(file.read())
    except:
        # If the file is missing or corrupted, returns a default score of 0
        return 0

def save_high_score(score):
    """
    Save the high score to file.
    :param score: score to save.
    :type score: int.
    :returns: None.
    :rtype: None.
    """
    # Opens (or create) the high score file in writing mode
    with open(high_score_file, "w") as file:
        file.write(str(score))