def move_zeros(nums):
    start = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            temp = nums[start]
            nums[start]=nums[i]
            nums[i]= temp
        
            start+=1

    return nums

list = [1,0,0,2,3,0]

a = move_zeros(list)

print(a)