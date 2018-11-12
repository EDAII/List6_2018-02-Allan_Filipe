
def countInversions(number_list):
    inversions = 0

    for i in range(0, len(number_list)):
        # print(number_list[i])
        for j in range(i+1, len(number_list)):
            # print(number_list[j])
            if (number_list[i] > number_list[j]):
                inversions += 1
    
    return inversions

def countMergedInversions(left_number_list, right_number_list):
    inversions = 0

    for i in range(0, len(left_number_list)):
        # print(number_list[i])
        for j in range(0, len(right_number_list)):
            # print(number_list[j])
            if (left_number_list[i] > right_number_list[j]):
                inversions += 1
    
    return inversions

def mergeSortCountingInversions(number_list):
    left_number_list = number_list[0:6]
    right_number_list = number_list[6:12]

    left_number_list_inversions = countInversions(left_number_list)
    right_number_list_inversions = countInversions(right_number_list)
    left_right_inversions = countMergedInversions(left_number_list, right_number_list)

    print(left_number_list_inversions)
    print(right_number_list_inversions)
    print(left_right_inversions)
     
    total_inversions = left_number_list_inversions + right_number_list_inversions + left_right_inversions

    return total_inversions

number_list = [1, 5, 4, 8, 10, 2, 6, 9, 12, 11, 3, 7]
total_inversions = mergeSortCountingInversions(number_list)

print(total_inversions)