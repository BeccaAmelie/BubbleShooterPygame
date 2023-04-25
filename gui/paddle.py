# import pygame
import pygame

class Paddle:
    # create init method to construct classes attributes
    def __init__(self,x, y, width, height, color, speed):
        '''
        __init__ constructor to set up the paddle class 
        '''
        # create private instance variables --> instance variables not class variables so that several instances of the paddle with unique attributes can be created and commented out as needed
        # paddle on x axis (int); needed to locate the position of the paddle on the x axis 
        self.__x = x # instance variables for coordinates: can position paddle differently (i.e. start in left corner)
        # paddle on y axis (int); needed to locate the position of the paddle on the y axis
        self.__y = y 
        # paddle with (int); needed to give the paddle a width for drawing it to the screen using pygame features
        self.__width= width # instance variables for paddle size so it can be wider/higher,...
        # paddle height (int); needed to give the paddle a heigth for drawing it to the screen using pygame features
        self.__height = height
        # paddle coordinates containing, x, y, width and height; needed to create getters more easily and access all paddle coordinates at the same time for repositioning
        self.__coordinates = [self.__x, self.__y, self.__width, self.__height] # instance variable to accept instance variables 
        # colour of paddle (list[r,g,b]); needed for drawing of paddle to window (and colouring it)
        self.__color = color # instance variable so colour is variable
        # speed of paddle moving (int); needed to move paddle on the screen
        self.__speed = speed # instance variable so that speed of paddle can be changed

    def __str__(self):
        '''
        string representation containing eader friendly information concerning the object's instance
        '''
        paddle_info ='Instance of class paddle with the colour ' + self.__color + ' and the coordinates of '+ self.__coordinates + '.'
        return paddle_info
    
    def draw(self, display):
        '''
        Method to draw the paddle on the display window using pygame features (called from main)
        Only method where paddle is drawn
        ''' 
        # draw rectangle using pygame feature using pygame display, colour parameter and coordinates
        pygame.draw.rect(display, self.__color, self.__coordinates)

    def move_left(self):
        '''
        Method to move paddle left on x axis when LEFT arrow pressed (called from main if left arrow pressed) 
        speed of paddle defined in a private instance variable "self.__speed_x" containing value of programmer's choice 
        paddle should not move off left of the screen 
        '''
        # if the paddle has not hit the left horizontal bound
        if self.__x > 0:
            # move paddle to the left with the speed defined in the private instance variable self.__speed
            self.__x -= self.__speed
        # if the paddle has hit/exceeded the left horizontal bound and the user keeps pressing the left arrow
        else:
            # don't let it move off the screen (relocate to left bottom corner)
            self.__x = 0 
        # update the coordinates of the paddle
        self.__coordinates = [self.__x, self.__y, self.__width, self.__height]

           
    def move_right(self, display_width):
        '''
        method to move the paddle right on the x axis (called rom main if right arrow pressed)
        - speed of paddle movement defined as private instance variable  self.__speed
        - paddle should not move off right of the screen 
        - no drawing paddle in this method
        '''
        # if the paddle has not hit the right horizontal bound
        if self.__x < display_width-self.__width: 
            # move paddle to the right with the speed defined in the private instance variable self.__speed
            self.__x += self.__speed
        # if the paddle has hit/exceeded the right horizontal bound and the user keeps pressing the right arrow
        else:
            # don't let it move off the screen (relocate to right bottom corner)
            self.__x=display_width-self.__width
        # update the coordinates of the paddle
        self.__coordinates = [self.__x, self.__y, self.__width, self.__height]

# --- getter methods
    def get_paddle_x_coordinate(self):
        '''
        method to get x coordinate of paddle 
        '''
        return self.__coordinates[0]
    def get_paddle_y_coordinate(self):
        '''
        method to get y coordinate of paddle 
        '''
        return self.__coordinates[1]
    def get_paddle_coordinates(self):
        '''
        method to get x and y coordinates of paddle
        '''
        return self.__coordinates[:2]
    def get_paddle_coordinates_and_size(self):
        '''
        method to get x, y, width and height of paddle 
        '''
        return self.__coordinates
    def get_paddle_size(self):
        '''
        method to get size of paddle 
        '''
        return self.__coordinates[2:]
