def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    for i in range(stop - start + 1):
        counter = i + start
        print(counter)

    # while loop alternative below
    # while start <= stop:
    #     print(start)
    #     start = start + 1

    # # YOUR CODE HERE


count_up(5, 7)        
