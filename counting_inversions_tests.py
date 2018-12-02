
def countInversions(number_list):
    inversions = 0

    for i in range(0, len(number_list)):
        # print(number_list[i])
        for j in range(i + 1, len(number_list)):
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


print("ANTIGO")
number_list = [2747, 14283, 19122, 14335, 2726, 12439, 15521, 16482, 4815, 6924, 19]
total_inversions = mergeSortCountingInversions(number_list)

print(total_inversions)


def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:int(len(arr) / 2)]
        b = arr[int(len(arr) / 2):]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a) - i)
    c += a[i:]
    c += b[j:]

    return c, inversions


number_list2 = [2747, 14283, 19122, 14335, 2726, 12439, 15521, 16482, 4815, 6924, 19]
vetor, total_inversions2 = mergeSortInversions(number_list2)

print("NOVO")
print(vetor)
print(total_inversions2)
