def linear_search(arr, target):
    #Performs linear search on the given list to find the target element
    #Returns the index of the target element if found, else returns -1
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1
# Example usage
arr = [2, 5, 1, 8, 3, 7, 4]
target = 4 #shows the index of target in the arugment (list)
index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found")