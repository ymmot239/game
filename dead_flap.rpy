init python:
    import time

    def isRectangleOverlap(R1, R2):
      if (R1[0]>=R2[2]) or (R1[2]<=R2[0]) or (R1[3]<=R2[1]) or(R1[1]>=R2[3]):
         return False
      else:
         return True

    def bird_update(st):
        birds.vel -= gravity
        birds.y-=birds.vel
        if birds.y >660:
            birds.y=660
        return 0.02
    def bird_event(event,x,y,st):
        if event.type == 1025:
            if event.button == 1:
                birds.vel = 20

    def pipe_update(st):
        for tops in top_pipes:
            tops.x-=10
        for bottoms in bottom_pipes:
            bottoms.x-=10
        if pipes.pointer < len(top_pipes):
            birds.rect = [birds.x, birds.y, birds.x+78, birds.y+58]
            pipes.top_rect = [top_pipes[pipes.pointer].x, top_pipes[pipes.pointer].y, top_pipes[pipes.pointer].x+120, top_pipes[pipes.pointer].y+749]
            pipes.bottom_rect = [bottom_pipes[pipes.pointer].x, bottom_pipes[pipes.pointer].y, bottom_pipes[pipes.pointer].x+120, bottom_pipes[pipes.pointer].y+749]
            #print(birds.rect)
            #print(isRectangleOverlap(birds.rect,pipes.bottom_rect))
            #print()
            if isRectangleOverlap(birds.rect,pipes.bottom_rect):
                pipes.pointer+=1
                print("over")

            elif (birds.x) > top_pipes[pipes.pointer].x+120:
                birds.score +=1
                pipes.pointer+=1
                print("score")
                print(birds.score)
        else:
            print(birds.game)
            birds.game = True
            print(birds.game)

        return 0.02

    def pipe_event(event, x, y, st):
        pass

label setup_icons:
    python:
        bird_path = "images/flappy.png"
        bird_image = Image(bird_path)
        birds = bird.create(Transform(child = bird_image, zoom = 0.25))
        birds.game = False
        birds.vel = 0
        birds.score = 0
        pipes.pointer = 0
        top_pipe_path = "images/toppipe.png"
        top_pipe_image = Image(top_pipe_path)
        bottom_pipe_path = "images/bottompipe.png"
        bottom_pipe_image = Image(bottom_pipe_path)
        for x in range(10):
            random = renpy.random.randint(0,500)
            top_pipes.append(pipes.create(Transform(child = top_pipe_image, zoom = 0.5)))
            top_pipes[x].y = -700+random
            top_pipes[x].x = x*300+500
            bottom_pipes.append(pipes.create(Transform(child = bottom_pipe_image, zoom = 0.5)))
            bottom_pipes[x].y = 200+random
            bottom_pipes[x].x = x*300+500
    e "click to start"
    call screen flappy_bird_game

    e "yay"

    return

    

screen flappy_bird_game:
    frame:
        top_padding 0
        left_padding 0
        add bird
        add pipes
        python:
            if birds.game == True:
                birds.destroy()
                for pipe in top_pipes:
                    pipe.destroy()
                for pipe in bottom_pipes:
                    pipe.destroy()
                print("dead birds")
                bird.redraw()
                renpy.jump("flappy")
            else:
                print("not done")



label flappyded:
    $vel = 0
    $gravity = 3
    $number_of_pipes = 100
    $top_pipes = []
    $bottom_pipes = []
    $bird = SpriteManager(update = bird_update, event = bird_event)
    $pipes = SpriteManager(update = pipe_update, event = pipe_event)
    scene black
    jump setup_icons
    return

label lose:
    scene white

