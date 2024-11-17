# sholuld I make this all a class? Do some research.
# also, when creating the basic API with the one
# super-route that calls all methods and returns a
# dict of them, consider sorting up front before
# median and iqr method calls, or just up front in general

# returns the range of a given data set:
# named set_range because of built-in range function;
# alternatively, if input data_set is already sorted,
# min == data_set[0] & max == data_set[-1]
def set_range(data_set):
    """
    :type data_set: list of ints or floats
    :rtype: float
    """
    min_value = min(data_set)
    max_value = max(data_set)
    return float((max_value - min_value))

# returns the mean of a given data set
def mean(data_set):
    """
    :type data_set: list of ints or floats
    :rtype: float
    """
    data_sum = sum(data_set)
    n = len(data_set)
    return (data_sum / n)

# returns the median of a given data set;
# consider rounding this and the mean's float?
def median(data_set):
    """
    :type data_set: list of ints or floats
    :rtype: float
    """
    if len(data_set) % 2 != 0:
        return data_set[len(data_set) // 2]
    else:
        right_center = len(data_set) // 2
        left_center = right_center - 1
        return (data_set[left_center] + data_set[right_center]) / 2
    
# returns the mode, if any, of a given data set;
# if there is no mode, returns None
def mode(data_set):
    """
    :type data_set: list of ints or floats
    :rtype: int, float or None
    """
    multiples_tracker = [1] * len(data_set)
    highest_frequency = 1
    solution_list = []

    for i in range(len(data_set)):
        count_current_idx = data_set.count(data_set[i])
        if count_current_idx >= highest_frequency:
            highest_frequency = count_current_idx
            multiples_tracker[i] = count_current_idx

    if highest_frequency == 1:
        return None
    else:
        for i in range(len(multiples_tracker)):
            if multiples_tracker[i] == highest_frequency and solution_list.count(data_set[i]) == 0:
                solution_list.append(data_set[i])
        return solution_list
    

# returns a dictionary containing the minimum value ('min'),
# 1st quartile ('q1'), 2nd quartile/median ('median'), 3rd quartile ('q3'),
# and the maximum value ('max') of a given data set
def five_num_summary_dict(data_set):
    """
    :type data_set: list of ints or floats
    :rtype: dictionary of ints or floats
    """

    # for n = odd, find median index, then find
    # median of left half (q1) & right half (q3),
    # then return five number summary dictionary
    if len(data_set) % 2 != 0:
        median_idx = len(data_set) // 2
        left_half = data_set[0 : median_idx]
        right_half = data_set[(median_idx + 1):]
        q1 = median(left_half)
        q3 = median(right_half)
        five_num_summary_dict = {'min': data_set[0], 'q1': q1, 'median': median(data_set), 'q3': q3, 'max': data_set[-1]}
        return five_num_summary_dict
    
    # for n = even, split set into left_half & right_half
    # using len(data_set) // 2 index, then find median of
    # each half [q1(left) & q3(right)] and return 5 num sum dict
    else:
        left_half = data_set[:(len(data_set) // 2)]
        right_half = data_set[(len(data_set) // 2):]
        q1 = median(left_half)
        q3 = median(right_half)
        five_num_summary_dict = {'min': data_set[0], 'q1': q1, 'median': median(data_set), 'q3': q3, 'max': data_set[-1]}
        return five_num_summary_dict

# returns outliers (if any) in the data set; outliers
# identified if < q1 - (1.5 * iqr) or > q3 + (1.5 * iqr)
def outliers(data_set):
    """
    :type data_set: list of ints or floats
    :rtype: list of ints or floats or None
    """
    q1 = five_num_summary_dict(data_set)['q1']
    q3 = five_num_summary_dict(data_set)['q3']
    iqr = q3 - q1
    small_outlier_max = q1 - (1.5 * iqr)
    large_outlier_min = q3 + (1.5 * iqr)
    outliers = []

    for value in data_set:
        if value < small_outlier_max or value > large_outlier_min:
            outliers.append(value)
    if len(outliers) == 0:
        outliers.append(None)
    return outliers

'''
# test_set = [5, 7, 10, 15, 19, 21, 21, 22, 22, 23, 23, 23, 23, 23, 24, 24, 24, 24, 25]
test_set = [25.5, 25.5, 26.5, 28.5, 29, 30.5, 31.5, 31.5, 32, 32.5]
# test_set = [1, 2, 3, 4, 5, 6]
print('range =', set_range(test_set))
print('mean =', mean(test_set))
print('median =', median(test_set))
print('mode =', mode(test_set))
print('five number summary =', five_num_summary_dict(test_set))
print('outliers =', outliers(test_set))
'''