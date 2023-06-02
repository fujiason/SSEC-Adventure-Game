# https://docs.google.com/document/d/1egzfjKQoo_qoXJP2Mq4tXOnI8xS0JaG8Sgi4njO6PX4/edit
import pygame

# pygame stuff
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

location = "pond"
items = {"nylon": 0, "smoker": 0, "ice": 0, "jellybean": 0, "weatherballoon": 0, "rope": 0, "bee": 0, "bucket": 0, "water": 0}
events ={"AERI": 0, "LIDAR": 0, "HSRL": 0, "umbrella": 0, "roof": 0, "jellybean": 0, "ants": 0, "beekeeper": 0, "well": 0, "cloud": 0, "pond": 0, "ending": 0}

# Code or level of completion for minigames
HSRL = [0, 0, 0, 0, 0] # if sum is 5 then minigame is solved
HSRLprev = -1 # don't set to modded number but if this number mod 5 matches with the selected number mod 5, update HSRL list at position and reset this to -1
AERI = 0 # minigame is solved if all levels are passed (becomes a 4)
LIDAR = "" # minigame is solved if given the right combo
jellybeans = "" # minigame is solved if given the right code

# mouse stuff
click = False
cursor = pygame.image.load("./sketches/cursor.png")
cursor_up = pygame.image.load("./sketches/cursor_up.png")
pygame.mouse.set_visible(False)
width = screen.get_width()
height = screen.get_height()
mouse = pygame.mouse.get_pos()

# when game boots up
def startgame():
    pass

# starting area (left is SSEC, right is beekeeper)
def pond():
    global location, items, events, mouse, click
    background = pygame.image.load("./sketches/pond.png")
    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, "red",[width/2,height/2,140,40])
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        screen.blit(cursor_up, mouse)
        if click:
            location = "parking"
    else:
        screen.blit(cursor, mouse)
    click = False


# SSEC front door (left is parking lot, up is SSEC office, right is starting area) [ice cream man and Doppler Lidar]
def entrance():
    global location, items, events, mouse, click
    background = pygame.image.load("./sketches/entrance.png")
    screen.blit(background, (0, 0))

    # Change mouse cursor if on button and switch modes when clicked
    pygame.draw.rect(screen, "red",[0,0,140,40])
    if 1 <= mouse[0] <= 140 and 1 <= mouse[1] <= 40:
        screen.blit(cursor_up, mouse)
        if click:
            location = "pond"
    else:
        screen.blit(cursor, mouse)
    click = False

# SSEC parking lot (right is SSEC front door, left is ant colony, up is SPARC) [rope and ant colony and surface met]
def parking():

    global location, items, events, mouse, click, AERI, LIDAR, HSRL

    # if minigame is done already, set to false
    minigame = True

    background = pygame.image.load("./sketches/entrance.png")
    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, "red",[0,0,140,40])
    if 1 <= mouse[0] <= 140 and 1 <= mouse[1] <= 40:
        screen.blit(cursor_up, mouse)
        if click and minigame:
            location = "lidar"
    else:
        screen.blit(cursor, mouse)
    click = False

    # on button press


# Ant colony (down is SSEC parking lot) [queen bee]
def ant():
    pass

# SSEC office (down is SSEC front door, right is cloud creation room, up is roof)
def office():
    pass

# beekeeper (left is starting area) [well is located here, smoker]
def bee():
    pass

# ice cream man [ice]
def ice():
    pass

# SSEC roof (down is SSEC office) [jelly bean information]
def roof():
    pass

# SPARC inside (down is SSEC parking lot) [nylon]
def sparc():
    pass

# cloud creation room
def cloud():
    pass

# ends the game
def endgame():
    pass

# uses item in hotbar (no use button)
def item(item1):
    pass

