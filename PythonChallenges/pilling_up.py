"""
Given an array of cubes lined horizaontaly, check if the cubes are stackable. If yes print "Yes", else print "No".
    - Start with the left most and right most
    -  If left most is >= to right most
        - Then side length of cube on the length is greater than the one on the rigth
"""

def is_stackable(cubes):
    """ Checks if an array of cube is fully(with all elements) stackable"""

    counter = 0
    for cube in cubes:
        
        cube_i = cubes[counter] # grabs the left most element
        cube_j = cubes[(len(cubes) - 1) - counter] # grabs the right most element
        
        # can only perform len/2 operations since we're comparing
        if counter >= len(cubes)/2:
            break
            # if left is >= right
        if cube_i >= cube_j:
            # go to the next element
            counter += 1
            # if right is > left, then the cube on top will be bigger than the one at the bottom
        elif cube_j > cube_i:
            print("No")
            return

    print("Yes")

def main():

    cube_one = [4,3,2,1,3,4]
    cube_two = [1,3,2]
    is_stackable(cube_one) # prints Yes
    is_stackable(cube_two) # prints No

if __name__ == '__main__':
    main()
