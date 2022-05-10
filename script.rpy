# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("")

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
    show screen status(manage.getValues())

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show text (manage.getTime()) at topright
        

    e "you wake up"
    while manage.getValues()[0]>0:
        show text (manage.getTime()) at topright
        $test = manage.getChoices()
        call screen buttons(test)
        with dissolve
        $final = manage.makeChoice(_return)
        show screen status(final)

        

label next:

    $ renpy.fix_rollback()

    e "ded"

    return
