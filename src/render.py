import pygame
from src.config import *
from src.grid import convert_shape_to_positions

def draw_grid(surface):
    """
    Draw the grid lines on the surface.
    :param surface: pygame surface where the grid is drawn.
    :type surface: pygame.Surface.
    :returns: None.
    :rtype: None.
    """
    # Draws horizontal lines for each row
    for i in range(ROWS):
        pygame.draw.line(surface, GRAY, (0, i * CELL_SIZE), (CELL_SIZE * COLUMNS, i * CELL_SIZE))

    # Draws vertical lines for each column
    for j in range(COLUMNS):
        pygame.draw.line(surface, GRAY, (j * CELL_SIZE, 0), (j * CELL_SIZE, CELL_SIZE * ROWS))

def draw_next_piece(surface, piece, x_offset, y_offset):
    """
    Render the preview of the next piece in the side panel.
    :param surface: pygame surface where the preview is drawn.
    :type surface: pygame.Surface.
    :param piece: next piece to display.
    :type piece: Piece.
    :param x_offset: horizontal offset for drawing.
    :type x_offset: int.
    :param y_offset: vertical offset for drawing.
    :type y_offset: int.
    :returns: None.
    :rtype: None.
    """
    # Initializes the shape for the piece, that will be displayed, and its pixel size
    shape = piece.shape
    piece_cell_size = CELL_SIZE

    # Calculates the maximum width of the shape to center it properly
    shape_width = max(len(row) for row in shape)

    # Calculates starting coordinates to center the piece within the preview panel
    start_x = x_offset + (PANEL_WIDTH - shape_width * piece_cell_size) // 2 - 10
    start_y = y_offset

    # Loops through the shape matrix and draws only the 'X' blocks
    for i, row in enumerate(shape):
        for j, ch in enumerate(row):
            if ch == 'X':
                # Defines the rectangle area for the block
                rectangle_area = pygame.Rect(start_x + j * piece_cell_size, start_y + i * piece_cell_size, piece_cell_size, piece_cell_size)

                # Fills the block with the piece's color
                pygame.draw.rect(surface, piece.color, rectangle_area)

                # Draws a white border (width 1) around the block for better visibility
                pygame.draw.rect(surface, WHITE, rectangle_area, 1)

