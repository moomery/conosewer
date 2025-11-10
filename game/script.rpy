# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pipi")
define s = Character("Sylph")


# The game starts here.

style default:
    antialias False



screen minigame:
    add MinigameManager(50, 30)

label start:
    "I'd been feeling depressed."

    "Sober for four months, with nothing to show for it."

    "Sylph thinks I'm okay, but every night I dream"

    "of that sweet, sweet ochre fluid:"

    "dehydrated urine."

    play music "what.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pipi

    p "My name is Pipi – pronounced pie-pie – and I have a piss addiction."

    # These display lines of dialogue.

    p "My contacts still send me their piss, I just hide it instead of drinking it."

    hide pipi
    show sylph

    s "Hey, my Cream Pie! What's up, hot stuff?"

    hide sylph
    show pipi sus

    p "(Sylph doesn't know about my secret life. He's too innocent.)"

    show pipi happy

    p "Nothing, Butt Cakes!"

    show pipi sus

    p "(Over the past four months, I've amassed a truly ungodly stockpile of piss.)"

    hide pipi
    show sylph

    s "I'm gonna hit the sack. And I don't mean yours!"

    hide sylph
    show pipi happy

    p "Okay, Sylphie! Good night!"

    show pipi

    p "(This most recent shipment put me over the edge.)"

    p "(I'm ready to break my streak.)"

    p "(Tonight, I feast.)"


    hide pipi
    play music "minigame.mp3"
    show screen minigame
    $ renpy.pause(999, hard=True)

    p "This should never happen"

    label go_on:
    show pipi happy
    hide screen minigame 
    p "You WIN!"
    return

    label lose:
    $ renpy.music.set_volume(0.00, delay=0, channel='music') 
    s "What the--!"
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

transform asleep:
    "minigame/asleep.png"

transform waking:
    "minigame/waking.png"

transform awake:
    "minigame/awake.png"

transform loss:
    "minigame/loss.png"

transform full:
    "minigame/bottle.png"

transform empt:
    "minigame/bottle2.png"

init python:
    import time
    import math

    # Wipe non-mouse bindings, because fuck those.
    wipethis = list(config.keymap.keys())
    for item in wipethis:
        spared = False
        val_list = config.keymap[item]
        for val in val_list:
            if('mouse' in val):
                spared = True
        if not spared:
            config.keymap[item] = None

    class Pipi(renpy.Displayable):
        ACTION_DELAY = 0.2

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
            self.lost = False
        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            if(time.time() >= self.state_deadline):
                self.state = "idle"
                self.current_sprite = Pipi.STATE_TO_TRANSFORM[self.state]
                self.state_deadline = math.inf

            pipi_render = renpy.render(self.current_sprite, width, height, st, at)

            return pipi_render

        def handle_key(self, new_state):
            renpy.play("drink.mp3")
            self.state = new_state
            self.current_sprite = Pipi.STATE_TO_TRANSFORM[self.state]
            self.state_deadline = math.inf

        def handle_keyup(self):
            self.state = "idle"
            self.current_sprite = Pipi.STATE_TO_TRANSFORM[self.state]
            self.state_deadline = math.inf

    class Sylph(renpy.Displayable):
        STATE_TO_TRANSFORM = {"awake": awake, "loss": loss, \
                            "asleep": asleep, "waking": waking}
        def __init__(self, start_time, difficulty):
            super(Sylph, self).__init__()
            self.start_time = start_time
            self.difficulty = difficulty
            self.state = "asleep"
            self.current_sprite = Sylph.STATE_TO_TRANSFORM[self.state]
            self.state_deadline = math.inf

        def render(self, width, height, st, at):
            time_since_start = time.time() - self.start_time
            r = renpy.Render(width, height)

            # LEVEL 1
            if(self.difficulty == 0):
                if(time_since_start%8 < 5):
                    self.state = "asleep"
                elif(time_since_start%8 < 6):
                    self.state = "waking"
                else:
                    self.state = "awake"
            self.current_sprite = Sylph.STATE_TO_TRANSFORM[self.state]

            sylph_render = renpy.render(self.current_sprite, width, height, st, at)

            return sylph_render

    class Bottle (renpy.Displayable):
        def __init__(self, x, y, full):
            self.x = x
            self.y = y
            self.full = full

        def render(self, st, at):
            bottle_transform = full if self.full else empt
            return renpy.render(bottle_transform, self.x, self.y, st, at)

    class BottleManager (renpy.Displayable):
        def __init__(self, stockpile, game_duration, difficulty=0):
            self.stockpile = stockpile
            self.game_duration = game_duration
            self.difficulty = difficulty
        def render(self, width, height, st, at):
            bottle_render = Bottle(width/2, height/2, True).render(st, at)
            return bottle_render

    class MinigameManager(renpy.Displayable):
        def __init__(self, stockpile, game_duration, difficulty=0):
            super(MinigameManager, self).__init__()
            self.stockpile = stockpile
            self.start_time = time.time()
            self.end_time = self.start_time + game_duration
            self.difficulty = difficulty
            self.done = False
            self.lost = False

            self.bottle_manager = BottleManager(self.stockpile, game_duration, self.difficulty)

            self.pipi = Pipi()
            self.sylph = Sylph(self.start_time, difficulty)

        def event(self, ev, x, y, st):
            if ev.type == pygame_sdl2.KEYDOWN \
                and ev.repeat == 0 \
                and ev.key in Pipi.VALID_PRESSES:

                # Check for loss condition.
                self.pipi.handle_key(Pipi.VALID_PRESSES[ev.key])
                if(self.sylph.state == "awake"):
                    self.lost = True
            elif ev.type == pygame_sdl2.KEYUP \
                and ev.key in Pipi.VALID_PRESSES:

                self.pipi.handle_keyup()

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            sylph_render = self.sylph.render(width, height, st, at)
            pipi_render = self.pipi.render(width, height, st, at)
            desk_render = renpy.render(desk, width, height, st, at)
            bottle_bar = self.bottle_manager.render(width, height, st, at)

            r.blit(sylph_render, (0, 0))
            # Todo: Fix this shit! 
            if(self.pipi.state == "drink"):
                r.blit(desk_render, (0, 0))
                r.blit(pipi_render, (0, 0))            
            else:
                r.blit(pipi_render, (0, 0))            
                r.blit(desk_render, (0, 0))

            r.blit(bottle_bar, (0, 0))
            # if self.lost:
            #     renpy.jump("lose")

            # Check for end of game only once
            if not self.done and time.time() >= self.end_time:
                self.done = True
                if self.stockpile <= 0:
                    renpy.jump("go_on")
                else:
                    renpy.jump("lose")

            renpy.redraw(self, 0.1)
            return r