def kSmallest(arr, k):
arr.sort(reverse=False)
for i in range(k):
   print (arr[i],end=" ") 
arr = [1, 23, 12, 9, 30, 2, 50]
k = int(input(""))
kSmallest(arr, k)
