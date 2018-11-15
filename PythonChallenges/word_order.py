def histogram(list):
    dict_histogram = {}
    keys = []

    for word in list:
        if word not in dict_histogram:
            dict_histogram[word] = 1
        else:
            dict_histogram[word] += 1

    for key,value in dict_histogram.items():
        keys.append(value)

    print(unique_words(dict_histogram))
    print(' '.join(str(x) for x in keys))

def unique_words(histogram):
    return len(histogram)

def main():

    n = 4
    list = ["bcdef", "abcdefg", "bcde", "bcdef"]
    histogram(list)

if __name__ == "__main__":
    main()
