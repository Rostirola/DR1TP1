import math

def find_square(grains):
    if grains < 1:
        return None

    square = math.ceil(math.log2(grains + 1))
    return square
