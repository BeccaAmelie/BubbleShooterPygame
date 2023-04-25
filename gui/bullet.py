# import pygame
import pygame

# create Bullet class
class Bullet:
        # variable to control the bullet moving
    __bullet_triggered = False # class variable because bullet should not be shot before the user pressed the space key

    # create init method to construct classes attributes
    def  __init__(self, x, y, radius, colour, speed):
        '''
        constructor to set up bullet class (bullet is a pygame circle)
        create private instance variavles for x coordinate, y coordinate, radius, coulour, speed and triggered status of the bullet
        '''
        # create private instance variables --> instance variables not class variables so that the properties of each created bubble are individual, different instances can be created and commented out as needed
        # bullet radius (int); ; needed to set the size of the bullet to know when its off screen
        self.__radius = radius # instance variable so size of bullet can change
        # bullet colour (list[r,g,b]); needed to draw bullet to window using pygame circle feature (and colouring it)
        self.__colour = colour # instance variable for unique colour of bullet
        # bullet speed; needed to move the bullet up and to sides with paddle
        self.__speed = speed # instance variable so it can be modified based on paddle/bubble speed
        # bullet on x axis (int); needed to locate bullet in accordance with paddle
        self.__x = x # instance variables x & y so its position is variable based on paddle properties
        # bullet on y axis (int); needed to locate bullet in accordance with paddle and upwards if shot
        self.__y = y
        # bullet coordinates with x and y (list); needed to locate bullet in accordance with paddle on x and y axis at the same time
        self.__coordinates = [self.__x, self.__y] # instance variable to accept instance variables x & y 

    def __str__(self):
        '''
        string representation containitng reader-friendly information concerning the object's instance
        - includes colour and position of the Bullet
        '''
        # create string representation
        bullet_info = 'Instance of class Bullet with the colour ' + self.__colour + ' and the coordinates of '+ self.__coordinates + '.'
        # return string for string representaiton
        return bullet_info 

    def draw(self, display):
        '''
        Method to draw the bullet with pygame feature "circle" to the pygame window
        - display window is passed in with this 
        '''
        # draw thee bullet as a circle using the colour, coordinates and radius
        pygame.draw.circle(display, self.__colour, self.__coordinates, self.__radius)

    def move(self, pos: list):
        '''
        method to move the bullet:
        - depending on whether it has been triggered or not (defined in instance variable self.__bullet_triggered)
            - bullet not triggered: move with the coordinates defined within pos (coordinates of the paddle)
            - bullet triggered: bullet leaves paddle and moves vertically (in the direction of bubble location)
        Accepted paramteter: 
        - pos: position where the bullet should be located, if not triggered in [x,y] format, assuming it will always be in that format.
        '''
        # if the Bullet was TRIGGERED
        if Bullet.__bullet_triggered == True:
            # move the Bullet up on the y axis with the speed defined
            self.__y = self.__y - self.__speed
        # if the Bullet is NOT triggered
        else:
            # set its x position to position it on the middle of the paddle
            self.__x = pos[0] + pos[2]//2
            # set its y to position it on top of the paddle
            self.__y = pos[1] - self.__radius
        # update bullet coordinates
        self.__coordinates = [self.__x, self.__y]

    def set_trigger(self, triggered:bool):
        '''
        method called when the user triggers the bullet to emerge from the paddle (called in main)
        --- parameters: 
        • triggered (bool): determining whether the bullet has been triggered (set self.__bullet_triggered to the value inside triggered.
        '''
        # if the bullet was triggered
        if triggered == True:
            # set the class variable to true
            Bullet.__bullet_triggered = True
        # if the bullet was NOT triggered
        if triggered == False:
            # set the class variable to true
            Bullet.__bullet_triggered = False
   
    def wall_collision(self):
        '''
        method to check if the bullet has collided with the wall behind the bubble
        method called in main after bullet has been triggered --> self.__bullet_triggered is True when the function is called
        - bullet collides with the “wall” behind the bubble --> bullet missed the bubble
            - bullet collided with wall behind bubble     --> self.__bullet_triggered = False
            - bullet not collided with wall behind bubble --> self.__bullet_triggered = True 
        '''
        # if the bullet collides with the top of the display
        if self.__y + self.__radius < 0 :
            # set the bullet_triggered to false using the set_trigger method
            self.set_trigger(False)

    def change_speed(self, lower_limit, upper_limit):
        '''
        parameters containing the minimum (lower_limit) and maximum (upper_limit) speed of the bullet
        changes bullet speed to random speed within limits 
        '''
        # import random to use library
        import  random
        # set speed of bullet to a random integer within the limits
        self.__speed = random.randint(lower_limit, upper_limit)

# --- create Getters for the coordinates and size (or radius) of bullet
    def get_bullet_radius(self):
        '''
        getter to return bullet radius
        '''
        return self.__radius

    def get_bullet_coordinates(self):
        '''
        getter to return bullet coordinates
        '''
        return self.__coordinates

    def get_bullet_x(self):
        '''
        getter to return x coordiante of bullet
        '''
        return self.__x

    def get_bullet_y(self):
        '''
        getter to return y coordiante of bullet
        '''
        return self.__y
    
    def get_set_triggered(self):
        '''
        mthod to get information of wether bullet has been triggered
        - for control of functionality while programming
        '''
        print(Bullet.__bullet_triggered)