import pygame 
import math
import random 

## setup display 

pygame.init() # initialize pygame; sets it up
WIDTH, HEIGHT = 800, 500 # define dimensions of screen 
win = pygame.display.set_mode((WIDTH, HEIGHT)) # tell pygame you want those specific dimentions 
pygame.display.set_caption("Hangman") # define game

## button variables 

RADIUS = 20 
GAP = 15 
letters = [] # store buttons; x,y position and what letter it corresponds to  
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13)/2)
starty = 400

A = 65 # how capital A is defined 

for i in range(26): # determine x,y position for each button
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y, chr(A+i), True]) # boolean to determine if button is visible 

## fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

## load images 
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

## game variables 
hangman_status = 0
words = ["JAZZ", "ELEPHANT", "AVENUE", "RAINBOW", "GARDEN"]
word = random.choice(words) # random word to guess
guessed = [] # what letters guessed so far 

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

## create game loop
FPS = 60 # max frames per second 
clock = pygame.time.Clock() # clock object that loop runs at this speed (FPS)
run = True # initialize while loop 


def draw():
    win.fill(WHITE) # set bg display
    
    # title 
    text = TITLE_FONT.render("Initial Hangman", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = "" # blank string 
    for letter in word:
      if letter in guessed:
        display_word += letter + " "
      else:
        display_word += "_ " # spaces for guessing word
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400,200)) # draw word 

    # draw buttons 
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3) # draw center on window, in black, in center, with radius 3 thick
            text = LETTER_FONT.render(ltr,1,BLACK) # draw character on screen (render text)
            win.blit(text, (x-text.get_width()/2,y-text.get_height()/2))

    win.blit(images[hangman_status], (150,100)) # draw image
    pygame.display.update() # update display 
  
def display_message(message):
  pygame.time.delay(1000)
  win.fill(WHITE) # fill screen with white
  text = WORD_FONT.render(message, 1, BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2- text.get_height()/2))
  pygame.display.update() # updates the screen
  pygame.time.delay(3000) # delay; dont do anything for 3 seconds then quits 


while run:
    clock.tick(FPS) # while loop runs at set speed

    for event in pygame.event.get(): # check for events (user initiates)
        if event.type == pygame.QUIT:
           run = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # check each button to see if mouse hit it (collision)
            m_x, m_y = pygame.mouse.get_pos() 
            for letter in letters:
                x, y, ltr, visible = letter 
                if visible: 
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False # letter[3] is where True value is held 
                        guessed.append(ltr) # add guessed letters to guessed list.a
                        if ltr not in word:
                          hangman_status += 1 # update hangman body
    draw()
    
    won = True
    for letter in word: # check if user won
      if letter not in guessed:
        won = False
        break

    if won:
      display_message("You won!")
      break 

    if hangman_status == 6:
      display_message("You lost!")
      break


pygame.quit()
