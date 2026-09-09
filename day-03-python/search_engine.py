numbers=[5, 10, 15, 20, 25, 30, 35, 40  ]
target=int(input("Enter the number you want to search: "))
left=0
right=len(numbers)-1
while left<=right:
    mid=(left+right)//2
    if numbers[mid]==target:
        print("Number found at index:",mid)
        break
    elif numbers[mid]<target:
        left=mid+1
    else:
        right=mid-1