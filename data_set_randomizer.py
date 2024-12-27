import random

def create_random_data_set(n, min, max):
    new_data_set = []
    for i in range(n):
        random_value = random.randint(min, max)
        new_data_set.append(random_value)
    print(new_data_set)
    new_data_set.sort()
    return new_data_set

print(create_random_data_set(10, -10, 10))