# 1 FUNCTION TO REVERSE A STRING
def reverse(s:str)->str:
    return s[::-1]

# print(reverse("GUNI"))

# 2 FUNCTION TO CHECK PALINDROME 
def checkPalindrome(s:str)->bool:
    return s==reverse(s)

# print(checkPalindrome("lol"))

# 3 FUNCTION TO FIND MAX ELEMENT
def findMax(nums:list[int])->int:
     max=nums[0]
     for n in nums:
         if max<n:
             max=n
     return max 

# print(findMax([1,4,5,6,1,2]))
# 4 CREATE A FUNCTION TO COUNT VOWLES
def countVowles(s:str)->int:
    count=0
    for ch in s:
        if ch in "aeiou":
            count+=1
    return count
# print(countVowles("rahul"))

# 5. CREATE CALCULATOR FUNCTION
def calculator(a:int,b:int,operation:str):
    match operation:
        case "add":
            return a+b
        case "substract":
            return a-b
        case "multiply":
            return a*b
        case "devide":
            return a/b
        case _:
            return "Invalid Operation"
        
# print(calculator(10,4,"multiply"))

# USING *ARGS

def sum(*nums):
     s=0
     for n in nums:
         s+=n
     return s 

print(sum(1,2,3,4,5))
 