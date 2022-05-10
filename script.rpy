﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init python:
    import manage as m
    manage = m.Manager()
    print(manage.getTime())

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show text (times.getTimeString()) at topleft

    e "you wake up"
    #  $test = manage.getTime()
    #  e "[test]"

    show eileen animated
    call screen five_buttons
    with dissolve
    menu:

        "wake up":
            jump next
        "oversleep":
            jump next

label next:

    $ renpy.fix_rollback()

    e "what's next?"

    return
