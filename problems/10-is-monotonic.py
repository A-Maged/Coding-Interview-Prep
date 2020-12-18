# non-increasing: means it decreases or stays the same(has duplicate elements)
# non-decreasing: means it increases or stays the same(has duplicate elements)

def isMonotonic(array):
	isIncreasing = True
	isDecreasing = True
	
	for i in range(1, len(array)):
		if array[i] > array[i - 1]:
			isDecreasing = False
		if array[i] < array[i - 1]:
			isIncreasing = False
	
	return isIncreasing or isDecreasing

	
	
	
print(isMonotonic([1, 2, 0])) # False