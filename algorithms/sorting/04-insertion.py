def insertion_sort(arr):

    # using index=1 ,because we're assuming the first item is sorted (an array of one item is definitely sorted)
    for i in range(1, len(arr)):
        current = arr[i]
        write_index = i

        # keep shifting items until our item is bigger
        while write_index > 0 and current < arr[write_index - 1]:
            arr[write_index] = arr[write_index - 1]
            write_index -= 1

        # insert our item
        arr[write_index] = current

    return arr


if __name__ == "__main__":
    print(insertion_sort([]))
    print(insertion_sort([9, 3]))
    print(insertion_sort([3, 2, 9, 7, 1, 3, 0, 1]))
