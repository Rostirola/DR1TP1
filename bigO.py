def greatestNumber(array):
    if not array:
        return None

    greatest = array[0]

    for i in array[1:]:
        if i > greatest:
            greatest = i

    return greatest
