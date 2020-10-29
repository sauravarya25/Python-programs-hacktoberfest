def pairsum(arr, size, n):
    pair=set()
    for i in range(0, len(arr)):
        temp=n-arr[i]
        if (temp in pair):
            print(" Pair of given sum is", arr[i], "and", temp)
        pair.add(arr[i])
print("Enter elements in array in sorted order: ")
arr=list(map(int, input().split()))
print("Enter the value of n:")
n=int(input())
pairsum(arr, len(arr), n)
