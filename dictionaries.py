# user={
#     "name":"Rahul Pradhan",
#     "age":24,
#     "address":"Choudwar Gola Sahi Cuttack Odisha",
   
# }
# # user["address"]="Choudwar Cuttack"
# # del user["address"]

# user["profession"]="Ai Engineer"
# # user.pop("spouse")
# # print(user)
# # print("name" in user)
# # for key,value in user.items():
# #     print(f"{key}::{value}")
# user["spouse"]={
#    "name":"Binita Swain",
#    "age":20,
#    "address":"Gupteswar Sahi,Cuttack Choudwar "
# }
# print(user["spouse"])

# nums=[1,2,3,4,5,6]

# squares={n:n*n for n in nums}
# NORMAL WAY
# for n in nums:
#     squares[n]=n*n
# print(squares)

# COUNT FREQUENCY OF WORDS
name="I love python I love AI"

freq={}

words=name.split(" ")
 

# for w in words:
#     if w in freq:
#         freq[w]+=1
#     else:
#         freq[w]=1
# print(freq)
# COUNT MAX FREQUENCY OF AN CHAR
# count=1
# res=name[0]
# for w in words:
#     for ch in w:
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1
#         if count<freq[ch]:
#             count=freq[ch]
#             res=ch
# print(count,res)

# MERGE TWO DICTIONARY

a={"x":1,"y":2}
b={"z":2}

# for key,val in b.items():
#     a[key]=val
print({**a,**b})