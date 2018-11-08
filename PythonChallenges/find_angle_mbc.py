import math

def find_angle(lenght_ab, length_bc):
    """ Finds the unknown angle in degree """
    angle_unknown = math.atan2(lenght_ab, length_bc)
    return int(round(math.degrees(angle_unknown)))

def main():
   ab = int(input())
   bc = int(input())
   print("{}°".format(find_angle(ab,bc)))


if __name__ == '__main__':
    main()
