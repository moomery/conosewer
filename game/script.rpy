# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pipi")
define s = Character("Sylph")


# The game starts here.

style default:
    antialias False

image white = "#fff"
screen minigame2:
    add MinigameManager(48, 180, 1)
screen minigame:
    add MinigameManager(12, 30)

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
    show fg
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
    hide fg
    play music "minigame.mp3"
    show screen minigame
    $ renpy.pause(999, hard=True)

    p "This should never happen"

    label reaching_lose:
    hide screen minigame
    hide screen minigame2
    show bg
    show loss
    show lsus
    show fg
    s "What the--"
    hide loss 
    hide lsus 
    with dissolve
    show sylph sus 
    with dissolve
    s "What is that."
    hide sylph
    show pipi sus
    "I'm sorry, Sylphie."
    jump lose

    label drinking_lose:
    hide screen minigame
    hide screen minigame2
    show bg
    show loss
    show fsus0
    show fg
    s "What the--"
    hide fsus0 
    hide loss
    with dissolve
    show sylph sus
    with dissolve
    s "Really."
    hide sylph
    show pipi sus
    "I'm sorry, Sylphie."
    jump lose

    label tossing_lose:
    hide screen minigame
    hide screen minigame2
    show bg
    show loss
    show rsus
    show fg
    s "What the--"
    hide loss 
    hide rsus 
    with dissolve
    show sylph sus
    with dissolve
    s "What the Hell are you tossing out the window?"
    hide sylph
    show pipi sus2 
    "I--I can explain!"
    jump lose

    label has_bottle_lose:
    hide screen minigame
    hide screen minigame2
    show bg
    show loss
    show punish
    show fg
    s "W--What is that in your inventory!?"
    hide loss
    hide punish
    with dissolve
    show sylph sus
    with dissolve
    s "This is disgusting. You're disgusting."
    hide sylph
    show pipi sus2 
    "W--Wait, I--"
    jump lose

    label lose:
    show loser
    s "Out! Out!"
    "YOU LOSE."
    # This ends the game.
    return
    
    label win:
    $ renpy.music.set_volume(0.00, delay=2, channel='music')                     
    show bg
    show fg
    hide screen minigame
    p "I drank piss all throughout the night."
    p "And Sylph was none the wiser."
    $ renpy.music.set_volume(1.00, delay=0, channel='music')                     
    play music "what.mp3"
    show sylph happy
    with dissolve
    s "Well. Someone's happy today."
    hide sylph
    show pipi sus 
    s "Oh ,you..."
    hide pipi
    show sylph
    s "Lemme give you a kiss!"
    p "No, wait--"
    hide sylph
    with dissolve
    $ renpy.music.set_volume(0.00, delay=0, channel='music')                     
    "Smooch!"
    show sylph sus
    with dissolve
    s "Erm, Pipi..."
    hide sylph
    show pipi sus2
    p "Eheheh... Yes, my love?"
    hide pipi
    show sylph sus
    s "For some reason you taste"
    show sylph 
    $ renpy.music.set_volume(1.00, delay=0, channel='music')                     
    s "FANTASTIC Today!"
    hide sylph
    show pipi sus
    p "Wow!"
    $ renpy.music.set_volume(0.00, delay=2, channel='music')                     
    p "(That night, I received my biggest shipment yet.)"
    p "(I would have to drink gallons and gallons to survive.)"
    hide pipi sus
    show screen minigame2
    $ renpy.music.set_volume(1.00, delay=2, channel='music')                     
    play music "minigame2.mp3"
    $ renpy.pause(999, hard=True)

    label win2:
    $ renpy.music.set_volume(0.00, delay=2, channel='music')                     
    hide room bg
    hide screen minigame2
    p "Months have passed."
    p "I thought I was being so sneaky."
    p "But turns out..."
    s "Pipi? My Cherry Pi?"
    p "...He knew all along."
    $ renpy.music.set_volume(1.00, delay=1, channel='music')                     
    play music "win_song.mp3"
    show sylph
    with dissolve
    s "Hey, Pirocyon..."
    "(Sylphie never uses my full name unless it's important.)"
    hide sylph
    show pipi
    p "Yes, Sylphester?"
    hide pipi
    show sylph sus
    s "You've seemed a bit distant lately..."
    hide sylph
    show pipi sus
    "Oh...!"
    hide pipi
    show sylph happy
    s "You know you can talk to me about anything, right?"
    $ renpy.music.set_volume(0.00, delay=1, channel='music')                     
    hide sylph
    with dissolve
    s "Well..."
    scene white with dissolve

    show win screen with dissolve
    p "I just wish you'd told me sooner!"
    s "Can you blame me? I couldn't drag you into this."
    p "I'm glad you did. It's delicious!"
    "YOU WIN"

    return


