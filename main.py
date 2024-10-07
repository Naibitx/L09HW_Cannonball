import random
from math import sin, cos
from matplotlib import pyplot as plt

class Print_Iface: # Making print interface (handles printing and plotting)
    @staticmethod
    def main_print(x,y):
        print(f"The ball is at ({x:.1f}, {y:.1f})")
        plt.scatter(x,y)
        plt.pause(.01)
## Represent a cannonball, tracking its position and velocity.
class Cannonball:
    ## Create a new cannonball at the provided x position.
    #  @param x the x position of the ball
    #
    def __init__(self, x):
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0
    ## Move the cannon ball, using its current velocities.
    #  @param sec the amount of time that has elapsed.
    #
    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec

        self._vy = self._vy - grav * sec

        self._x = self._x + dx
        self._y = self._y + dy
    ## Get the current x position of the ball.
    #  @return the x position of the ball
    #
    def getX(self):
        return self._x

    ## Get the current y position of the ball.
    #  @return the y position of the ball
    #
    def getY(self):
        return self._y
    
    ## Shoot the canon ball.
    #  @param angle the angle of the cannon
    #  @param velocity the initial velocity of the ball
    #
    def shoot(self, angle, velocity, user_grav, print_iface):
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)

        while self.getY() > 1e-14:
            print("The ball is at (%.1f, %.1f)" % (self.getX(), self.getY()))

            plt.scatter(self.getX(), self.getY())
            plt.pause(.01)
            self.move(0.1, user_grav)
class Crazyball(Cannonball): 
    def move (self, sec, grav=9.81):
        if self.getX() < 400: #If position is less than 400, add randomness
            rand_q = random.randrange(0,10) # randomized integers from 0-9
            self._vx += rand_q * 0.1
        super().move(sec, grav) # Call move method from Cannonball

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("[ Cannonball Simulator ]") # Welcomes user to Cannonball Simulator

    velocity=float(input("Enter initial velocity ")) # Tells user to input the initial velovity
    angle=float(input("Enter initial angle (in radians):  ")) # Tells user to input initial angle

    while True: # This displays menu for the users to seect the gravity they want
        print("\n Select Gravity Option: ")
        print("1. Earth Gravity")
        print("2. Moon Gravity")
        print("3. Crazy Trajectory")
        print("4. Quit")

        choice = input("Enter choice: ") # assigns users choice to variable "choice"

        if choice == "1": 
            cannonball = Cannonball(0)
            gravity = 9.81
        elif choice == "2":
            cannonball = Cannonball(0)
            gravity = 1.62
        elif choice == "3":
            cannonball = Crazyball(0) 
            gravity = 9.81
        elif choice == "4":
            print ("Goodbye!") # Displays goodbye message
            break # exits loop
        else:
            print ("Invalid input")
            continue

        print_iface = Print_Iface() #creates object Print_Iface
        cannonball.shoot(angle, velocity, gravity, print_iface) #Shoots the ball

