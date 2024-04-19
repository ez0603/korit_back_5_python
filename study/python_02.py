number = 10
print(type(number))

print(id(10)) # id() 주소값 확인
print(id(number))
number += 1
print(id(number))
number -= 1
print(id(number))

print(type("test")) # str
print(type([])) # list
print(type(())) # tuple
print(type({})) # dict

print([1,2,3,4])
print((1,2,3,4))
print({"id": 1, "name": "이지언"})

list1 = [1,2,3,4]
tp = (5,6,7,8)
dict1 = {"id": 1, "name": "이지언"}

print(list[0])
print(tp[0])
print(dict["id"])

list1.append(5)
print(list1)
print(tp.index(7))
list2 = list(tp)
print(list2)
print(dict1.keys()) 
print(dict1.values())
print(list(dict1.items())[0]) # 형 변환

print(True) # 파이썬은 대문자로 써야함
print(False)
