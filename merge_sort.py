
def sortPartialLists(number_list):
    aux = 0

    for i in range(0, len(number_list)):
        for j in range(i+1, len(number_list)):
            if (number_list[i] > number_list[j]):
                aux = number_list[i]
                number_list[i] = number_list[j]
                number_list[j] = aux
    
    return number_list


def sortAllLists(left_number_list, 
                 right_number_list, 
                 number_list_length):
    number_list = []
    left_position = 0
    right_position = 0
    position = 0 

    while position < number_list_length:
        if left_position >= len(left_number_list):
            number_list.append(right_number_list[right_position])
            right_position += 1
        elif right_position >= len(right_number_list):
            number_list.append(left_number_list[left_position])
            left_position += 1
        elif (left_number_list[left_position] > right_number_list[right_position]):
            number_list.append(right_number_list[right_position])
            right_position += 1
        else:
            number_list.append(left_number_list[left_position])
            left_position += 1
        position += 1

    return number_list


def mergeSort(number_list):
    number_list_length = len(number_list)
    number_list_middle = number_list_length/2
    left_number_list = number_list[0:number_list_middle]
    right_number_list = number_list[number_list_middle:number_list_length]

    left_number_list = sortPartialLists(left_number_list)
    right_number_list = sortPartialLists(right_number_list)
    final_list = sortAllLists(left_number_list,
                              right_number_list,
                              number_list_length)

    return final_list

number_list = [1, 5, 4, 8, 10, 2, 6, 9, 12, 11, 3, 7]
final_list = mergeSort(number_list)

print(final_list)