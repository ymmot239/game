define e = Character("Eileen")

# define the song titles and their files
init python:
    # must be persistent to be able to record the scores
    # after adding new songs, please remember to delete the persistent data

    rhythm_game_songs = [
    Song('Isolation', 'rhythm/audio/Isolation.mp3', 'rhythm/audio/Isolation.beatmap.txt'),
    Song('Positivity', 'rhythm/audio/Positivity.mp3', 'rhythm/audio/Positivity.beatmap.txt'),
    Song('Pearlescent', 'rhythm/audio/Pearlescent.mp3', 'rhythm/audio/Pearlescent.beatmap.txt'),
    Song('Pearlescent - trimmed', 'rhythm/audio/Pearlescent - trimmed.mp3', 'rhythm/audio/Pearlescent - trimmed.beatmap.txt'), # 22 sec, easy to test
    Song('Thoughts', 'rhythm/audio/Thoughts.mp3', 'rhythm/audio/Thoughts.beatmap.txt')
    ]

    # # init
    # if persistent.rhythm_game_high_scores:
    #     for song in songs:
    #         if not song in persistent.rhythm_game_high_scores:
    #             persistent.rhythm_game_high_scores[song] = (0, 0)

# map song name to high scores
default persistent.rhythm_game_high_scores = {
    song.name: (0, 0) for song in rhythm_game_songs
}

# the song that the player chooses to play, set in `choose_song_screen` below
default selected_song = None

label nope:
    scene bg room

    e "Welcome to the Ren'Py Rhythm Game! Choose a lofi song you'd like to play."

    window hide
    call rhythm_game_entry_label

    e "Nice work hitting those notes! Hope you enjoyed the game."

    return