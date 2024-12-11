def binarySearch(arr, val):
    l = 0
    r = len(arr)-1

    while l <= r:
        m = l + ((r - l) // 2)
        if arr[m] == val:
            return m
        elif val < arr[m]:
            r = m - 1
        else:
            l = m + 1
    return -1




if __name__ == "__main__":
    arr = list(map(int,input("\nEnter the array : ").split()))
    val = int(input("Enter the value to search in the array : "))
    index = binarySearch(arr,val)
    print(index)
    if index != -1:
        print(f"\n{val} found in the array {arr} at the index {index}\n")
    else:
        print(f"\n{val} can not be found in the array {arr}\n")
    