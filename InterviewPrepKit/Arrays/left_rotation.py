
def find_gcd(a, b):
    if b == 0:
        return a;
    else:
        return find_gcd(b, a % b)


def left_rotation(arr, d):
    ''' Juggling Algorithm to rotate array by n rotations'''
    length  = len(arr)

    for i in range(find_gcd(length,d)):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= length:
                k = k - length
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def main():

    arr = [1,2,3,4,5]
    left_rotation(arr,1)
    for i in range(len(arr)):
        print ("% d" % arr[i], end =" ")

if __name__ =='__main__':
    main()
