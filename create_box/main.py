def create_box(height, width, character):

    if height < 1 or width < 1:
        return None

    ret_val = ''
    for y in range(height):
        box_str = ''
        for x in range(width):
            box_str = box_str + str(character)

        ret_val = ret_val + box_str + '\n'

    return ret_val

def create_empty_box(height, width, character):
    ret_val = ''

    for y in range(height):
        box_str = ''

        for x in range(width):
            if x == 0 or x == (width - 1) \
            or y == 0 or y == (height -1) :
                box_str = box_str + character
            else:
                box_str = box_str + " "

        ret_val = ret_val + box_str + '\n'

    return ret_val

# Tests:
first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

empty_box_expected = """
$$$$$$$$
$      $
$      $
$$$$$$$$
""".lstrip()

def test_first_box():
    assert create_box(3, 4, '*') == first_box_expected


def test_second_box():
    assert create_box(1, 1, '@') == second_box_expected

# Write your own test using the `third_box_expected` box
def test_third_box():
    assert create_box(3, 25, 'x') == third_box_expected

def test_empty_box():
    assert create_empty_box(4, 8, '$') == empty_box_expected

#if __name__ == '__main__':
#    create_empty_box(4,8,'$')
