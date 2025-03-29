# -----------------------------------------------------------------  dictionary comprehension

# dic = {"A": 1, "B": 2, "C": 3}
# mul = {key: value*10 for key, value in dic.items()}
# print(mul)



# -----------------------------------------------------------------  dictionary

# dict1 = {'a': 100, 'b': 200, 'c': 300}
# dict2 = {'a': 300, 'b': 200, 'd': 400}
# for key in dict2:
#     if key in dict1:
#         dict1[key] += dict2[key]
#     else:
#         dict1[key] = dict2[key]
# print(dict1)



# -----------------------------------------------------------------  dictionary

# sample = {'a': 1, 'b': [1, 2, 3], 'c': 2, 'd': [4, 5, 6]}
# s = {key: (sum(val) if isinstance(val, list) else val)
#      for key, val in sample.items()}
# print(s)



# -----------------------------------------------------------------  list

# li1 = ['name', 'age', 'gender']
# li2 = ['Alice', 25, 'F']
# compained = {key: val for key, val in zip(li1, li2)}
# print(compained)



# -----------------------------------------------------------------  list

# li = ["cat", "dog", "monkey", "donkey", "cow"]
# new = [i for i in li if len(i) > 3]
# print(new)



# -----------------------------------------------------------------  remove vowels

# text = "List comprehensions are cool!"
# vow = "aeiouAEIOU"
# ans = ''.join([x for x in text if x not in vow])
# print(ans)



# -----------------------------------------------------------------  list comprehensions

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ans = [x for x in numbers if x % 2 == 0]
# print(ans)



# -----------------------------------------------------------------  list

# li = [-1, 3, -4, 7, 8]
# num = [x for x in li if x < 0 or x % 2 != 0]
# print(num)



# -----------------------------------------------------------------  list

# li = [1, 2, 3, 4, 5]
# new = [i*2 if i % 2 == 0 else i*3 for i in li]
# print(new)



# -----------------------------------------------------------------  list

# li = [1, 2, 3, 4, 5, 6, 7]
# list_com = ["Even" if x % 2 == 0 else "Odd" for x in li]
# lam = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", li))
# print(list_com)



# -----------------------------------------------------------------  dictionary

# num = {value: value*2 for value in range(1, 10) if value % 2 == 0}
# print(num)



# -----------------------------------------------------------------  count vowels

# s = "My name is Sooraj m s"
# count = 0
# for i in s:
#     if i in "AEIOUaeiou":
#         count += 1
# print(count)



# -----------------------------------------------------------------  generator

# def gen(num):
#     for i in range(1, 10):
#         total = i*num
#         yield total
# g = gen(5)
# print(next(g))
# print(next(g))



# -----------------------------------------------------------------  summing mixed type dict values

# sample = {'a': 1, 'b': [1, 2, 3], 'c': 2, 'd': [4, 5, 6]}
# get_sum = 0
# for i in sample.values():
#     if isinstance(i, int):
#         get_sum += i
#     elif isinstance(i, list):
#         get_sum += sum(i)
# print(get_sum)



# -----------------------------------------------------------------  finding duplicates

# li = [1, 2, 3, 1, 1, 2]
# printed = []
# for i in range(len(li)-1):
#     for j in range(i+1, len(li)):
#         if li[i] == li[j] and li[i] not in printed:
#             printed.append(li[i])
# print(printed)



# -----------------------------------------------------------------  second largest char in a str

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



# -----------------------------------------------------------------  factorial recursion

# def factorial(num):
#     if num <= 1:
#         return True
#     else:
#         return num * factorial(num-1)
# s = factorial(5)
# print(s)



# -----------------------------------------------------------------  destructuring

# user = [1, 3, 5]
# a, *c = user
# print(a, c)



# -----------------------------------------------------------------  merging dict

# dec1 = {'hi': 1, 'hello': 2}
# dec2 = {'hi': 3, 'hee': 4}
# com = {key: val for s in [dec1, dec2] for key, val in s.items()}
# com2 = {**dec1, **dec2}
# com3 = dec1 | dec2
# dec1.update(dec2)
# print(dec1)



# -----------------------------------------------------------------  replace

# word = 'restart'
# new_word = word[0]
# for i in range(1, len(word)):
#     if word[i] == word[0]:
#         new_word += '$'
#     else:
#         new_word += word[i]
# print(new_word)



# -----------------------------------------------------------------  filtering a list of dict

# li = [{'name': 'demo1', 'place': 'demo1 place', 'age': 10},
#       {'name': 'demo2', 'place': 'demo2 place', 'age': 20},
#       {'name': 'demo3', 'age': 30}]
# place = [i for i in li if 'place' in i]
# age = [i for i in li if i.get('age', 0) >= 20]
# print(place)



# -----------------------------------------------------------------  delete dict

# dic = {'name': 'demo', 'place': 'demo place'}
# del dic[max(dic, key=lambda x: len(dic[x]))]  # delete lengthy value keys
# del dic[max(dic, key=lambda x: len(x))]       # delete lengthy key of keys
# for i, j in dic.items():
#     if j == max(dic.values(), key=len):
#         del dic[i]
#         break
# print(dic)



# -----------------------------------------------------------------  zip

# a = ['a', 'b', 'c', 'd', 'e', 'f']
# b = [1, 2, 3, 4, 5]
# c = dict(zip(a, b))
# print(c)



# -----------------------------------------------------------------  random sample

# import random

# word = ''.join(random.sample('asdfsdf', 4))
# print(word)



# -----------------------------------------------------------------  flatten recursion

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



# -----------------------------------------------------------------  recursively summing

# arr = [[1, [1, 2, [1, 2, 3]]], [3, 4], [[1, 2], 6], 3]

# def get_sum(ans, li):
#     for i in li:
#         if isinstance(i, list):
#             ans += get_sum(0, i)
#         else:
#             ans += i
#     return ans

# print(get_sum(0, arr))



# -----------------------------------------------------------------  recursive remove char

# a = 'hello'

# def remove_ch(ch, a):
#     if not a:
#         return ch
#     if a[0] == 'e':
#         return remove_ch(ch, a[1:])
#     else:
#         return remove_ch(ch+a[0], a[1:])

# print(remove_ch('', a))



# -----------------------------------------------------------------  palindrome recursion

# def palindrome(word, left, right):
#     if left >= right:
#         return True
#     if word[0] != word[-1]:
#         return False
#     return palindrome(word, left + 1, right - 1)

# word = 'malayalam'
# print(palindrome(word, 0, len(word)-1))



# -----------------------------------------------------------------  fibonacci recursion

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6))



# -----------------------------------------------------------------  prime recursion

# def is_prime(n, i=2):
#     if i >= n:
#         return True
#     if n % i == 0:
#         return False
#     return is_prime(n, i + 1)

# print(is_prime(23))



# -----------------------------------------------------------------  sort dictionary

# dic = {20: 3, 30: 1, 10: 2}

# sorted_dict = sorted(dic.items(), key=lambda x:x[0])
# print(sorted_dict)



# -----------------------------------------------------------------  



