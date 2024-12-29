import main

test_set = {"data_input": [1, 2, 3, 'y', 5]}
print(main.calculate_stats(test_set))

'''
import requests

url = "http://127.0.0.1:8000/calculate-stats/"
data = {"data_input": [1, 2, 3, 4, 5]}

response = requests.post(url, json=data)

print(response.json())


def non_numeric_check(input_data_set):
    for data in input_data_set:
        if not isinstance(data, (int, float, complex)):
            print ("data set contains non-numeric values; please input numeric values only")
            return False
    print("test passed")
    return True

test_set = [1, 2, 3, 4]
letter_test = [1, 2, 'a']
one_negative_test = [-1, 2, 3]
decimal_test = [0.3, 4, 5]
fraction_test = [1/2, 17, 80]

non_numeric_check(test_set)
non_numeric_check(letter_test)
non_numeric_check(one_negative_test)
non_numeric_check(decimal_test)
non_numeric_check(fraction_test)
'''