def lidar():
    global location, items, events, mouse, click, AERI, LIDAR, HSRL

    background = pygame.image.load("./sketches/entrance.png")
    screen.blit(background, (0, 0))

    # Change mouse cursor if on button and switch modes when clicked
    pygame.draw.rect(screen, "red",[0,0,40,40])
    pygame.draw.rect(screen, "blue",[40,0,40,40])
    pygame.draw.rect(screen, "green",[0,40,40,40])
    pygame.draw.rect(screen, "black",[40,40,40,40])
    pygame.draw.rect(screen, "yellow",[80,0,40,40])
    pygame.draw.rect(screen, "orange",[0,80,40,40])

    if click:
        if 0 <= mouse[0] <= 40 and 0 <= mouse[1] <= 40:
            LIDAR += "a"
        elif 40 <= mouse[0] <= 80 and 0 <= mouse[1] <= 40:
            LIDAR += "b"
        elif 0 <= mouse[0] <= 40 and 40 <= mouse[1] <= 80:
            LIDAR += "c"
        elif 40 <= mouse[0] <= 80 and 40 <= mouse[1] <= 80:
            LIDAR += "d"
        elif 80 <= mouse[0] <= 120 and 0 <= mouse[1] <= 40:
            LIDAR = ""
        elif 0 <= mouse[0] <= 40 and 80 <= mouse[1] <= 120:
            if LIDAR == "abcd":
                print("Yes", LIDAR)
            else:
                print("No", LIDAR)
    else:
        screen.blit(cursor, mouse)
    click = False

def aeri():
    global location, items, events, mouse, click, AERI, LIDAR, HSRL

    # Change mouse cursor if on button and switch modes when clicked
    pygame.draw.rect(screen, "red",[0,0,40,40])
    pygame.draw.rect(screen, "blue",[40,0,40,40])
    pygame.draw.rect(screen, "green",[0,40,40,40])
    pygame.draw.rect(screen, "black",[40,40,40,40])

    if click:
        if AERI == 0:
            background = pygame.image.load("./sketches/entrance.png")
            screen.blit(background, (0, 0))
            if 0 <= mouse[0] <= 40 and 0 <= mouse[1] <= 40:
                AERI += 1
            else:
                print("Try again")
        elif AERI == 1:
            background = pygame.image.load("./sketches/entrance.png")
            screen.blit(background, (0, 0))
            if 40 <= mouse[0] <= 80 and 0 <= mouse[1] <= 40:
                AERI += 1
            else:
                print("Try again")
        elif AERI == 2:
            background = pygame.image.load("./sketches/entrance.png")
            screen.blit(background, (0, 0))
            if 0 <= mouse[0] <= 40 and 40 <= mouse[1] <= 80:
                AERI += 1
            else:
                print("Try again")
        elif AERI == 3:
            background = pygame.image.load("./sketches/entrance.png")
            screen.blit(background, (0, 0))
            if 40 <= mouse[0] <= 80 and 40 <= mouse[1] <= 80:
                AERI += 1
            else:
                print("Try again")
    else:
        screen.blit(cursor, mouse)
    click = False

# ------ Start Game ------ #

pygame.init()

while running:

    # Reset mouse position
    mouse = pygame.mouse.get_pos()

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

    if location == "pond":
        pond()
    elif location == "entrance":
        entrance()
    elif location == "parking":
        parking()
    elif location == "lidar":
        lidar()


    # create hotbar with combine and use buttons


    # starting area (left is SSEC, right is beekeeper)


    # SSEC front door (left is parking lot, up is SSEC office, right is starting area) [ice cream man and Doppler Lidar]


    # SSEC parking lot (right is SSEC front door, left is ant colony, up is SPARC) [rope and ant colony and surface met]


    # Ant colony (down is SSEC parking lot) [queen bee]


    # SSEC office (down is SSEC front door, right is cloud creation room, up is roof)


    # beekeeper (left is starting area) [well is located here, smoker]


    # ice cream man [ice]


    # SSEC roof (down is SSEC office) [jelly bean information]


    # SPARC inside (down is SSEC parking lot) [nylon]


    # cloud creation room [ends game]




    # Display Game
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()