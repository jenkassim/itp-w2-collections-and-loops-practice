#prime numbers can not be divided by any number besides its own
def _is_prime(number):

    prime_val = True
    if number < 2:
        prime_val = False
        print("#%s: %s" % (number,prime_val))
        return prime_val

    for idx in range(2, number):
        remainder = number % idx

        #non-prime number
        if remainder == 0:
            prime_val = False
            break

    print("#%s: %s" % (number,prime_val))
    return prime_val

def list_of_prime_numbers(max_number):
    list = []
    for x in range(max_number+1):
        if _is_prime(x):
            list.append(x)
    return list

# =================== #
# ====== Tests ====== #
# =================== #

# Test: `is_prime`


def test_big_number_prime_true():
    assert _is_prime(19) is True


def test_big_number_prime_false():
    assert _is_prime(20) is False


def test_two_prime():
    assert _is_prime(2) is True

def test_three_prime():
    assert _is_prime(3) is True


def test_four_prime():
    assert _is_prime(4) is False

def test_one_prime():
    assert _is_prime(1) is False


# Test: `list_of_prime_numbers`

def test_big_number_list():
    assert list_of_prime_numbers(19) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_list_one():
    assert list_of_prime_numbers(2) == [2]


def test_list_zero():
    assert list_of_prime_numbers(0) == []


#if __name__ == '__main__' :
    #list_of_prime_numbers(19)
