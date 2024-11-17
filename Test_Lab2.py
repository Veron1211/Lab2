import Lab2

def test_find_min_max():
    input_arr = [5, 7, 8, 9]
    expect_result = [5, 9]

    result = Lab2.find_min_max(input_arr)
    assert (result == expect_result)

def test_calc_average():
    input_arr = [5, 7, 8, 9]
    expect_result = 7.25

    result = Lab2.calc_average(input_arr)
    assert (result == expect_result)

def test_calc_median_temperature():
    input_arr = [5, 7, 8, 9]
    expect_result = 7.5

    result = Lab2.calc_median_temperature(input_arr)
    assert (result == expect_result)