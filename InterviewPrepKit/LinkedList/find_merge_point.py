def find_merge_node(head1, head2):

    current_one = head1
    current_two = head2
    while current_one.next and current_two.next != None:
        if current_one.next != current_two.next :
            current_one = current_one.next
        else:
            return current_one.next.data



def main():
    pass

if __name__ == "__main__":
    main()
