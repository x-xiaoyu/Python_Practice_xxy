# Problem 1: Calling Mississippi
# def count_mississippi(limit):
#     for num in range(1, limit):
#         print(f"{num} mississippi")

# count_mississippi(5)


# Problem 2: Swap Ends
# def swap_ends(my_str):
#     if len(my_str) < 2:
#         return my_str
#     return my_str[-1] + my_str[1:-1] + my_str[0]
# 🧵 小结：字符串切片技巧

# 表达式	意义
# my_str[0]	第一个字符
# my_str[-1]	最后一个字符
# my_str[1:-1]	中间部分（不含头尾）


# #双指针
# def swap_ends(my_str):
#     if len(my_str) <= 1:
#         return my_str

#     chars = list(my_str)  # 字符串转成列表
#     left = 0
#     right = len(chars) - 1

#     # 交换首尾字符
#     chars[left], chars[right] = chars[right], chars[left]

#     return ''.join(chars)  # 列表拼回字符串

# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)


# # Problem 3: Is Pangram
# def is_pangram(my_str):
#     my_str = my_str.lower()
#     return set(string.ascii_lowercase).issubet(my_str)


# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))


# # Problem 4: Reverse String
# def reverse_string(my_str):
#     return my_str[::-1]

# my_str = "live"
# print(reverse_string(my_str))


# Problem 5: First Unique
# def first_unique_char(my_str):
#     char_count = {}

#     for char in my_str:
#         char_count[char] = char_count.get(char, 0) + 1
#     # print(char_count)

#     for i, char in enumerate(my_str):
#         if char_count[char] == 1:
#             return i

#     return -1


# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))


# Problem 6: Minimum Distance
def min_distance(words, word1, word2):
    index1, index2 = -1, -1
    min_dist = float("inf")  # 修正变量名

    for i, word in enumerate(words):
        if word == word1:
            index1 = i
        elif word == word2:
            index2 = i
        if index1 != -1 and index2 != -1:
            min_dist = min(min_dist, abs(index1 - index2))  # 修正变量名
            if min_dist == 1:  # 直接返回最小可能距离
                return 1
    return min_dist if min_dist != float("inf") else -1  # 修正返回值逻辑


# 测试案例
words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)  # 2
print(dist2)  # 1

words2 = ["code", "path", "code", "contribute", "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)  # 2
