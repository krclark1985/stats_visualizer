import math_methods, pytest

# would be violating DRY principle to repeatedly check for
# empty data set or non-numeric data set; this check should
# be done in main.py (and then tested there, too!)

odd_length_data_set = [1, 2, 3]
even_length_data_set = [1, 2, 3, 4]
negative_data_set = [-1, -2, -3]
larger_data_set = [-8, -8, -2, -1, 1, 1, 8, 8, 9, 10]
mult_values_data_set = [0.2, 0.2, 0.22, 0.22, 0.22, 3, 3, 3]
# non_numeric_data_set = ['a', 'b', 'c']
# empty_data_set = []

@pytest.mark.parametrize("input_data_set, expected_mean", 
                         [(odd_length_data_set, 2),
                          (even_length_data_set, 2.5),
                          (negative_data_set, -2),
                          (larger_data_set, 1.8),
                          (mult_values_data_set, 1.2575)])
                          # (non_numeric_data_set, "data set contains non-numeric values; please input numeric values only"),
                          # (empty_data_set, "data set contains no values; please input numeric values")])

def test_mean(input_data_set, expected_mean):
    assert math_methods.mean(input_data_set) == expected_mean


@pytest.mark.parametrize("input_data_set, expected_median", 
                         [(odd_length_data_set, 2),
                          (even_length_data_set, 2.5),
                          (negative_data_set, -2),
                          (larger_data_set, 1),
                          (mult_values_data_set, 0.22)])
def test_median(input_data_set, expected_median):
    assert math_methods.median(input_data_set) == expected_median


@pytest.mark.parametrize("input_data_set, expected_mode", 
                         [(odd_length_data_set, None),
                          (even_length_data_set, None),
                          (negative_data_set, None),
                          (larger_data_set, [-8, 1, 8]),
                          (mult_values_data_set, [0.22, 3])])
def test_mode(input_data_set, expected_mode):
    assert math_methods.mode(input_data_set) == expected_mode

