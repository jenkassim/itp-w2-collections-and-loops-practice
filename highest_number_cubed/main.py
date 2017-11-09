def highest_number_cubed(limit):

    highNum = 0
    for val in range(limit):
        cube = val**3

        if cube > limit:
            highNum = val
            break

    return highNum-1

def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22

#if __name__ == '__main__':
#    highest_number_cubed(30)
