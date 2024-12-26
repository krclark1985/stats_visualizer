import math_methods, pytest

odd_length_data_set = [1, 2, 3]
even_length_data_set = [1, 2, 3, 4]
negative_data_set = [-1, -2, -3]
non_numeric_data_set = ['a', 'b', 'c']
empty_data_set = []

@pytest.mark.parametrize("input_data_set, expected_mean", 
                         [(odd_length_data_set, 2),
                          (even_length_data_set, 2.5),
                          (negative_data_set, -2),
                          (non_numeric_data_set, "data set contains non-numeric values; please input numeric values only"),
                          (empty_data_set, "data set contains no values; please input numeric values")])

def test_mean_parametrized(input_data_set, expected_mean):
    assert math_methods.mean(input_data_set) == expected_mean

