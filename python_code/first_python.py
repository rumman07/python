'''
python code to move zero to the end in a list
'''
list = [1,2,0,3,0,4,5,0,7,0,0]

def move_zero(nums):
  count =0
  for num in nums:
    if num != 0:
      nums[count] = num
      count += 1
  nums[count:] = [0] * (len(nums) - count)
  return nums

print(move_zero(list))



