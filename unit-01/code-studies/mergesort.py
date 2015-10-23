def merge(list_a, list_b, comparator, accumulator=None):
    if accumulator is None:
        accumulator = []

    if len(list_a) == 0:
        return accumulator + list_b

    if len(list_b) == 0:
        return accumulator + list_a

    if comparator(list_a[0], list_b[0]):
        accumulator.append(list_a[0])
        return merge(list_a[1:], list_b, comparator, accumulator)

    else:
        accumulator.append(list_b[0])
        return merge(list_a, list_b[1:], comparator, accumulator)


def sort(unsorted_list, comparator=lambda x, y: x < y):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle_index = len(unsorted_list) / 2
    list_a = sort(unsorted_list[:middle_index], comparator)
    list_b = sort(unsorted_list[middle_index:], comparator)
    return merge(list_a, list_b, comparator)
