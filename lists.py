# nums=[1,2,90,1,3,1,10,100]
# FIND MAX NUMS from an Array (0(N))
# max=nums[0]
# for n in nums:
#     if max<n:
#         max=n
# print(max)

# FIND SECOND LARGEST NUMBER
# max1=nums[0]
# max2=nums[0]
# for n in nums:
#     if max1<n:
#         max2=max1
#         max1=n

# print(max2)

# REMOVE DUPLICATES MANUALLY
# nums.sort()
# right=0
# while right<len(nums):
   
#     if right>0 and nums[right]==nums[right-1]:
#         nums.pop(right)
#     else:
#         right+=1
# print(nums)

# REVERSE LIST
# print(nums)
# left=0
# right=len(nums)-1
# while left<right:
#     nums[left],nums[right]=nums[right],nums[left]
#     left+=1
#     right-=1
# print(nums)

# COUNT FREQUENCY OF ELEMENTS
# freq={}
# for n in nums:
#     if n in freq:
#         freq[n]+=1
#     else:
#         freq[n]=1
# print(freq)

# MOVE ALL ZERO TO END
# nums=[0,1,0,3,12]
 
# left=0
# for right in range(len(nums)):
#     if nums[right]!=0:
#         nums[left],nums[right]=nums[right],nums[left]
#         left+=1
    
# print(nums)

# Pythonic way to Find square of a number
# square=[n*n for n in nums]
# print(square)

# CREATE SQUARE OF THE LIST

# nums=[1,2,3,4,5,6]

# sqr=[n*n for n in nums]

# print(sqr)

# EXTRACT VOWELS from a string
# name="binita swain"

# vowles=[ch for ch in name if ch in "aeiou"]

# print(vowles)

# GET EVENT NUMBER ONLY
nums=[1,2,3,4,5,6]

evens=[n for n in nums if n%2==0]
print(evens)

# converts list of string to upper case

names=["rahul","binita"]

res=[s.upper() for s in names]
print(res)