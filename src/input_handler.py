import pygame
from src.config import *
from src.grid import valid_space, create_grid

def handle_keyboard(event, state, audio):
    """
    Handle keyboard input for gameplay actions.
    :param event: pygame keyboard event.
    :type event: pygame.event.Event.
    :param state: current game state.
    :type state: dict.
    :param audio: audio configuration dictionary.
    :type audio: dict.
    :returns: None.
    :rtype: None.
    """
    # Memorizes the current controlled piece in an object
    piece = state["current_piece"]

    # If 'ESC' is pressed, the game and the window close
    if event.key == pygame.K_ESCAPE:
        state["running"] = False

    # If 'P' is pressed, the game pause and the music toggle
    elif event.key == pygame.K_p:
        state["paused"] = not state["paused"]
        if state["paused"]:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    # If 'R' is pressed, the game restarts
    elif event.key == pygame.K_r:
        state["restart"] = True

    # Checks if the game isn't paused or ended
    elif not state["paused"] and not state["game_over"]:
        # If Left Arrow or 'A' are pressed, the piece moves to the left
        if event.key in (pygame.K_LEFT, pygame.K_a):
            piece.x -= 1
            if not valid_space(piece, create_grid(state["locked"])):
                piece.x += 1

        # If Right Arrow or 'D' are pressed, the piece moves to the right
        elif event.key in (pygame.K_RIGHT, pygame.K_d):
            piece.x += 1
            if not valid_space(piece, create_grid(state["locked"])):
                piece.x -= 1

        # If Down Arrow or 'S' are pressed, the piece moves down by one (Soft Drop)
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            piece.y += 1
            if not valid_space(piece, create_grid(state["locked"])):
                piece.y -= 1
            elif audio["sfx_enabled"]:
                audio["drop"].play()

        # If Up Arrow or 'K' are pressed, the piece rotates clockwise
        elif event.key in (pygame.K_UP, pygame.K_w):
            piece.rotate()
            if not valid_space(piece, create_grid(state["locked"])):
                piece.rotate_back()
            elif audio["sfx_enabled"]:
                audio["rotate"].play()

        # If Space is pressed, the piece instantly drops (Hard Drop)
        elif event.key == pygame.K_SPACE:
            while True:
                piece.y += 1
                if not valid_space(piece, create_grid(state["locked"])):
                    piece.y -= 1
                    break
            if audio["sfx_enabled"]:
                audio["hard_drop"].play()
            state["change_piece"] = True

        # If 'M' is pressed, the music state changes
        elif event.key == pygame.K_m:
            audio["music_enabled"] = not audio["music_enabled"]
            if audio["music_enabled"]:
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(audio["music_volume"])
            else:
                pygame.mixer.music.stop()

        # If 'K' is pressed, the SFX state changes
        elif event.key == pygame.K_k:
            audio["sfx_enabled"] = not audio["sfx_enabled"]

def handle_mouse(event, audio):
    """
    Handle mouse input for UI interactions.
    :param event: pygame mouse event.
    :type event: pygame.event.Event.
    :param audio: audio configuration dictionary.
    :type audio: dict.
    :returns: None.
    :rtype: None.
    """
    # Gets the current mouse position (X and Y coordinates)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculates the start of the side panel
    panel_x = CELL_SIZE * COLUMNS

    # Checks if the user is clicking something with the mouse
    if event.type == pygame.MOUSEBUTTONDOWN:
        # If the user clicks the Music checkbox, the music toggles on or off
        if panel_x + 20 <= mouse_x <= panel_x + 38 and MUSIC_CHECKBOX_Y <= mouse_y <= MUSIC_CHECKBOX_Y + 18:
            audio["music_enabled"] = not audio["music_enabled"]
            if audio["music_enabled"]:
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(audio["music_volume"])
            else:
                pygame.mixer.music.stop()

        # If the user clicks the SFX checkbox, the sound effects toggle on or off
        if panel_x + 20 <= mouse_x <= panel_x + 38 and SFX_CHECKBOX_Y <= mouse_y <= SFX_CHECKBOX_Y + 18:
            audio["sfx_enabled"] = not audio["sfx_enabled"]

        # If the user clicks near the Music slider, starts dragging the music volume knob
        if panel_x + 20 <= mouse_x <= panel_x + 140 and MUSIC_SLIDER_Y - 10 <= mouse_y <= MUSIC_SLIDER_Y + 10:
            audio["dragging_music"] = True

        # If the user clicks near the SFX slider, starts dragging the SFX volume knob
        if panel_x + 20 <= mouse_x <= panel_x + 140 and SFX_SLIDER_Y - 10 <= mouse_y <= SFX_SLIDER_Y + 10:
            audio["dragging_sfx"] = True

    # If the user released a mouse button, stops dragging any slider
    elif event.type == pygame.MOUSEBUTTONUP:
        audio["dragging_music"] = False
        audio["dragging_sfx"] = False

    # Checks if the user is moving the mouse while keeping clicked something
    elif event.type == pygame.MOUSEMOTION:
        # Updates music volume while dragging the slider
        if audio["dragging_music"]:
            # Calculates volume (0 to 1) based on mouse X position
            audio["music_volume"] = max(0, min(1, (mouse_x - (panel_x + 20)) / 120))
            # Applies the new volume level to the music mixer
            pygame.mixer.music.set_volume(audio["music_volume"])

        # Updates SFX volume while dragging the slider
        if audio["dragging_sfx"]:
            # Calculates volume (0 to 1) based on mouse X position
            audio["sfx_volume"] = max(0, min(1, (mouse_x - (panel_x + 20)) / 120))
            # Applies the new volume to all sound effect objects
            for s in audio["sounds"]:
                s.set_volume(audio["sfx_volume"])