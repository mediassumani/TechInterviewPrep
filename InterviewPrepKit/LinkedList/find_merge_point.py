''' Solved with help from Artelius on Stack Overflow'''

def find_merge_node(head1, head2):

    currentA = head1
    currentB = head2

    while currentA != currentB:
        if currentA.next == None :
            currentA = head1
        else:
            currentA = currentA.next;

        if currentB.next == None :
            currentB = head2
        else:
            currentB = currentB.next
    return currentB.data

def main():
    pass

if __name__ == "__main__":
    main()
