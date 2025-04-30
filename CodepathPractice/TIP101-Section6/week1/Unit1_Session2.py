# # 1
# def print_list(lst):
#     for item in lst:
#         print(item)

# lst = ["squirtle", "gengar", "charizard", "pikachu"]
# print_list(lst)


# 2
# def doubled(lst):
#     for num in lst:
#         print(num * 2)


# # Example usage:
# lst = [1, 2, 3]
# doubled(lst)


# 3
# def doubled(lst):
#     new_lst = []  # 用于存储结果
#     for num in lst:  # 遍历原列表
#         new_lst.append(num * 2)  # 计算两倍并存入新列表
#     return new_lst  # 返回新列表


# # 测试代码
# lst = [1, 2, 3]
# new_lst = doubled(lst)
# print(new_lst)  # 预期输出: [2, 4, 6]

# # # 4
# def flip_sign(lst):
#     flipped_lst = []
#     for num in lst:
#         flipped_lst.append(num * -1)
#     return flipped_lst


# lst = [1, -2, -3, 4]
# flipped_lst = flip_sign(lst)  # 调用函数
# print(flipped_lst)  # 打印结果

# #5
# def max_difference(lst):
#     return max(lst) - min(lst)

# lst = [5, 22, 8, 10, 2]
# print(max_difference(lst))  # 预期输出: 20

# #6
# def count_less_than(numbers, threshold):
#     count = 0
#     for num in numbers:
#         if num < threshold:
#             count += 1
#     return count  # 返回小于 threshold 的元素个数

# numbers = [12, 8, 2, 4, 4, 10]
# counter = count_less_than(numbers, 5)  # 计算小于 5 的元素个数
# print(counter)  # 预期输出: 3

# #7
# def get_evens(lst):
#     evens = []
#     for num in lst:
#         if num % 2 == 0:
#             evens.append(num)
#     return evens  # 返回偶数列表

# lst = [1, 2, 3, 4]
# evens_lst = get_evens(lst)  # 获取偶数列表
# print(evens_lst)  # 预期输出: [2, 4]


# #8
# def multiples_of_five():
#     for num in range(5, 101, 5):  # 5 到 100（包括 100），步长为 5
#         print(num)

# # 调用函数
# multiples_of_five()

# #9
# def find_divisors(n):
#     divisors = []  # 存储因数的列表
#     for i in range(1, n + 1):  # 遍历从 1 到 n
#         if n % i == 0:  # 如果 n 能被 i 整除
#             divisors.append(i)  # 添加 i 到因数列表
#     return divisors  # 返回因数列表

# # 测试代码
# lst = find_divisors(6)
# print(lst)  # 预期输出: [1, 2, 3, 6]

# #10
# def fizzbuzz(n):
#     for i in range(1, n + 1):  # 遍历 1 到 n
#         if i % 15 == 0:  # 既是 3 又是 5 的倍数  if i % 3 == 0 and i % 5 == 0:  # 既是 3 又是 5 的倍数
#             print("FizzBuzz")
#         elif i % 3 == 0:  # 仅是 3 的倍数
#             print("Fizz")
#         elif i % 5 == 0:  # 仅是 5 的倍数
#             print("Buzz")
#         else:  # 其他情况，直接打印数字
#             print(i)

# # 调用函数
# fizzbuzz(13)

# #11
# def print_indices(lst):
#     for i in range(len(lst)):  # 遍历索引
#         print(i)  # 打印索引

# # 测试代码
# lst = [5, 1, 3, 8, 2]
# print_indices(lst)


# #12
# def linear_search(lst, target):
#     for i in range(len(lst)):  # 遍历索引 0 到 len(lst) - 1
#         if lst[i] == target:  # 如果当前索引处的元素等于 target
#             return i  # 返回索引
#     return -1  # 如果没找到，返回 -1

# # 测试代码
# lst = [1, 4, 5, 2, 8]
# print(linear_search(lst, 5))   # 预期输出: 2
# print(linear_search(lst, 10))  # 预期输出: -1

# def linear_search(lst, target):
#     for i, value in enumerate(lst):  # 遍历列表
#         if value == target:  # 如果找到目标值
#             return i  # 返回索引
#     return -1  # 如果没找到，返回 -1

# # 测试代码
# lst = [1, 4, 5, 2, 8]
# print(linear_search(lst, 5))   # 预期输出: 2
# print(linear_search(lst, 10))  # 预期输出: -1

# set2
# #1
# def convertTemp(celsius):
#     kelvin = round(celsius + 273.15, 2)
#     fahrenheit = round(celsius * 1.80 + 32.00, 2)
#     return [kelvin, fahrenheit]

# # 测试代码
# temperatures = convertTemp(23.00)
# print(temperatures)  # 预期输出: [296.15, 73.40]
