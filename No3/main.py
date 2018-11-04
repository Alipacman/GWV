import numpy as np
import random


#Methods for string array switch
def gamefield_into_array(height, width):

    gamefield_array = np.empty(shape=[height, width], dtype ="str")

    for y in range(height):
        for x in range(width):
            gamefield_array[y][x] = gamefield[((y * width + 1 * y) + x)]

    return gamefield_array

def array_into_gamefield(array):

    gamfield_str = ""

    for y in range(len(array)):
        if y != 0:
            gamfield_str = gamfield_str + "\n"
        for x in range(len(array[0])):
            gamfield_str = gamfield_str + str(array[y][x])

    return gamfield_str


#gameFields and measures
gamefield = open('blatt3_environment.txt', 'r').read()

gamefield_width = gamefield.find("\n")
gamefield_height = int((len(gamefield) - 9)/gamefield_width)


gamefield_array = gamefield_into_array(gamefield_height, gamefield_width)


def find_start_index(height, width):
    for y in range(height):
        for x in range(width):
            if gamefield_array[y][x] == "s":
                return (y,x)

def check_possible_field(y_pos, x_pos):
    return (((y_pos <= gamefield_height and y_pos >= 0) and
             (x_pos <= gamefield_width and x_pos >= 0 )) and
            (gamefield_array[y_pos][x_pos] == " " or
            gamefield_array[y_pos][x_pos] == "g" or
            #take this line out, if robot should not be able to go on already visited field
             gamefield_array[y_pos][x_pos] == "."))

def check_goal(y_pos, x_pos):
    return (gamefield_array[y_pos][x_pos] == "g")

def mark_field_visited(y_pos, x_pos):
    gamefield_array[y_pos][x_pos] == "."

def get_random_direction():
    ''' 0 = up
        1 = right
        2 = down
        3 = left '''
    return random.randint(0,4)

def restart_game():
    print(gamefield)
    gamefield_array = gamefield_into_array(gamefield_height, gamefield_width)
    print(array_into_gamefield(gamefield_array))

def get_direction(y_pos, x_pos):
    while True:
        direction = get_random_direction()

        if direction == 0 and check_possible_field(y_pos + 1,x_pos):
            return (y_pos + 1, x_pos)
        elif direction == 1 and check_possible_field(y_pos,x_pos + 1):
            return (y_pos, x_pos + 1)
        elif direction == 2 and check_possible_field(y_pos - 1,x_pos):
            return (y_pos - 1, x_pos)
        elif direction == 3 and check_possible_field(y_pos,x_pos - 1):
            return (y_pos, x_pos - 1)

def get_step_pos(y_pos, x_pos):
    if check_if_deadend(y_pos,x_pos):
        restart_game()
        return (-1,-1)
    return get_direction(y_pos, x_pos)

#only useful if robot should not be able to go on already visited field
def check_if_deadend(y_pos,x_pos):
    return not (check_possible_field(y_pos + 1,x_pos) or
            check_possible_field(y_pos,x_pos + 1) or
            check_possible_field(y_pos - 1,x_pos) or
            check_possible_field(y_pos,x_pos - 1))

def start_search(y_pos, x_pos):

    start_pos = (y_pos,x_pos)

    current_y = y_pos
    current_x = x_pos

    onGoal = False

    while not onGoal:
        print(array_into_gamefield(gamefield_array))
        gamefield_array[current_y,current_x] = "."

        new_pos = get_step_pos(current_y,current_x)

        if new_pos == (-1,-1):
            current_y = start_pos[0]
            current_x = start_pos[1]
        else:
            current_y = new_pos[0]
            current_x = new_pos[1]

        if check_goal(current_y,current_x):
            onGoal = True

        gamefield_array[current_y][current_x] = "s"

    print("goal at : %d %d" %(current_y, current_x))
    print(array_into_gamefield(gamefield_array))

def main():
    print("height of th gamefield: %s \n width of th gamefield: %d" %(gamefield_height,gamefield_width))

    #print(gamefield)
    #print(gamefield_array)
    #print(array_into_gamefield(gamefield_array))

    start_index = find_start_index(gamefield_height,gamefield_width)

    start_search(start_index[0],start_index[1])

main()
