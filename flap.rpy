init python:
    import time
    def bird_update(st):
        birds.vel -= gravity
        #birds.y-=birds.vel
        return 0.1
    def bird_event(event,x,y,st):
        if event.type == 1025:
            if event.button == 1:
                print("yay")
                birds.vel = 15

label setup_icons:
    python:
        bird_path = "images/flappy.png"
        bird_image = Image(bird_path)
        birds = bird.create(Transform(child = bird_image, zoom = 0.25))
        birds.vel = 0
        
        pipe_path = "images/pipe.png"
        pipe_image = Image(pipe_path)
        all_pipes.append(pipes.create(pipe_image))
    call screen game
    call screen pipe
    

screen game:
    frame:
        xalign 0.5
        yalign 0.5
        xsize 78
        ysize 59
        top_padding 0
        left_padding 0
        add bird at center

screen pipe:
    frame:
        xalign 0.1
        yalign 0.5
        xsize 100
        ysize 100
        add pipes

label flappy:
    $vel = 0
    $gravity = 2
    $number_of_pipes = 100
    $all_pipes = []
    $bird = SpriteManager(update = bird_update, event = bird_event)
    $pipes = SpriteManager()
    scene black
    call setup_icons


