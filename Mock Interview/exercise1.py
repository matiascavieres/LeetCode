# Given the array nums consisting of 2n elements in the form
# [x1,x2,...,xn,y1,y2,...,yn]
# Return the array in the form [x1,y1,x2,y2...,xn,yn]

# Example1: 
# Input: nums = [2,5,1,3,4,7], n = 3

# Constraints
# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10^3


# Tasks:
# Declare our variables
    # ArrXY: [] #Refering the positions of xyn
    #Constrains: 0 # Validates constrainst, when == 3 can start making the new arrays

#Loop through our nums array and give ArrX and ArrY A value for each Loop
# Return ArrXY

def orderedArray(nums,n):

    constraints = 0

    arrXY = []

    constraints +=1 if 1<=n<=500 else 1000
    constraints +=1 if len(nums)%2 == 0 else 1000
    constraints +=1 if 1<=len(nums) else 1000

    if constraints == 3:
        for i in range(n):
            arrXY.append(nums[i])
            arrXY.append(nums[i+n])


    return arrXY,print(arrXY)

orderedArray([2,5,1,3,4,7], 3)