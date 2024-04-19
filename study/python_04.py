def add(num1, num2):
    return num1 + num2

result1 = add(10,20)
print(result1)

def add(num1, num2, num3, num4):
    return num1 + num2,  num3 + num4 # 함수는 하나의 값만 리턴할 수 있다

result2, result3 = add(10, 20, 30, 40)
print(result2)
print(result3)

r1, r2 = (1, 2)
print(r1, r2)

nums = [5,2,7,3,1]
nums.sort()
nums.reverse() # sort, reverse는 return 값이 none이다.
print(nums)

# print(nums.index(10))

name = "이지언"
print(name.find("어")) # find는 못찾으면 -1
# print(name.index("어")) # index는 못찾으면 ValueError

user = {
    "username": "testuser",
    "password": "1234",
    "name": "이지언",
    "email": "test@gmail.com"
}

print(user)
user.update({
    "phone": "010-1234-5678",
    "name": "삼지언"
})
user["age"] = 25
print(user)
