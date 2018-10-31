def compute(n):
 
    count = 1
    while count <= n:
        print(count,end='')
        count += 1

def main():
  n = int(input())
  compute(n)


if __name__ == '__main__':
    main()
