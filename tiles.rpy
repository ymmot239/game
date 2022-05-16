init python:

    # DEFAULT GAME SETTINGS:

    # default card type set
    all_cards = ['+2', '+1', '+0',"-1","-2"]
    # width and height of the field
    ww = 4
    hh = 4
    # how many cards can be opened for 1 turn
    max_c = 2
    # text size in the card for text mode
    card_size = 48
    # time allocated for the passage
    max_time = 25
    # pause before the cards disappear
    wait = 0.5
    # mode of cards with images, not with the text
    img_mode = True

    values_list = []
    temp = []
    # we announce picture cards
    # must be in the format "images / card _ *. png"
    # required "card_back.png" and "card_empty.png"
    for fn in renpy.list_files ():
        if fn.startswith ("images/card_") and fn.endswith ((".png")):
            name = fn [12: -4]
            renpy.image ("card" + name, fn)
            if (name != "empty") and (name != "back"):
                temp.append (str (name))
    # if the picture found> 1,
    # then change the set of card types, but the file names
    if len (temp)> 1:
        all_cards = temp
    else:
        # otherwise turn on the text mode,
        # because the pictures are very small
        img_mode = False

    # the function of initializing the playing field
    def cards_init ():
        global values_list
        values_list = []
        while len (values_list) + max_c <= ww * hh:
            current_card = renpy.random.choice (all_cards)
            for i in range (0, max_c):
                values_list.append (current_card)
        renpy.random.shuffle (values_list)
        while len (values_list) <ww * hh:
            values_list.append ('empty')

# screen game
screen memo_scr:
    # timer
    timer 1.0 action If (memo_timer> 1, SetVariable ("memo_timer", memo_timer - 1), Jump ("memo_game_lose")) repeat True
    # field
    grid ww hh:
        align (.5, .5) # in the center
        for card in cards_list:
            button:
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0
                background None
                if card ["c_value"] == 'empty':
                    if img_mode:
                        add "card_empty"
                    else:
                        text "" size card_size
                else:
                    if card ["c_chosen"]:
                        if img_mode:
                            add "card" + card ["c_value"]
                        else:
                            text card ["c_value"] size card_size
                    else:
                        if img_mode:
                            add "card_back"
                        else:
                            text "##" size card_size
                # pressing the button-card
                action If ((card ["c_chosen"] or not can_click), None, [SetDict (cards_list [card ["c_number"]], "c_chosen", True), Return (card ["c_number"])])
    text str (memo_timer) xalign .5 yalign 0.0 size card_size

# the game itself
label memoria_game:
    $ cards_init ()
    $ cards_list = []
    $ score = 0
    python:
        for i in range (0, len (values_list)):
            if values_list [i] == 'empty':
                cards_list.append ({"c_number": i, "c_value": values_list [i], "c_chosen": True})
            else:
                cards_list.append ({"c_number": i, "c_value": values_list [i], "c_chosen": False})
    $ memo_timer = max_time
    # show the game screen
    show screen memo_scr
    # main game loop
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c
        $ final_count = 0
        label turns_loop:
            if turns_left> 0:
                $ result = ui.interact ()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list [result] ["c_number"])
                $ turned_cards_values.append (cards_list [result] ["c_value"])
                $ turns_left -= 1
                jump turns_loop
        # prevent opening of extra cards
        $ can_click = False
        if turned_cards_values.count (turned_cards_values [0])!= len (turned_cards_values):
            $ renpy.pause (wait, hard = True)
            python:
                for i in range (0, len (turned_cards_numbers)):
                    cards_list [turned_cards_numbers [i]] ["c_chosen"] = False
        else:
            $ renpy.pause (wait, hard = True)
            python:
                for i in range (0, len (turned_cards_numbers)):
                    score += int(cards_list [turned_cards_numbers [i]] ["c_value"])/2
                    print(score)
                    cards_list [turned_cards_numbers [i]] ["c_value"] = 'empty'
                for j in cards_list:
                    if j ["c_chosen"] == False:
                        final_count+=1
                if final_count > ww*hh/2:
                    renpy.jump ("memo_game_loop")
                renpy.jump ("memo_game_win")
        jump memo_game_loop

# loss
label memo_game_lose:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    centered "{size=36} Vdul! Re-Try. {/size}"
    jump memoria_game
    
# winnings
label memo_game_win:
    $ renpy.pause (0.2, hard = True)
    hide screen memo_scr

    centered "{size=36} {b} Winning! {/b} {/size}\n Score = [score]"
    return

# start-up example
label tilestart:
     scene black
     call memoria_game
     scene yay
     return
