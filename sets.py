# nums=set()

# nums.add(1)
# nums.add(2)
# nums.add(4)

# nums.remove(2)
# print(nums)

# SET OPERATIONS

# a={1,2,3,4}
# b={2,4,1,5,6}
# UNION OPERATION
# ab=a-b
# print(ab)

# EXERCISES

# 1 remove duplicated
# nums=[1,1,2,3,2,4]

# print(set(nums))

# 2 FIND COMMON ELEMENT BETWEEN 2 lists
# a=[1,2,3,4]
# b=[2,2,4,1]
# print(set(a)&set(b))
# 3 find uniq word in sentense
# s="Hello All , Good Morning, Morning is Good But it is Not Good For me"
# uniq=set()

# for w in s.split(" "):
#     uniq.add(w.lower())
# print(uniq)

# Check if two strings are anagrams.
# a="listen"
# b="silent"

# aset=set(a)
# bset=set(b)
# if(len(aset)!=len(bset)):
#     print("False")
# else:
#     fa={}
#     fb={}
#     for c in a:
#       if c in fa:
#            fa[c]+=1
#       else:
#            fa[c]=1
#     for c in b:
#         if c in fb:
#            fb[c]+=1
#         else:
#            fb[c]=1
#     isAnagram=True
#     for ch in aset:
#         if fa[ch]!=fb[ch]:
#             isAnagram=False
#             break
#     print(isAnagram)

# FIND FIRST REPEATING ELEMENT
nums = [1, 2, 3, 4, 2, 5, 1]

track=set()

# for n in nums:
#     if n in track:
#         print(n)
#         break
#     else:
#         track.add(n)

s="Rahul"

for ch in s:
    print(ch)

