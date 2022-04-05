from binary_chop import basic_chop


def assert_equal(true_value, returned_value):
    assert true_value == returned_value


def test_basic_chop():
    assert_equal(-1, basic_chop(3, []))
    assert_equal(-1, basic_chop(3, [1]))
    assert_equal(0, basic_chop(1, [1]))
    #
    assert_equal(0, basic_chop(1, [1, 3, 5]))
    assert_equal(1, basic_chop(3, [1, 3, 5]))
    assert_equal(2, basic_chop(5, [1, 3, 5]))
    assert_equal(-1, basic_chop(0, [1, 3, 5]))
    assert_equal(-1, basic_chop(2, [1, 3, 5]))
    assert_equal(-1, basic_chop(4, [1, 3, 5]))
    assert_equal(-1, basic_chop(6, [1, 3, 5]))
    #
    assert_equal(0, basic_chop(1, [1, 3, 5, 7]))
    assert_equal(1, basic_chop(3, [1, 3, 5, 7]))
    assert_equal(2, basic_chop(5, [1, 3, 5, 7]))
    assert_equal(3, basic_chop(7, [1, 3, 5, 7]))
    assert_equal(-1, basic_chop(0, [1, 3, 5, 7]))
    assert_equal(-1, basic_chop(2, [1, 3, 5, 7]))
    assert_equal(-1, basic_chop(4, [1, 3, 5, 7]))
    assert_equal(-1, basic_chop(6, [1, 3, 5, 7]))
    assert_equal(-1, basic_chop(8, [1, 3, 5, 7]))
