
def find_min_max(numbers):
    if not numbers:
        return None, None

    min_num = max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return min_num, max_num


# Example usage
my_list = [5, 2, 9, 1, 7]
min_value, max_value = find_min_max(my_list)
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
