import pygame

def init_audio():
    """
    Initialize audio system and load all sounds.
    :param: none.
    :type: none.
    :returns: dictionary containing audio settings and sound objects.
    :rtype: dict.
    """
    # Initializes the pygame mixer with a standard frequency to ensure that sounds are played back with good quality.
    pygame.mixer.init(frequency = 44100)

    # Loads sound effects and music from local files
    rotate = pygame.mixer.Sound("assets/sounds/rotate.wav")
    drop = pygame.mixer.Sound("assets/sounds/drop.wav")
    clear = pygame.mixer.Sound("assets/sounds/clear.wav")
    hard_drop = pygame.mixer.Sound("assets/sounds/lock.wav")
    game_over = pygame.mixer.Sound("assets/sounds/game_over.wav")
    pygame.mixer.music.load("assets/music/tetris_slow.mp3")
    pygame.mixer.music.play(-1) # '-1' -> Play music on loop

    # Default audio settings
    audio = {
        "music_enabled": True,
        "sfx_enabled": True,
        "music_volume": 0.5,
        "sfx_volume": 0.5,
        "current_music": "slow",
        "dragging_music": False,
        "dragging_sfx": False,
        "rotate": rotate,
        "drop": drop,
        "clear": clear,
        "hard_drop": hard_drop,
        "game_over": game_over,
        "sounds": [rotate, drop, clear, hard_drop, game_over]
    }

    # Applies initial volume
    pygame.mixer.music.set_volume(audio["music_volume"])
    for s in audio["sounds"]:
        s.set_volume(audio["sfx_volume"])

    return audio

def update_music(fall_speed, audio):
    """
    Update background music based on fall speed.
    :param fall_speed: current falling speed.
    :type fall_speed: float.
    :param audio: audio configuration dictionary.
    :type audio: dict.
    :returns: None.
    :rtype: None.
    """
    # Decides which music to play based on pieces' fall speed
    if fall_speed > 0.6 and audio["current_music"] != "slow":
        track = "assets/music/tetris_slow.mp3"
        audio["current_music"] = "slow"
    elif 0.3 < fall_speed <= 0.6 and audio["current_music"] != "medium":
        track = "assets/music/tetris_medium.mp3"
        audio["current_music"] = "medium"
    elif 0.1 < fall_speed <= 0.3 and audio["current_music"] != "fast":
        track = "assets/music/tetris_fast.mp3"
        audio["current_music"] = "fast"
    elif fall_speed <= 0.1 and audio["current_music"] != "super_fast":
        track = "assets/music/tetris_super_fast.mp3"
        audio["current_music"] = "super_fast"
    else:
        return

    # Loads and plays the new track
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(audio["music_volume"])