# def binary_search(arr, target):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         mid=(left+right)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1
# numbers = [10, 20, 30, 40, 50, 60, 70]



# print(binary_search(numbers, 60))
# print(binary_search(numbers, 100))


# //linear Search

# def find_number(number,target):
#     for i in range(len(number)):
#         if number[i]==target:
#             print("Number found at index:",i)
#             return
#     return -1


# arr=[10, 20, 30, 40, 50, 60, 70]
# target=42
# find_number(arr,target)

# def find_number(number,target):
#     left=0
#     right=len(number)-1
#     while left<=right:
#         mid=(left+right)//2
#         if number[mid]==target:
#             print("Number found at index:",mid)
#             return
#         elif number[mid]<target:
#             left=mid+1
#         else:
#             right=mid-1
#     print("Number not found")
#     return -1

# arr=[10, 20, 30, 40, 50, 60, 70]
# target=43
# find_number(arr,target)

# numbers = [10, 20, 30, 40, 50, 60, 70]
# target = 603

# left=0
# right=len(numbers)-1
# while left<right:
#     sum=numbers[left]+numbers[right]
#     if sum==target:
#         print("got it")
#         break
#     elif sum<target:
#         left=left+1
#     else:
#         right=right-1

# numbers = [3, 8, 12, 17, 25, 31, 42, 56]
# left=0
# right=len(numbers)-1
# target=int(input("Do you want to search for a number? "))
# while left<=right:
#     mid=(left+right)//2
#     if numbers[mid]==target:
#         print("Number found at index:",mid)
#         break
#     elif numbers[mid]<target:
#         left=mid+1
#     else:
#         right=mid-1








