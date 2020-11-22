# brute force - O(n^2)

# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]

#         for j in range(i + 1, len(array)):
#             secondNum = array[j]

#             if firstNum + secondNum == targetSum:
#                 return [firstNum, secondNum]

#     return []


# O(n) time | O(n) space
# def twoNumberSum(array, targetSum):
#     comps = {}

#     for num in array:
#         # complement(-1) = targetSum(10) - currentNum(11)
#         complement = targetSum - num

#         if complement in comps:
#             return [complement, num]
#         else:
#             # complement(-1) = targetSum(10) - currentNum(11)
#             # store "num", because next time we'll encounter the current "complement", but it will be treated as a currentNum
#             comps[num] = True

#     return []

# O(nLog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        comp = array[left] + array[right]

        if comp == targetSum:
            return [array[left], array[right]]
        elif comp < targetSum:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    print(twoNumberSum([-1, 3, 11, 5, -4, 8, 1, 6], 10))
