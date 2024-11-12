import random
import time
import matplotlib.pyplot as plt


def tim_sort(arr, k):
    if len(arr) <= k:
        insertion_sort(arr)
        return arr  # Return sorted array after insertion sort
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = tim_sort(arr[:mid], k)  # Sort left half
    rightHalf = tim_sort(arr[mid:], k)  # Sort right half

    return merge(leftHalf, rightHalf)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        insert_index = i
        current_value = arr.pop(i)
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value)



# Store elapsed times for each algorithm
insertion_sort_stored = []
merge_sort_stored = []
tim_sort_stored = []

# Initial size of the random list
x = 5
# Range of usable values
min_val = 1
max_val = 1000000
# Number of iterations for average case time
num_iterations = 1000
# The tim_sort benchmark number
benchmark = 50


checked_feature = False

while True:
    total_insertion_time = 0
    total_merge_time = 0
    total_tim_time = 0

    for a in range(num_iterations):
        random_list = [random.randint(min_val, max_val) for a in range(x)]

        # Insertion sort
        start_time_insertion = time.perf_counter()
        sorted_arr_insertion = insertion_sort(random_list)
        end_time_insertion = time.perf_counter()
        elapsed_time_insertion = end_time_insertion - start_time_insertion

        # Merge sort
        start_time_merge = time.perf_counter()
        sorted_arr_merge = merge_sort(random_list)
        end_time_merge = time.perf_counter()
        elapsed_time_merge = end_time_merge - start_time_merge

        # Tim sort
        start_time_tim = time.perf_counter()
        sorted_arr_tim = tim_sort(random_list, benchmark)
        end_time_tim = time.perf_counter()
        elapsed_time_tim = end_time_tim - start_time_tim

        # Accumulate the elapsed times
        total_insertion_time += elapsed_time_insertion
        total_merge_time += elapsed_time_merge
        total_tim_time += elapsed_time_tim

    # Calculate the average times
    average_insertion_time = total_insertion_time / num_iterations
    average_merge_time = total_merge_time / num_iterations
    average_tim_time = total_tim_time / num_iterations

    # Store the average times
    insertion_sort_stored.append(average_insertion_time)
    merge_sort_stored.append(average_merge_time)
    tim_sort_stored.append(average_tim_time)

    if average_insertion_time >= average_merge_time and checked_feature == False:
        print(f"First number Insertion Sorting Is Less Efficient: {x}")
        
        checked_feature = True

    elif x == 100:
        print(f"Average Insertion Sort Time: {average_insertion_time:.6f} seconds")
        print(f"Average Merge Sort Time: {average_merge_time:.6f} seconds")
        print(f"Average Tim Sort Time: {average_tim_time:.6f} seconds")
        break
    else:
        x += 1

# Plotting the results
plt.plot(range(1, len(insertion_sort_stored) + 1), insertion_sort_stored, label='Insertion Sort Average Time', color='blue')
plt.plot(range(1, len(merge_sort_stored) + 1), merge_sort_stored, label='Merge Sort Average Time', color='orange')
plt.plot(range(1, len(tim_sort_stored) + 1), tim_sort_stored, label='Tim Sort Average Time', color='green')
plt.xlabel('Size of List')
plt.ylabel('Elapsed Time (Seconds)')
plt.title('Average Comparison of Insertion Sort, Merge Sort, and Tim Sort Times')
plt.legend()
plt.grid(True)
plt.show()