def draw_ghost(surface, ghost_piece):
    """
    Draw the ghost piece at its landing position.
    :param surface: pygame surface where the ghost is drawn.
    :type surface: pygame.Surface.
    :param ghost_piece: piece representing the landing position.
    :type ghost_piece: Piece.
    :returns: None.
    :rtype: None.
    """
    # Converts the ghost piece's internal shape into grid (row, column) coordinates
    for (r, c) in convert_shape_to_positions(ghost_piece):
        # Only draws if the block is within the visible part of the grid (row 0 or below)
        if r >= 0:
            # Creates a small square surface for a single block
            ghost_piece_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))

            # Sets the transparency level (0 = invisible, 255 = solid)
            ghost_piece_surface.set_alpha(80)

            # Fills this small surface with the ghost's specific color
            ghost_piece_surface.fill(GHOST_COLOR)

            # Draws (blit) the transparent block onto the main game surface
            surface.blit(ghost_piece_surface, (c * CELL_SIZE, r * CELL_SIZE))

            # Draws a thin white border around the block for better definition
            pygame.draw.rect(surface, WHITE, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def draw_game_over(surface, score, high_score):
    """
    Render the game over screen with score information.
    :param surface: pygame surface where the screen is drawn.
    :type surface: pygame.Surface.
    :param score: current game score.
    :type score: int.
    :param high_score: best recorded score.
    :type high_score: int.
    :returns: None.
    :rtype: None.
    """
    # Renders text objects (converts strings into images)
    text1 = LARGE.render("GAME OVER", True, (220, 20, 20))
    text2 = MEDIUM.render(f"Score: {score}", True, WHITE)
    text3 = MEDIUM.render(f"High Score: {high_score}", True, GOLD)
    text4 = SMALL.render("Press R to Restart", True, WHITE)

    # Draws (blit) the text at the center of the screen with vertical spacing
    surface.blit(text1, ((TOTAL_WIDTH - text1.get_width()) // 2, TOTAL_HEIGHT // 2 - 80))
    surface.blit(text2, ((TOTAL_WIDTH - text2.get_width()) // 2, TOTAL_HEIGHT // 2 - 20))
    surface.blit(text3, ((TOTAL_WIDTH - text3.get_width()) // 2, TOTAL_HEIGHT // 2 + 20))
    surface.blit(text4, ((TOTAL_WIDTH - text4.get_width()) // 2, TOTAL_HEIGHT // 2 + 80))


def draw_audio_section(surface, panel_x, music_enabled, music_volume, sfx_enabled, sfx_volume):
    """
    Render audio controls including checkboxes and sliders.
    :param surface: pygame surface where controls are drawn.
    :type surface: pygame.Surface.
    :param panel_x: horizontal position of the panel.
    :type panel_x: int.
    :param music_enabled: state of music.
    :type music_enabled: bool.
    :param music_volume: current music volume.
    :type music_volume: float.
    :param sfx_enabled: state of sound effects.
    :type sfx_enabled: bool.
    :param sfx_volume: current sound effects volume.
    :type sfx_volume: float.
    :returns: None.
    :rtype: None.
    """
    # Initializes the starting y-coordinate to the global constant and the size of checkboxes
    start_y = AUDIO_START_Y
    checkbox_size = 20

    # Configures a list to avoid repeating drawing logic for Music and SFX
    audio_configs = [
        ("Music", music_enabled, music_volume, start_y),
        ("Sound Effects", sfx_enabled, sfx_volume, start_y + 50)
    ]

    for label, enabled, volume, y_position in audio_configs:
        # Draws the checkbox outline
        rect = pygame.Rect(panel_x + 20, y_position, checkbox_size, checkbox_size)
        pygame.draw.rect(surface, BLACK, rect, 2)

        if enabled:
            # Draws an 'X' inside the checkbox (if enabled)
            pygame.draw.line(surface, BLACK, rect.topleft, rect.bottomright, 2)
            pygame.draw.line(surface, BLACK, rect.topright, rect.bottomleft, 2)

            # Draws the volume slider (line and knob)
            slider_y = y_position + 30
            pygame.draw.rect(surface, BLACK, (panel_x + 20, slider_y, 120, 4))
            knob_x = panel_x + 20 + int(120 * volume)
            pygame.draw.circle(surface, BLACK, (knob_x, slider_y + 2), 6)

        # Renders the label text using the SMALL font
        surface.blit(SMALL.render(label, True, BLACK), (panel_x + 45, y_position - 2))


def draw_window(surface, grid, score, high_score, next_piece, paused, music_enabled, sfx_enabled, music_volume, sfx_volume):
    """
    Render the entire game interface.
    :param surface: pygame surface where everything is drawn.
    :type surface: pygame.Surface.
    :param grid: current grid matrix.
    :type grid: list[list[tuple[int, int, int]]].
    :param score: current game score.
    :type score: int.
    :param high_score: best recorded score.
    :type high_score: int.
    :param next_piece: next piece to display.
    :type next_piece: Piece.
    :param paused: pause state.
    :type paused: bool.
    :param music_enabled: state of music.
    :type music_enabled: bool.
    :param sfx_enabled: state of sound effects.
    :type sfx_enabled: bool.
    :param music_volume: current music volume.
    :type music_volume: float.
    :param sfx_volume: current sound effects volume.
    :type sfx_volume: float.
    :returns: None.
    :rtype: None.
    """
    # Fills the background with black
    surface.fill(BLACK)

    # Defines the starting X position for the side UI panel
    panel_x = CELL_SIZE * COLUMNS

    # Draws the side panel background rectangle
    pygame.draw.rect(surface, PANEL_COLOR, (panel_x, 0, PANEL_WIDTH, TOTAL_HEIGHT))

    # --- GRID RENDERING ---
    # Loops through the grid matrix and draws blocks that are not BLACK
    for i, row in enumerate(grid):
        for j, color in enumerate(row):
            if color != BLACK:
                rect = (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                # Draws the filled block color
                pygame.draw.rect(surface, color, rect)

                # Draws a white border for visual block separation
                pygame.draw.rect(surface, WHITE, rect, 1)

    # Draws the gray grid lines over the board
    draw_grid(surface)

    # --- UI TEXTS (SCORE & RECORD) ---
    # Uses MEDIUM font for better readability of scores
    surface.blit(MEDIUM.render(f"Score: {score}", True, BLACK), (panel_x + 10, 7))
    surface.blit(MEDIUM.render(f"High Score: {high_score}", True, GOLD), (panel_x + 10, 40))

    # --- COMMANDS LIST ---
    # Renders pre-generated command surfaces
    y = 85
    for text_surface in RENDERED_COMMANDS:
        surface.blit(text_surface, (panel_x + 20, y))
        y += 22

    # --- NEXT PIECE PREVIEW ---
    next_y = TOTAL_HEIGHT - 220
    surface.blit(MEDIUM.render("Next Piece:", True, BLACK), (panel_x + 13, next_y))

    # Calls the preview function to draw the piece shape
    draw_next_piece(surface, next_piece, panel_x + 10, next_y + 50)

    # --- PAUSE OVERLAY ---
    if paused:
        # Uses LARGE font for the main pause message
        text = LARGE.render("PAUSED", True, WHITE)

        # Centers the text automatically within the game grid area
        text_rect = text.get_rect(center = ((CELL_SIZE * COLUMNS) // 2, TOTAL_HEIGHT // 2))
        surface.blit(text, text_rect)

    # --- AUDIO CONTROLS ---
    # Helper call to handle the music and SFX UI section
    draw_audio_section(surface, panel_x, music_enabled, music_volume, sfx_enabled, sfx_volume)