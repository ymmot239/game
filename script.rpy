# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("")

init python:
    import manage as m
    #import flap as f
    manage = m.Manager()
    print(manage.getTime())

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image yay = (im.Scale("images/bg_room.jpg",1280,720))
    scene yay
    show screen status(manage.getValues())
    $manage.setValues(50,50,50)
    $manage.resetTime()
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show text (manage.getTime()) at topright
    show screen status(manage.getValues())

    while manage.getValues()[0]>0:
        show text (manage.getTime()) at topright
        $test = manage.getChoices()
        call screen buttons(test,manage.getPrompts())
        with dissolve
        $before = manage.getTimeInt()
        $final = manage.makeChoice(_return)
        
        if _return == "sleep":
            if before == 1330:
                call sleeps(1)
            else:
                if before >=1200:
                    call sleeps((manage.getTimeInt()+2400-before) //100)
                else:
                    call sleeps((manage.getTimeInt()-before) //100)
        show screen status(manage.getValues())
        

        

label next:

    $ renpy.fix_rollback()

    e "ded"

    return
    e "yay"
