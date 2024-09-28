def has_33(nums): 
 for i in range(0, len(nums) - 1):
    if(nums[i] == 3 and nums[i + 1] == 3) or (nums[0] == 3 and nums[len(nums) - 1] == 3):
     print('True')
     return
 print('False')
 
list1 = [int(i) for i in input().split()]
has_33(list1)

