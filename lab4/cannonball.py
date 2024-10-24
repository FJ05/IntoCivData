from math import sin , cos , radians

def main ():
    angle = float (input ("Enter the launch angle (in degrees): "))
    vel = float (input ("Enter the initial velocity (in meters/sec): "))
    hO = float (input ("Enter the initial height (in meters): "))
    time = float (input (
    "Enter the time interval between position calculations: "))
    # convert angle to radians
    theta = radians (angle)
    
    # set the initial position and velocities in x and y directions
    maximum_ypos = 0
    xpos = 0
    ypos = hO
    xvel = vel * cos (theta)
    yvel = vel * sin (theta)
    # loop until the ball hits the ground
    while ypos >= 0.0:
    # calculate position and velocity in time seconds
        if maximum_ypos < ypos:
            maximum_ypos = ypos # this will make sure that we get the maximum of y
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1)/2.0
        yvel = yvel1
    print ("\nDistance traveled: {0: 0.1f} meters.".format (xpos))
    print ("\nThe maximum hight of the ball was: {0: 0.1f}".format (maximum_ypos))

main()