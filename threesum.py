'''
Three Sum Problem
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
'''

    
if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6]
    target = 9

    for num1 in arr:
        for num2 in arr:
            for num3 in arr:
                if num1 + num2 + num3 == target:
                    print(num1, num2, num3)

