def isValidSubsequence(array, sequence):
    count = 0

    for i in range(len(array)):

        if array[i] == sequence[count]:
            count += 1

        if count == len(sequence):
            return True

    return False


if __name__ == "__main__":
    # result equals [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
