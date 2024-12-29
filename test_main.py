import main, pytest

# these data sets represent various iterations of numerical
# data sets that might be received as input
zeroes_data_set = [0, 0]
odd_length_data_set = [1, 2, 3]
even_length_data_set = [1, 2, 3, 4]
negative_data_set = [-3, -2, -1]
larger_data_set = [-8, -8, -2, -1, 1, 1, 8, 8, 9, 10]
mult_values_data_set = [0.2, 0.2, 0.22, 0.22, 0.22, 3, 3, 3]
outliers_data_set = [5, 98, 101, 101, 101, 102, 103, 103, 396]
letter_data_set = ['a', 'b', 'c', 'd']
mixed_data_set = [1, 'x', 'y', 54, 'z']
empty_data_set = []
one_value_data_set = [2]

@pytest.mark.parametrize("input_data_set, expected_validation", 
                         [(zeroes_data_set, True),
                          (odd_length_data_set, True),
                          (even_length_data_set, True),
                          (negative_data_set, True),
                          (larger_data_set, True),
                          (mult_values_data_set, True),
                          (outliers_data_set, True),
                          (letter_data_set, False),
                          (mixed_data_set, False),
                          (empty_data_set, False),
                          (one_value_data_set, False)])
def test_valid_input_check(input_data_set, expected_validation):
    assert main.valid_input_check(input_data_set) == expected_validation

default_dict = {'min': 0.0, 'q1': 0.0, 'median': 0.0, 'q3': 0.0, 'max': 0.0, 
                'range': 0.0, 'iqr': 0.0, 'mean': 0.0, 'mode': [], 'outliers': []}
zeroes_data_set_dict = {"data_input": [0, 0]}
zeroes_solution_dict = {'min': 0.0, 'q1': 0.0, 'median': 0.0, 'q3': 0.0, 'max': 0.0, 
                'range': 0.0, 'iqr': 0.0, 'mean': 0.0, 'mode': [0], 'outliers': []}
odd_data_set_dict = {"data_input": [1, 2, 3]}
odd_solution_dict = {'min': 1, 'q1': 1, 'median': 2, 'q3': 3, 'max': 3, 
                'range': 2, 'iqr': 2, 'mean': 2, 'mode': None, 'outliers': []}

@pytest.mark.parametrize("input_data_set, expected_stats_dict", 
                         [(zeroes_data_set_dict, zeroes_solution_dict),
                          (odd_data_set_dict, odd_solution_dict)])
                          # (even_length_data_set, True),
                          # (negative_data_set, True),
                          # (larger_data_set, True),
                          # (mult_values_data_set, True),
                          # (outliers_data_set, True),
                          # (letter_data_set, False),
                          # (mixed_data_set, False),
                          # (empty_data_set, False),
                          # (one_value_data_set, False)])
def test_calculate_stats(input_data_set, expected_stats_dict):
    assert main.calculate_stats(input_data_set) == expected_stats_dict
