def recursive_search(arr, target, start=0):
    if start >= len(arr):
        return -1  # Not found
    if arr[start] == target:
        return start  # Found the target
    return recursive_search(arr, target, start + 1)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    target = int(input("Enter a number to search for: "))
    index = recursive_search(numbers, target)
    
    if index != -1:
        print(f"Number found at index {index}")
    else:
        print("Number not found")

