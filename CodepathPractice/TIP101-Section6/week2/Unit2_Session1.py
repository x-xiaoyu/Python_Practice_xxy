# # 1
# def is_subsequence(lst, sequence):
#     if not sequence:
#         return True  # 空序列永远是任何列表的子序列

#     i = 0  # 指向 sequence
#     for num in lst:
#         if num == sequence[i]:
#             i += 1
#         if i == len(sequence):
#             return True
#     return False


# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))


# 2
# def create_dictionary(keys, values):
#     new_pairs = {}
#     for i in range(len(keys)):
#         new_pairs[keys[i]] = values[i]
#     return new_pairs

# 讲解
# keys[1] = "age"
# values[1] = 21
# 结果就会变成：
# new_pairs["age"] = 21

# def create_dictionary(keys, values):
#     new_pairs = {}
#     for k, v in zip(keys, values):
#         new_pairs[k] = v
#     return new_pairs


# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]
# print(create_dictionary(keys, values))


# 3
# def print_pair(dictionary, target):
#     value = dictionary.get(target)
#     if value is not None:
#         print(f"Key: {target}")
#         print(f"Value: {value}")
#     else:
#         print("That pair does not exist!")

# dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
# print_pair(dictionary, "patrick")
# print_pair(dictionary, "plankton")
# print_pair(dictionary, "spongebob")

# .get() 是字典的一个方法：
# dictionary.get(key)
# ✅ 它做的事是：如果 key 在字典里，就返回对应的值
# 如果 key 不在字典里，不会报错，而是返回 None（或你指定的默认值）


# 4
# def keys_v_values(dictionary):
#     key_sum = sum(dictionary.keys())  # 所有 keys 的总和 # dictionary.keys() 拿到所有的 key（不是 list，但可以迭代）
#     value_sum = sum(dictionary.values()) # 所有 value 的总和 # dictionary.values() 拿到所有的 value

#     if key_sum > value_sum:
#         return "keys"
#     elif value_sum > key_sum:
#         return "values"
#     else:
#         return "balanced"


# dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
# greater_sum = keys_v_values(dictionary1)
# print(greater_sum)

# dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
# greater_sum = keys_v_values(dictionary2)
# print(greater_sum)


# 5
# def restock_inventory(current_inventory, restock_list):
#     for item in restock_list:
#         if item in current_inventory:
#             current_inventory[item] += restock_list[item]
#         else:
#             current_inventory[item] = restock_list[item]
#     return current_inventory


# current_inventory = {"apples": 30, "bananas": 15, "oranges": 10}
# restock_list = {"oranges": 20, "apples": 10, "pears": 5}
# updated_inventory = restock_inventory(current_inventory, restock_list)
# print(updated_inventory)


# 6
# def calculate_gpa(report_card):
#     grade_points = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

#     total = 0
#     for subject in report_card:
#         letter = report_card[subject]  # 比如 "A"
#         total += grade_points[letter]  # 查表得分，比如 4

#     average = total / len(report_card)
#     return round(average, 2)


# report_card = {
#     "Math": "A",
#     "Science": "C",
#     "History": "A",
#     "Art": "B",
#     "English": "B",
#     "Spanish": "A",
# }
# print(calculate_gpa(report_card))


# # 7
# def highest_rated(books):
#     best_book = books[0]  # 先假设第一本书是最高的
#     for book in books:
#         if book["rating"] > best_book["rating"]:
#             best_book = book
#     return best_book


# books = [
#     {
#         "title": "Tomorrow, and Tomorrow, and Tomorrow",
#         "author": "Gabrielle Zevin",
#         "rating": 4.18,
#     },
#     {
#         "title": "A Fortune For Your Disaster",
#         "author": "Hanif Abdurraqib",
#         "rating": 4.47,
#     },
#     {
#         "title": "The Seven Husbands of Evelyn Hugo",
#         "author": "Taylor Jenkins Reid",
#         "rating": 4.40,
#     },
# ]

# print(highest_rated(books))

# 8、


# def index_to_value_map(lst):
#     result = {}
#     for i, value in enumerate(lst):
#         result[i] = value
#     return result


# lst = ["apple", "banana", "cherry"]
# print(index_to_value_map(lst))
