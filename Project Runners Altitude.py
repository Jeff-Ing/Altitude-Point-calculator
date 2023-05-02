"""
This program ask the user to input its Altitude data and will return its Total climbed, total decent, and net change in altitude
"""
import os
climb_again_bool = False

def climb():
    total_climbed = 0
    total_descended = 0

    # Get the number of altitude readings from the user
    how_many_points = int(input("How many altitude readings do you have?: "))

    # Initialize the points variable
    points = (how_many_points - how_many_points) + 1

    # Check if the number of altitude readings is less than 2
    while how_many_points < 2:
        # If it is, print an error message and ask for a new input
        print("You cannot have less than two points!")
        how_many_points = int(input("How many altitude readings do you have?: "))

    # Create an empty list to store the altitude readings and points
    altitude_list = []

    # Loop until points is equal to how_many_points + 1
    while points != (how_many_points + 1):
        # Get an altitude reading from the user
        altitude_reading = int(input("What is reading " + str(points) + "?: "))
        # Create a tuple with the points and altitude_reading values
        reading = (points, altitude_reading)
        # Append the tuple to the list
        altitude_list.append(reading)
        # Increment the points variable
        points += 1

    # Loop through the altitude_list to calculate the total amount climbed
    for i in range(1, len(altitude_list)):
        if altitude_list[i][1] > altitude_list[i-1][1]: 
            total_climbed += altitude_list[i][1] - altitude_list[i-1][1]

    # Loop through the altitude_list to calculate the total amount descended
    for i in range(1, len(altitude_list)):
        if altitude_list[i][1] < altitude_list[i-1][1]: 
            total_descended += altitude_list[i][1] - altitude_list[i-1][1]

    # Print out the results
    """
    # Print all the data
    print("")
    for reading in altitude_list:
        print("Reading", reading[0], ":", reading[1])
    """
    print("")
    print("Total Climbing up: " + str(total_climbed))
    print("Total Climbing down: " + str(-1 * total_descended))
    print("Net Altitude gain/loss: " + str(total_climbed + total_descended))
    altitude_list.clear()


while climb_again_bool == False:
    climb()
    print("")
    climb_again = input("Would you like me to analyze more data?: ")
    while climb_again != "yes" and climb_again != "no":
        print("Invalid response!")
        climb_again = input("Would you like me to analyze more data?: ")
    if climb_again == "yes":
        os.system('cls')
    else:
        climb_again_bool = True
        os.system('cls')

print("  ____             _")
print(" |  _ \           | |")
print(" | |_) |_   _  ___| |")
print(" |  _ <| | | |/ _ \ |")
print(" | |_) | |_| |  __/_|")
print(" |____/ \__, |\___(_)")
print("         __/ |       ")
print("        |___/        ")
print("")
input("Press the Enter key to close...")