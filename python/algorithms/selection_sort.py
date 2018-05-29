def sort(elements):
    sorted_list = []

    current_higher_index = 0
    while len(elements) > 0:
        for i in range(0, len(elements)):
            if elements[current_higher_index] < elements[i]:
                current_higher_index = i
        sorted_list.insert(0, elements.pop(current_higher_index))
        current_higher_index = 0

    return sorted_list
