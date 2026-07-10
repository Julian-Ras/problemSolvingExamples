"""
This function takes an array of numbers that contains zeros and moves all zeros to the
end of the array while keeping the relative order of the non zero elements the same
"""
def moveZeros(nums):
    lastPos = 0
    for current in range(len(nums)):
        if nums[current] != 0:
            temp = nums[current]
            nums[current] = nums[lastPos]
            nums[lastPos] = temp
            lastPos += 1
    return nums

print(moveZeros([0,1,0,3,12]))