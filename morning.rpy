
screen buttons(sets):

    window:
        id "window"

    vbox style "choice_vbox" xalign 0.5 yalign 0.5 spacing 20 :
        for i in sets[0]:
            image im.Scale("gui/textbox.png",200,35)
        for i in sets[1]:
            image im.Scale("gui/textbox.png",200,30)

    vbox style "choice_vbox" xalign 0.5 yalign 0.5 spacing 20 :
        for i in sets[0]:
            textbutton i action Return(i)
        for i in sets[1]:
            text i
            
    
            
screen status(number):
    vpgrid:
        cols 1
        spacing 20
        for x in range (3):
            bar:
                value number[x]
                range 100
                xsize 360
                ysize 20
                
                
