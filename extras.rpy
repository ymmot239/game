
screen buttons(sets,prompt):
    window:
        window:
            style "say_dialogue"
            text prompt

    vbox style "choice_vbox" xalign 0.5 yalign 0.5 spacing 20 :
        for i in sets[0]:
            image im.Scale("gui/textbox.png",250,35)
        for i in sets[1]:
            image im.Scale("gui/textbox.png",250,30)

    vbox style "choice_vbox" xalign 0.5 yalign 0.5 spacing 20 :
        for i in sets[0]:
            textbutton i action Return(i)
        for i in sets[1]:
            text "{color=#000000}[i]{/color}"
                
    
screen status(number):
    vpgrid:
        cols 3
        rows 3
        xspacing 20
        xsize 1000
        $ values = ["S", "H", "E"]
        for x in range(3):
            text values[x]
            text str(number[x])
            bar:
                value number[x]
                range 99
                xsize 360
                ysize 20
label sleeps(times):
    $number_of_times = 0
    $sanity_boost = 0
    hide screen status
    while number_of_times <times:
        scene black
        show text str(times-number_of_times)+ " Hours left" at topright
        if paranoia == False:
            menu:
                "tiles":
                    call tilestart
                    $sanity_boost+=_return*2
                "flappy":
                    pass
                "catch":
                    pass
                "rhythm":
                    call rhythm_game_entry_label
                    $sanity_boost+=_return//1000
                "fishing":
                    pass
        else:
            menu:
                "memory":
                    pass
                "tiles":
                    call tilestart pass ("hard")
                    $sanity_boost+=_return*2
                "blackjack":
                    call blackjack
                "rhythm":
                    pass
                "catch":
                    pass
        $number_of_times +=1
    $manage.setValues(manage.getValues()[0]+ sanity_boost, manage.getValues()[1], manage.getValues()[2])
    $print("final score")
    $print(sanity_boost)
    scene yay
    show screen status(manage.getValues())
    show text (manage.getTime()) at topright
    return
