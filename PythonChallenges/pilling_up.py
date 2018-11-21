def is_stackable(cubes):

    counter = 0
    for cube in cubes:
        cube_i = cubes[counter]
        cube_j = cubes[(len(cubes) - 1) - counter]

        if counter >= len(cubes)/2:
            break
        if cube_i >= cube_j:
            counter += 1
        elif cube_j > cube_i:
            print("No")
            return

    print("Yes")

def main():

    cube_one = [4,3,2,1,3,4]
    cube_two = [1,3,2]
    is_stackable(cube_one)
    is_stackable(cube_two)

if __name__ == '__main__':
    main()
