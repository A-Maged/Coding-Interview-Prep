# book solution
# def dedub(array):
#     if not array:
#         return 0

#     write_index = 1

#     for i in range(1, len(array)):
#         if array[write_index - 1] != array[i]:
#             array[write_index] = array[i]
#             write_index += 1

#     return write_index


def dedub(array):
    if not array:
        return 0

    write_index = 0

    for i in range(1, len(array)):
        if array[i] != array[i - 1]:  # ignore repeated elements
            write_index += 1
            array[write_index] = array[i]

    return write_index + 1  # add one to change index into length


if __name__ == "__main__":
    print(dedub([2, 3, 5, 5, 11, 11, 13]))
    print(dedub([2, 3, 5, 11, 13]))
