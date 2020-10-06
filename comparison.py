nums = [3, 2, 4, 3, 5, 8]

for num1 in nums:
    i = nums.index(num1)+1
    for num2 in nums[i:]:
        if num1 == num2:
            c = num1
            break
print('Output:', c)