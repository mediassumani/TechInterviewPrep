def merge_changes(time_slots):

    condensed_slots = []

    for index, slot in enumerate(time_slots):
        curr_start_time = slot[0]
        curr_end_time = slot[1]
        new_slot = ()

        for next_slot in time_slots[index+1:]:

            new_start_time = None
            new_end_time = None
            # check if any time slot has an earlier start
            if next_slot[0] < curr_start_time:
                # Update new start time
                new_start_time = next_slot[0]

            # check if any time slot with start time less than curr end time
            if next_slot[0] < curr_end_time:
                # Update new end time
                new_end_time = next_slot[1]

            if (new_start_time == None and new_end_time == None) :
                new_slot = (curr_start_time, curr_end_time)
                         
        if len(new_slot) == 2 :
            condensed_slots.append(new_slot)
    return condensed_slots


def main():

    slots =   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    print(merge_changes(slots))

if __name__ == "__main__":
    main()