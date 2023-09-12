n=int(input("enter the number of elements:"))
arr=[]
for i in range(n):
    ele=int(input("enter the elements:"))
    arr.append(ele)
mini=arr[0]
maxi=arr[0]
for i in range(len(arr)):
    if arr[i] < mini:
        mini=arr[i]
    if arr[i] > maxi:
        maxi=arr[i]
print("smallest element:",mini)
print("largest element:",maxi)