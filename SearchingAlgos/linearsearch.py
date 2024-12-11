def linearSearch(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1


if __name__ == "__main__":
    arr = list(map(int,input("\nEnter the array : ").split()))
    val = int(input("Enter the value to search in the array : "))
    index = linearSearch(arr,val)
    if index != -1:
        print(f"\n{val} found in the array {arr} at the index {index}\n")
    else:
        print(f"\n{val} can not be found in the array {arr}\n")
    