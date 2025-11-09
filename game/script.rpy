# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pipi")


# The game starts here.

style default:
    antialias False



screen minigame:
    add MinigameManager(50, 5)

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pipi

    # These display lines of dialogue.

    p "Minigame time!"
    hide pipi
    show screen minigame
    $ renpy.pause(999, hard=True)

    p "This should never happen"

    label go_on:
    show pipi happy
    hide screen minigame 
    p "You WIN!"
    return

    label lose:
    hide screen minigame
    show pipi sus2
    p "You LOSE!"
    # This ends the game.
    return

transform fneutral:
    "minigame/fneutral.png"

transform loot:
    "minigame/lsus.png"

transform drink:
    "minigame/fsus.png"

transform toss:
    "minigame/rsus.png"

transform desk:
    "minigame/fg.png"

init python:
    import time
    import math


        
    class Pipi(renpy.Displayable):
        ACTION_DELAY = 0.25

        VALID_PRESSES = {pygame_sdl2.K_UP: "drink", \
                        pygame_sdl2.K_LEFT: "loot", \
                        pygame_sdl2.K_DOWN: "drink", \
                        pygame_sdl2.K_RIGHT: "toss", \
                        pygame_sdl2.K_w: "drink", \
                        pygame_sdl2.K_a: "loot",
                        pygame_sdl2.K_s: "drink", \
                        pygame_sdl2.K_d: "toss" \
                        }
        STATE_TO_TRANSFORM = {"idle": fneutral, "drink": drink, \
                            "loot": loot, "toss": toss}
        def __init__(self):
            super(Pipi, self).__init__()
            self.state = "idle"
            self.current_sprite = Pipi.STATE_TO_TRANSFORM[self.state]
            self.state_deadline = math.inf
        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            if(time.time() >= self.state_deadline):
                self.state = "idle"
                self.current_sprite = Pipi.STATE_TO_TRANSFORM[self.state]
                self.state_deadline = math.inf

            pipi_render = renpy.render(self.current_sprite, width, height, st, at)

            return pipi_render

        def handle_key(self, new_state):
            if(self.state != new_state):
                self.state = new_state
                self.current_sprite = Pipi.STATE_TO_TRANSFORM[self.state]
                self.state_deadline = time.time() + Pipi.ACTION_DELAY




    class MinigameManager(renpy.Displayable):
        def __init__(self, stockpile, game_duration):
            super(MinigameManager, self).__init__()
            self.pipi = Pipi()
            self.stockpile = stockpile
            self.start_time = time.time()
            self.end_time = self.start_time + game_duration
            self.done = False

            self.pipi = Pipi()

        def event(self, ev, x, y, st):
            if ev.type == pygame_sdl2.KEYDOWN and ev.key in Pipi.VALID_PRESSES:
                self.pipi.handle_key(Pipi.VALID_PRESSES[ev.key])

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            pipi_render = self.pipi.render(width, height, st, at)
            desk_render = renpy.render(desk, width, height, st, at)

            # Todo: Fix this shit! 
            if(self.pipi.state == "drink"):
                r.blit(desk_render, (0, 0))
                r.blit(pipi_render, (0, 0))            
            else:
                r.blit(pipi_render, (0, 0))            
                r.blit(desk_render, (0, 0))


            # Check for end of game only once
            if not self.done and time.time() >= self.end_time:
                self.done = True
                if self.stockpile <= 0:
                    renpy.jump("go_on")
                else:
                    renpy.jump("lose")

            renpy.redraw(self, 0.1)
            return r