transform crates2:
    "minigame/crates2.png"
transform crates1:
    "minigame/crates1.png"
transform crates0:
    "minigame/crates0.png"

transform fneutral:
    "minigame/fneutral.png"

transform loot:
    "minigame/lsus.png"

transform drink:
    "minigame/fsus0.png"
    pause 0.14
    "minigame/fsus1.png"
    pause 0.14
    repeat

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

transform shaking:
    "minigame/bottle.png"
    pause 0.10
    "minigame/bottle2.png"
    pause 0.10
    repeat

transform empt:
    "minigame/bottle2.png"

transform punish:
    "minigame/punish.png"

init python:
    import time
    import math
    import random

    ACTION_MARGIN = 0.25

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
                            "loot": loot, "toss": toss, \
                            "punish": punish}
        def __init__(self, bottle_manager):
            super(Pipi, self).__init__()
            self.bottle_manager = bottle_manager
            self.state = "idle"
            self.current_sprite = Pipi.STATE_TO_TRANSFORM[self.state]
            self.state_deadline = math.inf
            self.lost = False

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            if(time.time() >= self.state_deadline):

                # This SHOULD be where drinking ends.
                if(self.state == "drink"):
                    # Successful drink occurred.
                    renpy.play("drank.mp3")
                    self.bottle_manager.drink()

                self.state = "idle"
                self.current_sprite = Pipi.STATE_TO_TRANSFORM[self.state]
                self.state_deadline = math.inf

            pipi_render = renpy.render(self.current_sprite, width, height, st, at)

            return pipi_render

        def handle_key(self, new_state, difficulty):
            locked = False
            if(new_state == "loot"):
                if(self.bottle_manager.stockpile == 0):
                    renpy.play("no.mp3")
                    locked = True
                else:
                    renpy.play("loot.mp3")
                    if(difficulty == 1):
                        self.bottle_manager.add_bottle(6)
                    else:
                        self.bottle_manager.add_bottle()



            elif(new_state == "drink"):
                success = self.bottle_manager.attempt_drink()
                if(success):
                    renpy.play("drink.mp3")
                else:
                    renpy.play("no.mp3")
                    locked = True
            elif(new_state == "toss"):
                success = self.bottle_manager.attempt_toss()
                if(success):
                    renpy.play("toss.mp3")
                else:
                    renpy.play("no.mp3")
                    locked = True

            if(locked):
                new_state = "punish"

            self.state = new_state
            self.current_sprite = Pipi.STATE_TO_TRANSFORM[self.state]
            self.state_deadline = time.time() + ACTION_MARGIN
            return locked

        def handle_keyup(self):
            if(self.state == "drink"):
                self.bottle_manager.bottle_queue[-1].being_drank = False

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
                    renpy.play("waking.mp3")
                    self.state = "waking"
                else:
                    self.state = "awake"
            if(self.difficulty == 1):
                if(time_since_start%7 < 4):
                    self.state = "asleep"
                elif(time_since_start%7 < 6):
                    renpy.play("waking.mp3")
                    self.state = "waking"
                else:
                    self.state = "awake"


            self.current_sprite = Sylph.STATE_TO_TRANSFORM[self.state]

            sylph_render = renpy.render(self.current_sprite, width, height, st, at)

            return sylph_render

    class Bottle (renpy.Displayable):
        def __init__(self, index, full):
            self.index = index
            self.max_width = 10
            self.full = full
            self.being_drank = False


    class BottleManager (renpy.Displayable):
        def __init__(self, stockpile, game_duration, difficulty=0):
            self.stockpile = stockpile
            self.max_stock = stockpile
            self.game_duration = game_duration
            self.difficulty = difficulty
            self.bottle_queue = []

        def has_full_bottle(self):
            for bottle in self.bottle_queue:
                if(bottle.full):
                    return True
        def add_bottle(self, n = 1):
            for i in range(n):
                if(self.stockpile == 0):
                    continue

                if(self.difficulty == 0):
                    new_full = random.random() < .7
                if(self.difficulty == 1):
                    new_full = random.random() < .3

                self.bottle_queue.append( \
                    Bottle( \
                        len(self.bottle_queue), \
                        new_full \
                        )
                )
                self.stockpile -= 1

        def drink(self):
                self.bottle_queue[-1].being_drank = False
                self.bottle_queue[-1].full = False

        def attempt_drink(self):
            if(not self.bottle_queue):
                return False
            
            if (self.bottle_queue[-1].full):
                self.bottle_queue[-1].being_drank = True
                return True
            return False
            
        def attempt_toss(self):
            if(not self.bottle_queue):
                return False
            
            if(not self.bottle_queue[-1].full):
                self.bottle_queue = self.bottle_queue[:-1]
                return True
            return False

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            # Render the crates
            frac_remaining = (self.stockpile/self.max_stock)
            if(frac_remaining <= 0):
                pass
            elif(frac_remaining < 0.33):
                stack_render = renpy.render(crates0, 0, 0, st, at)
                r.blit(stack_render, (0, 0))            
            elif(frac_remaining < 0.66):
                stack_render = renpy.render(crates1, 0, 0, st, at)
                r.blit(stack_render, (0, 0))            
            else:
                stack_render = renpy.render(crates2, 0, 0, st, at)
                r.blit(stack_render, (0, 0))            


            # Render the bottles
            index = 0
            for bottle in self.bottle_queue:
                bottle_transform = full if bottle.full else empt

                if(bottle.being_drank):
                    bottle_transform = shaking

                bottle_render = renpy.render(bottle_transform, 0, 0, st, at)
                r.blit(bottle_render, (35*(index%11), 35*(math.floor(index/11))))
                index += 1


            return r

    class MinigameManager(renpy.Displayable):
        def __init__(self, stockpile, game_duration, difficulty=0):
            super(MinigameManager, self).__init__()
            self.stockpile = stockpile
            self.start_time = time.time()
            self.end_time = self.start_time + game_duration
            self.difficulty = difficulty
            self.done = False
            self.lost = False
            self.locked_time = -1

            self.bottle_manager = BottleManager(self.stockpile, game_duration, self.difficulty)

            self.pipi = Pipi(self.bottle_manager)
            self.sylph = Sylph(self.start_time, difficulty)

        def event(self, ev, x, y, st):

            # Disallow keypress when punished or drinking
            if(self.pipi.state == "punish"):
                return
            if(self.pipi.state == "drink"):
                # Gotta check if you stopped drinking too early.
                if(ev.type == pygame_sdl2.KEYUP \
                and ev.key in Pipi.VALID_PRESSES):
                    self.pipi.handle_keyup()

                return

            if ev.type == pygame_sdl2.KEYDOWN \
                and ev.repeat == 0 \
                and ev.key in Pipi.VALID_PRESSES:

                # Check for loss condition.
                locked = self.pipi.handle_key(Pipi.VALID_PRESSES[ev.key], self.difficulty)
                if(locked):
                    self.pipi.state = "punish"
                    self.locked_time = time.time()
                    
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

            # Loss conditions:
            if(self.sylph.state == "awake" and self.difficulty == 0):
                if(self.pipi.state == "loot" \
                and self.bottle_manager.bottle_queue[-1].full):
                    renpy.music.set_volume(0.00, delay=0, channel='music') 
                    renpy.play("Whistle.wav")
                    renpy.jump("reaching_lose")
                    
                if(self.pipi.state == "drink"):
                    renpy.music.set_volume(0.00, delay=0, channel='music') 
                    renpy.play("Whistle.wav")
                    renpy.jump("drinking_lose")
                if(self.pipi.state == "toss"):
                    renpy.music.set_volume(0.00, delay=0, channel='music') 
                    renpy.play("Whistle.wav")
                    renpy.jump("tossing_lose")
                if(self.bottle_manager.has_full_bottle()):
                    renpy.music.set_volume(0.00, delay=0, channel='music') 
                    renpy.play("Whistle.wav")
                    renpy.jump("has_bottle_lose")



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
            if self.bottle_manager.stockpile <= 0 \
            and not self.bottle_manager.has_full_bottle():
                if(self.difficulty == 0):
                    renpy.jump("win")
                if(self.difficulty == 1):
                    renpy.jump("win2")

            if not self.done and time.time() >= self.end_time:
                self.done = True
                renpy.jump("lose")

            renpy.redraw(self, 0.1)
            return r