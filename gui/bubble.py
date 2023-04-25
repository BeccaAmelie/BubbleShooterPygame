# import pygame
import pygame
# import random
import random
 # create bulbble class
class Bubble:

    # create init method to construct classes attributes
    def __init__(self, x, y, colour, radius, speed_x, speed_y):
        '''
        constructor to set up bubble class 
        defend parameter choice in comments
        '''
        # create private instance variables --> instance variables not class variables so that several instances of the bubble with unique attributes can be created and commented out as needed
        # bubble on x axis (int); needed to locate the position of the bubble on the x axis
        self.__x = x # instance variables for coordinates: can position bubble differently (i.e. start in left corner)
        # bubble on y axis (int); needed to locate the position of the bubble on the y axis
        self.__y = y
        # bubble radis (int); needed to set the size of the bubble to know when it hit bounds
        self.__radius = radius # instance variable so size of bubble can change
        # bubble coordinates with x and y (list); needed to get the x and y coordinates of the bubble at once & relocate it to x any y position at same time
        self.__coordinates = [self.__x, self.__y] # instance variable to accept instance variables x & y
        # speed of horizontal bubble movement (x-axis; int); needed to define speed bubble moves horizontally for diagonal movement
        self.__speed_x = speed_x # speed instance variables so it can be modified (i.e. create easier and harder versionof game: higher level = faster)
        # vertical speed of bubble movement (y axis; int); needed to define speed bubble moves vertically for diagonal movement
        self.__speed_y = speed_y 
        # both speeds needed because width and height of constraints might be different; i.e. if both the same horizontal might be too fast and never reaches line 
        # colour of bubble (list:[r,g,b]); needed for drawing of bubble to window (and colouring it)
        self.__colour = colour # instance variable so can change colour of bubble
    
    def __str__(self):
        '''
        string representation containing reader-friendly information concerning the object's instance, including the color and 
        position of the Bubble.
        '''
        # create string representation
        bubble_info = 'Instance of class bubble with the colour ' + self.__colour + ' and the coordinates of '+ self.__coordinates + '.'
        # return string for string representaiton
        return bubble_info
    
    def draw(self, display):
        '''
        method to draw the bubble on the display window
        - display window is passed in
        - draw bubble with pygame features (circle)
        - Bubble not drawn in other methods.
        '''
        # draw bubble as a circle on pygame display using colour, coordinates and radius instance variables
        pygame.draw.circle(display, self.__colour, self.__coordinates, self.__radius)

    def move(self, horizontal_bound, vertical_bound):
        '''
        method to move the bubble diagonally within constraints of the pygame window (called from main)
        - speed of bubble defined in instance variables (value of programmer's choice) 
        constraints for the bubble:
        - bubble movement constrained within horizontal_bound and vertical_bound
        - bubble changes direction when collides with horizontal_bound
        - bubble relocates to a random position when collides with the vertical_bound (line)
        '''
        # if the bubble has not hit the line
        if self.__y < vertical_bound-self.__radius:
            # --- move bubble diagonally 
            # move it downwards on x-axis
            self.__y += self.__speed_y
            # move it right/left on x-axis
            self.__x += self.__speed_x
            # if bubble hits left or right horizontal bounds
            if self.__x >= horizontal_bound or self.__x <= 0+self.__radius:
                # change direction of bubble's horizontal movement
                self.__speed_x = -self.__speed_x
            # update y coordinate of bubble in coordinates instance variable 
            self.__coordinates[1] = self.__y
            # update x coordinate of bubble in coordinates instance variable 
            self.__coordinates[0] = self.__x
        # if the bubble hit the line
        else:
            # set y-axis position of bubble to random location over line & below vertical bound
            self.__y = random.randint(self.__radius, (vertical_bound-self.__radius))
            # update y coordinate of bubble in coordinates instance variable 
            self.__coordinates[1] = self.__y
            # set y-axis position of bubble to random location in horizontal bounds
            self.__x = random.randint((self.__radius*2), (horizontal_bound-self.__radius))
            # update x coordinate of bubble in coordinates instance variable 
            self.__coordinates[0] = self.__x
            
    def relocate(self, horizontal_bound, vertical_bound):
        '''
        Method to generate a new random position for the bubble within the horizontal and vertical bounds passed in as parameters
        '''
        # set y-axis position of bubble to random location over line & below vertical bound
        self.__y = random.randint(self.__radius, vertical_bound-self.__radius)
        # set y-axis position of bubble to random location in horizontal bounds
        self.__x = random.randint((self.__radius*2), (horizontal_bound-self.__radius))
        # update coordinates of bubble in coordinates instance variable 
        self.__coordinates = [self.__x, self.__y] 

    def change_size(self, lower_limit, upper_limit, resize_factor):
        '''
        Method to change bubble size between lower and upper limits (inclusive of both) given as parameters
        '''
        # check if the radius if changed is still within the upper and lower limit
        # if would be out of limits 
        if not self.__radius + resize_factor <= upper_limit or not self.__radius + resize_factor >= lower_limit:
            # turn the resize_factor around
            resize_factor=-resize_factor
        # add resize factor to radius
        self.__radius = self.__radius + resize_factor
        # return the new resize factor (to keep it updated: change direction only when a limit would be surpassed)
        return(resize_factor)



# --- creating getters for the x, y, and size the bubble
    def get_bubble_x(self):
        '''
        getter to return x coordinate of the bubble
        '''
        return self.__x
    def get_bubble_y(self):
        '''
        getter to return y coordinate of the bubble
        '''
        return self.__y
    def get_bubble_size(self):
        '''
        getter to return bubble size (radius)
        '''
        return self.__radius
