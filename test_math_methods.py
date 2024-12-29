import math_methods, pytest

# these data sets represent various iterations of numerical
# data sets that might be received as input
zeroes_data_set = [0, 0]
odd_length_data_set = [1, 2, 3]
even_length_data_set = [1, 2, 3, 4]
negative_data_set = [-3, -2, -1]
larger_data_set = [-8, -8, -2, -1, 1, 1, 8, 8, 9, 10]
mult_values_data_set = [0.2, 0.2, 0.22, 0.22, 0.22, 3, 3, 3]
outliers_data_set = [5, 98, 101, 101, 101, 102, 103, 103, 396]

@pytest.mark.parametrize("input_data_set, expected_mean", 
                         [(zeroes_data_set, 0),
                          (odd_length_data_set, 2),
                          (even_length_data_set, 2.5),
                          (negative_data_set, -2),
                          (larger_data_set, 1.8),
                          (mult_values_data_set, 1.2575),
                          (outliers_data_set, 1110 / 9)])
def test_mean(input_data_set, expected_mean):
    assert math_methods.mean(input_data_set) == expected_mean


@pytest.mark.parametrize("input_data_set, expected_median", 
                         [(zeroes_data_set, 0),
                          (odd_length_data_set, 2),
                          (even_length_data_set, 2.5),
                          (negative_data_set, -2),
                          (larger_data_set, 1),
                          (mult_values_data_set, 0.22),
                          (outliers_data_set, 101)])
def test_median(input_data_set, expected_median):
    assert math_methods.median(input_data_set) == expected_median


@pytest.mark.parametrize("input_data_set, expected_mode", 
                         [(zeroes_data_set, [0]),
                          (odd_length_data_set, None),
                          (even_length_data_set, None),
                          (negative_data_set, None),
                          (larger_data_set, [-8, 1, 8]),
                          (mult_values_data_set, [0.22, 3]),
                          (outliers_data_set, [101])])
def test_mode(input_data_set, expected_mode):
    assert math_methods.mode(input_data_set) == expected_mode


@pytest.mark.parametrize("input_data_set, expected_five_num_summary", 
                         [(zeroes_data_set, {'min': 0, 'q1': 0, 'median': 0, 'q3': 0, 'max': 0}),
                          (odd_length_data_set, {'min': 1, 'q1': 1, 'median': 2, 'q3': 3, 'max': 3}),
                          (even_length_data_set, {'min': 1, 'q1': 1.5, 'median': 2.5, 'q3': 3.5, 'max': 4}),
                          (negative_data_set, {'min': -3, 'q1': -3, 'median': -2, 'q3': -1, 'max': -1}),
                          (larger_data_set, {'min': -8, 'q1': -2, 'median': 1, 'q3': 8, 'max': 10}),
                          (mult_values_data_set, {'min': 0.2, 'q1': (0.22 + 0.2) / 2, 'median': 0.22, 'q3': 3, 'max': 3}),
                          (outliers_data_set, {'min': 5, 'q1': 99.5, 'median': 101, 'q3': 103, 'max': 396})])
def test_five_num_summary(input_data_set, expected_five_num_summary):
    assert math_methods.five_num_summary_dict(input_data_set) == expected_five_num_summary


@pytest.mark.parametrize("input_data_set, expected_outliers", 
                         [(zeroes_data_set, []),
                          (odd_length_data_set, []),
                          (even_length_data_set, []),
                          (negative_data_set, []),
                          (larger_data_set, []),
                          (mult_values_data_set, []),
                          (outliers_data_set, [5, 396])])
def test_outliers(input_data_set, expected_outliers):
    assert math_methods.outliers(input_data_set) == expected_outliers

