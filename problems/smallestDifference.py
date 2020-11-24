# def smallestDifference(arrayOne, arrayTwo):
#     minDistance = float('inf')
#     last_pair = None

#     for i in range(len(arrayOne)):
#         for j in range(len(arrayTwo)):
#             if arrayOne[i] > 0 and arrayTwo[j] > 0 or arrayOne[i] < 0 and arrayTwo[j] < 0:
#                 currentDistance = abs(abs(arrayOne[i]) - abs(arrayTwo[j]))
#             else:
#                 currentDistance = abs(abs(arrayOne[i]) + abs(arrayTwo[j]))

#             if currentDistance < minDistance:
#                 minDistance = currentDistance
#                 last_pair = [arrayOne[i], arrayTwo[j]]

#     return last_pair

# smallestDifference means closest numbers
# that's why we're itrating sorted arrays  trying to find closest numbers to each other
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    minDistance = float('inf')
    pair = None
    i = 0
    j = 0

    while i < len(arrayOne) and j < len(arrayTwo):
        currentDistance = abs(abs(arrayOne[i]) - abs(arrayTwo[j]))

        if currentDistance < minDistance:
            minDistance = currentDistance
            pair = [arrayOne[i], arrayTwo[j]]

        if arrayOne[i] == arrayTwo[j]:
            return [arrayOne[i], arrayTwo[j]]
        elif arrayOne[i] < arrayTwo[j]:
            i += 1  # advance pointer
        else:
            j += 1

    return pair


if __name__ == "__main__":
    # print(smallestDifference([-1, 5, 10, 20, 28, 3],
    #                          [26, 134, 135, 15, 17]))  # [28, 26]

    print(smallestDifference([-1, 5, 10, 20, 3],
                             [26, 134, 135, 15, 17]))  # [20, 17]

    print(smallestDifference([-1, 0, 3, 6, 7],
                             [2, 7, 9, 14]))  # [7,7]
