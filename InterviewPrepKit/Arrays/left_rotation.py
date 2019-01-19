
def gcd(a, b):
    if b == 0:
        return a;
    else:
        return gcd(b, a % b)


def left_rotation(arr, d):
    ''' Juggling Algorithm to rotate array by n rotations'''
    length  = len(arr)
    gcd = gcd(d,length)

    for i in range(gcd):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def main():

    arr = [1,2,3,4,5]
    #print(left_rotation(list,1))
    print(gcd(3,12))

if __name__ =='__main__':
    main()
