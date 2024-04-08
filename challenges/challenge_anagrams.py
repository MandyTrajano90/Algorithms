def sort_method(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = sort_method(array[:mid])
    right = sort_method(array[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def is_anagram(first_string, second_string):
    lower_first = first_string.lower()
    lower_second = second_string.lower()
    first_sorted = "".join(sort_method(list(lower_first)))
    second_sorted = "".join(sort_method(list(lower_second)))

    anagram_exists = first_sorted == second_sorted
    if first_sorted == "" or second_sorted == "":
        anagram_exists = False

    return first_sorted, second_sorted, anagram_exists
