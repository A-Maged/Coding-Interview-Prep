def threeNumberSum(array, targetSum):
    array.sort()
    result = []

    for i in range(len(array) - 1):
        currentNum = array[i]
        # pointers
        left = i + 1
        right = len(array) - 1

        while left < right:
            currentSum = currentNum + array[left] + array[right]

            if currentSum == targetSum:
                result.append([currentNum, array[left], array[right]])

                # advance both pointers to keep searching for other matching pairs
                right -= 1
                left += 1
            elif currentSum > targetSum:
                right -= 1
            else:
                left += 1

    return result


if __name__ == "__main__":
    # result equals [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))

    # result equals [[1, 2, 3]]
    print(threeNumberSum([1, 2, 3], 6))
