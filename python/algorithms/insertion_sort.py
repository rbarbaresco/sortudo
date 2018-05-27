def sort(elements):
    sorted_list = list(elements)
    for i in range(1, len(sorted_list)):
        current_element = sorted_list[i]
        position = i

        while position > 0 and sorted_list[position - 1] > current_element:
            sorted_list[position] = sorted_list[position - 1]
            position -= 1

            sorted_list[position] = current_element
    return sorted_list
