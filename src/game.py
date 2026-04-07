"""
Tetris.py
Simple Tetris game with ghost pieces, next piece preview, increasing speed with score, pause, restart and exit.
Requirements: pip install pygame
"""

import pygame
from src.config import *
from src.audio import *
from src.grid import *
from src.render import *
from src.input_handler import *
from src.utils import *
from src.state import *

def main():
    """
    Run the main game loop and manage game execution.
    :param: none.
    :type: none.
    :returns: None.
    :rtype: None.
    """
    # Starts Pygame modules
    pygame.init()

    # Sets delay and speed for continuous key presses
    pygame.key.set_repeat(300, 100)

    # Initializes sounds, music, and game state (score, pieces, etc.)
    audio = init_audio()
    state = reset_state()

    # Creates the game window
    display = pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT))

    # Sets the window title and icon
    pygame.display.set_caption("Tetris Game")
    pygame.display.set_icon(pygame.image.load("assets/images/icon.jpg"))

    # Instantiates a clock to track time and control FPS
    clock = pygame.time.Clock()

    # Sets the starting fall speed and the fastest possible (in seconds)
    initial_fall_speed = 1
    max_fall_speed = 0.1

    # Loops until the user closes the window game
    while state["running"]:
        # Calculates time passed since the last frame
        dt = clock.tick(FPS) / 1000.0

        # Resets everything if the user wants to restart
        if state["restart"]:
            # Preserves the music's state before restarting
            old_audio = audio
            state = reset_state()
            # Restores audio
            audio = old_audio
            if audio["music_enabled"]:
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(audio["music_volume"])
            else:
                pygame.mixer.music.stop()

            continue

        # Makes the game harder and adjusts music speed as the score increases
        current_fall_speed = max(max_fall_speed, initial_fall_speed - (state["score"] / 4000.0))
        update_music(current_fall_speed, audio)

        # Checks if the game is not paused or ended
        if not state["paused"] and not state["game_over"]:
            # Accumulates time for the piece to fall
            state["fall_time"] += dt

        # Checks for user inputs (keyboard/mouse)
        for event in pygame.event.get():
            # If the user quits the game, the game loop stops
            if event.type == pygame.QUIT:
                state["running"] = False

            # If the user presses any key, the appropriate function processes it
            elif event.type == pygame.KEYDOWN:
                handle_keyboard(event, state, audio)

            # If the user interacts with the mouse in some specific cases, the appropriate function processes them
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                handle_mouse(event, audio)

        if not state["paused"] and not state["game_over"] and state["fall_time"] >= current_fall_speed:
            # Resets the fall time timer and moves the piece down one row automatically
            state["fall_time"] = 0
            state["current_piece"].y += 1

            # If the piece hits something, moves back and prepares to lock
            if not valid_space(state["current_piece"], create_grid(state["locked"])):
                state["current_piece"].y -= 1
                state["change_piece"] = True

        # Checks if the current piece is going to be locked
        if state["change_piece"]:
            # Adds the current piece positions to the 'locked' dictionary
            for (r, c) in convert_shape_to_positions(state["current_piece"]):
                if r >= 0:
                    state["locked"][(r, c)] = state["current_piece"].color

            # Updates the grid with the new locked piece and removes full lines (if any)
            grid = create_grid(state["locked"])
            rows_cleared, state["locked"] = clear_rows(grid, state["locked"])

            # If some rows are cleared, the clear sound plays
            if rows_cleared > 0 and audio["sfx_enabled"]:
                audio["clear"].play()

            # Updates score
            state["score"] += (100 * rows_cleared) * rows_cleared

            # Switches and generates the next piece, also resets the corresponding flag
            state["current_piece"] = state["next_piece"]
            state["next_piece"] = get_shape()
            state["change_piece"] = False

            # If the blocks reached the top, it's Game Over
            if check_lost(state["locked"]):
                state["game_over"] = True
                pygame.mixer.music.stop()
                if audio["sfx_enabled"]:
                    audio["game_over"].play()

        # Refreshes the grid state
        grid = create_grid(state["locked"])

        # Calculates where the piece would land (Ghost)
        ghost_piece = get_ghost_position(state["current_piece"], state["locked"])

        # Adds the active moving piece to the grid for drawing
        for (r, c) in convert_shape_to_positions(state["current_piece"]):
            if r >= 0:
                grid[r][c] = state["current_piece"].color

        # Renders everything on the screen
        draw_window(display, grid, state["score"], state["high_score"], state["next_piece"], state["paused"],
                    audio["music_enabled"], audio["sfx_enabled"],
                    audio["music_volume"], audio["sfx_volume"])

        # Draws the transparent ghost piece
        draw_ghost(display, ghost_piece)

        # If the current score is higher than the record, it is updated and saved to the file
        if state["score"] > state["high_score"]:
            state["high_score"] = state["score"]
            save_high_score(state["high_score"])

        # If it's Game Over, it is displayed on screen
        if state["game_over"]:
            draw_game_over(display, state["score"], state["high_score"])

        # Updates the physical monitor display
        pygame.display.update()

    # Closes the game window and cleans up
    pygame.quit()