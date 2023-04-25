# --- main.py to create interactions between classes and set up pygame window

# import pygame to use its features
import pygame 
# import Bubble class
from bubble import Bubble
# import paddle class
from paddle import Paddle
# import Bullet class
from bullet import Bullet
from math import sqrt

# initialise pygame
pygame.init()

# --- initialise display characteristics
# set the background colour to black
background = [0,0,0]
# set the display width and height (here. to 600px)
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
# create list for display size out ot display width and height
DISPLAY_SIZE = [DISPLAY_WIDTH, DISPLAY_HEIGHT]
# set up pygame display 
display = pygame.display.set_mode(DISPLAY_SIZE)
# initialise pygame time/clock
clock = pygame.time.Clock()

# CREATE CLASS INSTANCES

# --- create instance of BUBBLE

# set up instance of bubble
# create bubble radius variable  
bubble_radius = (DISPLAY_WIDTH+DISPLAY_HEIGHT)/50

#create speed variable to be used for speed_x and speed_y
bubble_speed = 1

# create instance of BUBBLE
bubble_instance = Bubble(DISPLAY_WIDTH//2, DISPLAY_HEIGHT-(DISPLAY_HEIGHT-bubble_radius), [150, 0, 100], bubble_radius, bubble_speed, bubble_speed) #self, x, y, colour, radius, speed_x, speed_y
resize_factor = (bubble_radius*2)//10
# --- create instance of PADDLE 

# setup fot instance of paddle
# create paddle_width variable according to DISPLAY_WIDTH
paddle_width = DISPLAY_WIDTH//10
# create paddle_height variable according to paddle_with
paddle_height = paddle_width//3
# paddle_x coordinate is the middle of the display (subtract paddle_width//2 because rectangle draws from upper left corner)
paddle_x = DISPLAY_WIDTH//2-paddle_width//2
# set height of paddle to display height (bottom of display); subtract paddle height because rectangle draws from upper left corner (else exceeds display height and is not visible)
paddle_y = DISPLAY_HEIGHT-paddle_height
# create paddle colour variable 
paddle_colour = [0,255,255]
# create paddle speed
paddle_speed = bubble_speed*5

# create instance of PADDLE
paddle_instance = Paddle(paddle_x, paddle_y, paddle_width, paddle_height, paddle_colour, paddle_speed)

# --- create instance of BULLET

# setup fot paddle_instance
# set bullet radius to half of bubble
bullet_radius = bubble_radius//2
# position bullet on middle of screen / x-axis
bullet_x = DISPLAY_WIDTH//2
# positon bullet on paddle
bullet_y = DISPLAY_HEIGHT-paddle_height-bullet_radius
# variable to store speed of the bullet
bullet_speed = bubble_speed *5

# create instance of BULLET
bullet_instance = Bullet(bullet_x, bullet_y, bullet_radius, [255, 255, 255], bullet_speed) #x, y, colour, radius, speed_x, speed_y

#create line_with variable 
line_width = 5

# set run_game to true so the game loop can run
run_game = True
# set moveleftbool to move paddle (with bullet if bullet on paddle) left to false
moveleftbool = False
# set moverightbool to move paddle (with bullet if bullet on paddle) right to false
moverightbool = False
# set shootbool to shoot bullet to false
shootbool = False
# get coordinated of the paddle to later move the bullet with the paddle coordinates
paddle_coord = paddle_instance.get_paddle_coordinates_and_size()

# --- CREATE GAME LOOP
while run_game:
   # fill background
   display.fill(background)
   # --- prepare drawable elements
   # draw bubble to window
   bubble_instance.draw(display)
   # create vertical_bound variable according to DISPLAY_HEIGHT
   vertical_bound = DISPLAY_HEIGHT//2
   # horizontal bound is DISPLAY_WIDTH-bubble_radius
   horizontal_bound = DISPLAY_WIDTH-bubble_instance.get_bubble_size()
   # draw the line to window 
   pygame.draw.line(display, [0,255,0], [0, vertical_bound], [DISPLAY_WIDTH, vertical_bound],line_width)
   # draw the paddle
   paddle_instance.draw(display)
   # draw the bullet 
   bullet_instance.draw(display)
   # move the bubble 
   bubble_instance.move(horizontal_bound, vertical_bound)

   # --- get size and positions of bubble and bullet 
   # get location of bullet on x axis
   bullet_x = bullet_instance.get_bullet_x()
   # get location of bullet on y axis
   bullet_y = bullet_instance.get_bullet_y()
   # get radius of bullet
   bullet_size = bullet_instance.get_bullet_radius()

   # get radius of bubble 
   bubble_size = bubble_instance.get_bubble_size()
   # get location of bubble on x axis
   bubble_x = bubble_instance.get_bubble_x()
   # get location of bubble on x axis
   bubble_y = bubble_instance.get_bubble_y()
   distance = sqrt((bubble_x-bullet_x)**2+(bubble_y-bullet_y)**2) 
   # if the distace between bubble and bullet is smaller or equal to the sum of their radii (aka if they collide)
   if distance < bubble_size+bullet_size:
      # relocate the bubble to a random position
      bubble_instance.relocate(horizontal_bound, vertical_bound) 
      # relocate bullet to board after hitting so that bubble is not relocated over and over again
      bullet_instance.wall_collision()
      # change the bubbles size using calling the change_size method with the bubble_radius as a minimum, double it as maximum radius and the resize factor
      resize_factor = bubble_instance.change_size(bubble_radius, bubble_radius*2, resize_factor)
      # change the speed of the bullet calling the change_speed method in the bullet.py using half the bullet_speed as the lower and double it as the upper limit
      bullet_instance.change_speed(bullet_speed//2, bullet_speed*2)

# called from ACTION LISTENER
   # if LEFT arrow pressed
   if moveleftbool:
      # call move_left method in paddle to move paddle left
      paddle_instance.move_left()
      # get new paddle coordinates to move bullet with paddle
      paddle_coord = paddle_instance.get_paddle_coordinates_and_size()
      # if the bullet is not shot, otherwise would move with paddle while shot
      if shootbool == False:
         # move the bullet with the (coordinates of) the paddle
         bullet_instance.move(paddle_coord)
   if moverightbool:
      # call move_right method in paddle to move paddle right, give display_width to create bound (so that paddle does not go off screen)
      paddle_instance.move_right(DISPLAY_WIDTH)
      # get new paddle coordinates to move bullet with paddle
      paddle_coord = paddle_instance.get_paddle_coordinates_and_size()
      # if the bullet is not shot, otherwise would move with paddle while shot
      if shootbool == False:
         # move the bullet with the (coordinates of) the paddle
         bullet_instance.move(paddle_coord)
   # if shootbool was set to true because SPACE was pressed
   if shootbool:
      # call move method in bullet to move bullet up
      bullet_instance.move(paddle_coord)
      # call wall_collision so shootbool is set to false if the bullet has met the top of the y-axis/pygame window
      bullet_instance.wall_collision()
      # if shootbool set to false: wall_collision method calls set_trigger in bullet to set bullet_triggered to false 
      # so that the move method relocates the bullet on top of the paddle

   # --- EVENT LISTENER
   # for every event on the pygame display - loop 
   for event in pygame.event.get():
      # if user has closed the pygame window
      if event.type == pygame.QUIT:
         # set run_game to false to stop GAME LOOP
         run_game = False
      # IF KEY WAS PRESSED
      if event.type == pygame.KEYDOWN:
         # IF DOWN ARROW PRESSED
         if event.key == pygame.K_LEFT: 
            # set moveleftbool to True
            moveleftbool = True
         if event.key == pygame.K_RIGHT: 
            # set moverightbool to True
            moverightbool = True
         # IF SPACE KEY pressed
         if event.key == pygame.K_SPACE:
            # set shootbool to True because bullet was triggered
            shootbool = True
            # call set_trigger method in bullet to set_trigger to True
            bullet_instance.set_trigger(True)

      # IF KEY WAS RELEASED
      if event.type == pygame.KEYUP:
         # if LEFT arrow was released
         if event.key == pygame.K_LEFT: 
            # set moveleftbool to False
            moveleftbool = False
         # if RIGHT arrow was released
         if event.key == pygame.K_RIGHT: 
            # set moverightbool to False
            moverightbool = False

   # update framerate
   clock.tick(70)
   # update display
   pygame.display.update()

# quit pygame 
pygame.quit()
# quit application
quit()