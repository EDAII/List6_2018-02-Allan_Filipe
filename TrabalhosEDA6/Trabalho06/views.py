from django.shortcuts import render
import time


def home(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.POST['selectedOption']:
        myfile = request.FILES['myfile']
        byte_str = myfile.file.read()
        # Convert to a "unicode" object
        text_obj = byte_str.decode('UTF-8')

        columns_descriptions, all_data = read_csv(text_obj.splitlines())

        # Choosing algorithm options
        if request.POST['selectedOption'] == "Merge Sort Recursivo":
            time_initial = time.time()
            sorted_data = mergeSort(all_data)
            time_final = time.time() - time_initial

            return render(request, 'result.html', {'algorithm': request.POST['selectedOption'],
                                                   'columns_descriptions': columns_descriptions,
                                                   'sorted_data': sorted_data,
                                                   'merge_sort_time': time_final})

        elif request.POST['selectedOption'] == "Contador de Inversões + Merge Sort":
            time_initial = time.time()
            sorted_data, inversions = mergeSortInversions(all_data)
            time_final = time.time() - time_initial

            return render(request, 'result.html', {'algorithm': request.POST['selectedOption'],
                                                   'columns_descriptions': columns_descriptions,
                                                   'all_data': all_data,
                                                   'inversions': inversions,
                                                   'count_inversion_time': time_final})

        else:
            # Nothing to do
            pass
    else:
        # Nothing to do
        pass

    return render(request, 'home.html')


def read_csv(file):
    all_data = []
    columns_descriptions = []

    # Save all csv data in a list of lists, removing '\n' at the last line element.
    for line in file:
        if not columns_descriptions:
            columns_descriptions = line.split(",")
            columns_descriptions[-1] = columns_descriptions[-1].strip("\n")
        else:
            line_splitted = line.split(",")
            line_splitted[-1] = line_splitted[-1].strip("\n")
            all_data.append(line_splitted)

    return columns_descriptions, all_data


# Conquer function
def sortList(data_list):
    aux = 0

    for i in range(0, len(data_list)):
        for j in range(i + 1, len(data_list)):
            if (int(data_list[i][0]) > int(data_list[j][0])):
                aux = data_list[i]
                data_list[i] = data_list[j]
                data_list[j] = aux

    return data_list


# Merge function
def mergeLists(left_data_list, right_data_list, data_list_length):
    data_list = []
    left_position = 0
    right_position = 0
    position = 0

    while position < data_list_length:
        if left_position >= len(left_data_list):
            data_list.append(right_data_list[right_position])
            right_position += 1
        elif right_position >= len(right_data_list):
            data_list.append(left_data_list[left_position])
            left_position += 1
        elif (int(left_data_list[left_position][0]) > int(right_data_list[right_position][0])):
            data_list.append(right_data_list[right_position])
            right_position += 1
        else:
            data_list.append(left_data_list[left_position])
            left_position += 1
        position += 1

    return data_list


# Divide function
def mergeSort(dataset):
    data_list = list(dataset)
    data_list_length = len(data_list)

    if data_list_length >= 3:
        data_list_middle = int(data_list_length / 2)
        left_data_list = data_list[0:data_list_middle]
        right_data_list = data_list[data_list_middle:data_list_length]

        left_data_list = mergeSort(left_data_list)
        right_data_list = mergeSort(right_data_list)
    elif data_list_length < 3:
        data_list = sortList(data_list)
        return data_list

    final_list = mergeLists(left_data_list,
                            right_data_list,
                            data_list_length)

    return final_list


# Count Inversions + Merge Sort
def mergeSortInversions(dataset):
    data_list = list(dataset)

    if len(data_list) == 1:
        return data_list, 0

    else:
        left_data_list = data_list[:int(len(data_list) / 2)]
        right_data_list = data_list[int(len(data_list) / 2):]

        left_data_list, left_inversions = mergeSortInversions(left_data_list)
        right_data_list, right_inversions = mergeSortInversions(right_data_list)

        sorted_data = []
        left_iterator = 0
        right_iterator = 0
        inversions = 0 + left_inversions + right_inversions

    while left_iterator < len(left_data_list) and right_iterator < len(right_data_list):
        if int(left_data_list[left_iterator][0]) <= int(right_data_list[right_iterator][0]):
            sorted_data.append(left_data_list[left_iterator])
            left_iterator += 1

        else:
            sorted_data.append(right_data_list[right_iterator])
            right_iterator += 1
            inversions += (len(left_data_list) - left_iterator)

    sorted_data += left_data_list[left_iterator:]
    sorted_data += right_data_list[right_iterator:]

    return sorted_data, inversions
