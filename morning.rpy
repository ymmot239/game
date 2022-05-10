
screen five_buttons():

    window:
        id "window"

    vbox style "choice_vbox" xalign 0.5 yalign 0.5 spacing 20 :
        for i in range(5):
            textbutton str(i) action Return(i + 1)