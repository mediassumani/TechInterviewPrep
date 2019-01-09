# O(n)^2
def sort_athlete(N, M, nested_arr, k):

    sorted_atheltes = []
    current_lowest_attribute = nested_arr[0][k]
    kth_elements = sorted([arr[k] for arr in nested_arr])

    for attribute in kth_elements:
        for index, athlete in enumerate(nested_arr):
            current_athlete = athlete
            if attribute == current_athlete[k]:
                sorted_atheltes.append(current_athlete)

    print(sorted_atheltes)

def main():

    arr = [
        [10, 2, 5],
        [7,1,0],
        [9,9,9],
        [1,23,12],
        [6,5,9]
    ]

    number_of_atheletes = len(arr)
    number_of_attributes = 3
    k = 1

    sort_athlete(number_of_atheletes, number_of_attributes, arr,k)


if __name__ == "__main__":
    main()
