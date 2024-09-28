def has_33(nums): 
 for i in range(0, len(nums)):
    if nums[i] == 0:
     for j in range(i + 1, len(nums)):
       if nums[j] == 0:
         for k in range(j + 1, len(nums)):
           if nums[k] == 7:
            print("True")
            return

     
 print('False')
 
list1 = [int(i) for i in input().split()]
has_33(list1)

