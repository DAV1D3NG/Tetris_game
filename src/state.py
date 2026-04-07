from src.utils import get_shape, load_high_score

def reset_state():
    """
    Initialize and return the default game state.
    :param: none.
    :type: none.
    :returns: dictionary containing initial state values.
    :rtype: dict.
    """
    return {
        # Keeps the main game loop running
        "running": True,
        # Ensures the game starts unpaused
        "paused": False,
        # Sets game over status to false
        "game_over": False,
        # Resets the restart request flag
        "restart": False,
        # Resets the timer for falling blocks
        "fall_time": 0,
        # Resets the flag that triggers a new piece
        "change_piece": False,
        # Clears all blocks locked on the grid
        "locked": {},
        # Generates the first active piece
        "current_piece": get_shape(),
        # Generates the preview of the next piece
        "next_piece": get_shape(),
        # Resets current score to zero
        "score": 0,
        # Loads the best score from the local file
        "high_score": load_high_score(),
    }