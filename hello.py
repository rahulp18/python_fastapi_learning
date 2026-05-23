name="apple"
city="Cuttack"
address="""I am from Cuttack
Odisha India"""
age=24
# print("My Name is ",name, "and I am from ",city,". I am ",age," years old. My address is ",address)
# print(f"My name is {name} and i am from {address.strip()}. I am {age} years old.") 
# for ch in name:
#     print(ch)
# chars=list(name)
# print(chars)
# print(name[0])
# print(name[len(name)-1])
# vowels="aeiou"
# count=0
# for ch in name:
#     if ch in vowels:
#         count=count+1
# print(count)
# CHECK PALINDROME
# SIMPLE
# reverse=name[::-1]
# if name==reverse:
#     print("Yes it's a palindrome")
# else:
#     print("No it's Not")
# BETTER
# left=0
# right=len(name)-1
# isPalin=True
# while left<right:
#     if name[left]==name[right]:
#         left=left+1
#         right=right-1
#     else:
#         isPalin=False
#         break
# if isPalin:
#     print("Yes it's a palindrome")
# else:
#     print("No it's not")
 
#  COUNT FREQUENCY
freq={}
for ch in name:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

print(freq)


# NOTES
# Strings are immutable means if i am creating one string then changin it it will create new string not modify that