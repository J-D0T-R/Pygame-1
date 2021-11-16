###   OOP and Pygame   ###
###   James Rutley   ###
###   Start Date: 11/15/2021   ###
###   End Date: 11/15/2021   ###


#Pygame uses OOP to create and maintain inprogam objects and their properties as the code runs.
#A good example of this is the many blobs.
#By using the blob class, a significant amount of space is saved by using the class to create each blob,
#we don’t need to spend the time to create each individual blob and it’s properties with a function, dictionary,
#or some other method. Class attributes allow for us to create things like hit and hurt boxes,
#object collision, and more, because instead of coding for every possible interaction,
#we can essentially create rules for each interaction.
 
#This could be done without OOP, but it would be incredibly difficult and highly impractical.
#You would have to create every individual object, ensure it is constantly maintained,
#and create code for every possible interaction the object could have.
#It would be a huge program and take up a tremendous amount of memory.

# Imports
import pygame
import random

# Variables 
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

STARTING_RED_BLOBS = 10
STARTING_BLUE_BLOBS = 10

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('My Blob World')
clock = pygame.time.Clock()

# Classes
class blob:
    
    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,8)
        self.color = color

    def move(self):
        self.move_x = random.randrange(-2,3)
        self.move_y = random.randrange(-2,3)
        self.x += self.move_x
        self.y += self.move_y
        
        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH
        
        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.y = HEIGHT
        
    def move_y(self):
        self.move_y = random.randrange(-2,3)
        self.y += self.move_y
        
        if self.y < 0: self.y = 0
        
        elif self.y > HEIGHT: self.y = HEIGHT
            
    def move_x(self):
        self.move_x = random.randrange(-2,3)
        self.x += self.move_x
            
        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH
        
    def moving(self):
        which_move = random.randint(1, 3)
        if which_move == 1:
            blob.move(self)
            
        elif which_move == 2:
            blob.move_y(self)
            
        else:
            blob.move_x(self)
        
# Functions 
def draw_environment(blob_list):
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.moving()
    pygame.display.update()
    
def main():
    blue_blobs = dict(enumerate([blob(BLUE) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([blob(RED) for i in range(STARTING_RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs])
        clock.tick(60)

# Main Code 
main()