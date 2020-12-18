# ps: array contains only positive integers

def canSumDp(target, nums):
    smallestNum = min(nums)
    memo = {}

    return _canSumDp(target, nums, memo, smallestNum)


def _canSumDp(target, nums, memo, smallestNum):
    if target in memo:  # cached
        return memo[target]

    # target must be atleast bigger than one number(the smallest)
    # because subtracting nums-in-array from target should ultimately lead to zero(that's how we know there's a pair the canSum to target)
    if target < smallestNum:
        return False

    if target == 0:
        return True

    for num in nums:
        difference = target - num

        memo[target] = _canSumDp(
            difference, nums, memo, smallestNum)  # memoize

        if memo[target]:
            return True

    memo[target] = False

    return memo[target]


def canSum(target, nums):
    nums.sort()

    left = 0
    right = len(nums) - 1

    while right > left:
        sum_ = nums[right] + nums[left]

        if sum_ == target:
            # return nums[left], nums[right]
            return True
        elif(sum_ > target):
            right -= 1
        elif(sum_ < target):
            left += 1

    return False


if __name__ == "__main__":
    print(canSum(7, [5, 4, 3, 7]))  # True
    print(canSumDp(7, [5, 4, 3, 7]))  # True

    print(canSum(0, [5, 4, 3, 7]))  # False
    print(canSumDp(0, [5, 4, 3, 7]))  # False

    print(canSum(300, [7, 14]))  # False
    print(canSumDp(300, [7, 14]))  # False
