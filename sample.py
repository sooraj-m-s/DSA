# dec = {"A": 1, "B": 2, "C": 3}
# mul = {key: value*10 for key, value in dec.items()}
# print(mul)


# dict1 = {'a': 100, 'b': 200, 'c': 300}
# dict2 = {'a': 300, 'b': 200, 'd': 400}
# for key in dict2:
#     if key in dict1:
#         dict1[key] += dict2[key]
#     else:
#         dict1[key] = dict2[key]
# print(dict1)


# sample = {'a': 1, 'b': [1, 2, 3], 'c': 2, 'd': [4, 5, 6]}
# s = {key: (sum(val) if isinstance(val, list) else val)
#      for key, val in sample.items()}
# print(s)


# li1 = ['name', 'age', 'gender']
# li2 = ['Alice', 25, 'F']
# compained = {key: val for key, val in zip(li1, li2)}
# print(compained)


# li = ["cat", "dog", "monkey", "donkey", "cow"]
# new = [i for i in li if len(i) > 3]
# print(new)


# text = "List comprehensions are cool!"
# vow = "aeiouAEIOU"
# ans = ''.join([x for x in text if x not in vow])
# print(ans)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ans = [x for x in numbers if x % 2 == 0]
# print(ans)


# li = [-1, 3, -4, 7, 8]
# num = [x for x in li if x < 0 or x % 2 != 0]
# print(num)


# li = [1, 2, 3, 4, 5]
# new = [i*2 if i % 2 == 0 else i*3 for i in li]
# print(new)


# li = [1, 2, 3, 4, 5, 6, 7]
# list_com = ["Even" if x % 2 == 0 else "Odd" for x in li]
# lam = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", li))
# print(list_com)


# num = {value: value*2 for value in range(1, 10) if value % 2 == 0}
# print(num)


# s = "My name is Sooraj m s"
# count = 0
# for i in s:
#     if i in "AEIOUaeiou":
#         count += 1
# print(count)


# def gen(num):
#     for i in range(1, 10):
#         total = i*num
#         yield total
# g = gen(5)
# print(next(g))
# print(next(g))


# sample = {'a': 1, 'b': [1, 2, 3], 'c': 2, 'd': [4, 5, 6]}
# get_sum = 0
# for i in sample.values():
#     if isinstance(i, int):
#         get_sum += i
#     elif isinstance(i, list):
#         get_sum += sum(i)
# print(get_sum)


# li = [1, 2, 3, 1, 1, 2]
# printed = []
# for i in range(len(li)-1):
#     for j in range(i+1, len(li)):
#         if li[i] == li[j] and li[i] not in printed:
#             printed.append(li[i])
# print(printed)


# name = "abcdyz"
# largest = ""
# second = ""
# for i in name:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i
# print(second)


# def sample(num):
#     if num < 1:
#         return True
#     else:
#         return num*sample(num-1)
# s = sample(5)
# print(s)


# user = [1, 3, 5]
# a, *c = user
# print(a, c)


# dec1 = {'hi': 1, 'hello': 2}
# dec2 = {'hi': 3, 'hee': 4}
# com = {key: val for s in [dec1, dec2] for key, val in s.items()}
# com2 = {**dec1, **dec2}
# com3 = dec1 | dec2
# dec1.update(dec2)
# print(dec1)


# a = 'restart'
# b = a[0]
# new = a[0]
# for i in range(1, len(a)):
#     if a[i] == b:
#         new += '$'
#     else:
#         new += a[i]
# print(new)


# li = [{'name': 'demo1', 'place': 'demo1 place', 'age': 10},
#       {'name': 'demo2', 'place': 'demo2 place', 'age': 20},
#       {'name': 'demo3', 'age': 30}]
# place = [i for i in li if 'place' in i]
# age = [i for i in li if i.get('age', 0) >= 20]
# print(place)


# dic = {'name': 'demo', 'place': 'demo place'}
# del dic[max(dic, key=lambda x: len(dic[x]))]  # delete lengthy value keys
# del dic[max(dic, key=lambda x: len(x))]       # delete lengthy key of keys
# for i, j in dic.items():
#     if j == max(dic.values(), key=len):
#         del dic[i]
#         break
# print(dic)


# a = ['a', 'b', 'c', 'd', 'e', 'f']
# b = [1, 2, 3, 4, 5]
# c = dict(zip(a, b))
# print(c)


# import random

# s = ''.join(random.sample('asdfsdf', 4))
# print(s)


# def flatten(arr):
#     temp = []
#     for i in arr:
#         if isinstance(i, list):
#             temp.extend(flatten(i))
#         else:
#             temp.append(i)
#     return temp

# arr = [[1, [1, 2, [1, 2, 3]]], [3, 4], [[1, 2], 6]]
# print(flatten(arr))
