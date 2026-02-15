from calculator import square
import pytest


def test_positive():
    assert square(2) == 4

def test_negative():
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("a string")

# def main():
#     test_square()

# def test_square():
#     assert square(2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0


#simplified version of below code
    """
    try:
        assert square(2) == 4
    except AssertionError:
        print("Test failed: square(2) should be 4")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("Test failed: square(-3) should be 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("Test failed: square(0) should be 0")

    """
# comment the main function 
# if __name__ == "__main__":
#     main()