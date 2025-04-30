# 1
# def cast_vote(votes, candidate):
#     if candidate in votes:
#         votes[candidate] += 1 #候选人已存在加一票
#     else:
#         votes[candidate] = 1 #不存在就加进去
#     return votes


# votes = {"Alice": 5, "Bob": 3}
# cast_vote(votes, "Alice")
# print(votes)
# cast_vote(votes, "Gina")
# print(votes)


# # 2
# def common_keys(dict1, dict2):
#     new_list = []
#     for key in dict1:
#         if key in dict2:
#             new_list.append(key)
#     return new_list

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)

# 3
# def get_highest_priority_task(tasks):
#     # 初始化：还没找到任务时，设置默认
#     best_task = None
#     highest_priority = -1

#     for task, priority in tasks.items():
#         if priority > highest_priority:
#             best_task = task
#             highest_priority = priority
#         elif priority == highest_priority:
#             # 如果优先级一样，比字母顺序
#             if task < best_task:
#                 best_task = task

#     # 删除找到的任务
#     del tasks[best_task]
#     return best_task

# ✅ tasks.items() 是什么？
# 它是字典（dict）的一个方法，作用是：一次性把字典的 key 和 value 都拿出来，一对一对地用。

# tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}

# print(get_highest_priority_task(tasks))  # task2
# print(get_highest_priority_task(tasks))  # task4
# print(get_highest_priority_task(tasks))  # task3
# print(tasks)  # {'task1': 8, 'task5': 7}


# 4
# def count_occurrences(nums):
#     counts = {}
#     for num in nums:
#         if num in counts:
#             counts[num] += 1
#         else:
#             counts[num] = 1
#     return counts

# nums = [1, 2, 2, 3, 3, 3, 4]
# print(count_occurrences(nums))


# 5
# def find_majority_element(elements):
#     counts = {}

#     for num in elements:
#         if num in counts:
#             counts[num] += 1
#         else:
#             counts[num] = 1

#     majority_count = len(elements) // 2

#     for num, count in counts.items():
#         if count > majority_count:
#             return num

#     return None

# elements = [2, 2, 1, 1, 1, 2, 2]
# print(find_majority_element(elements))  # 输出 2

# print(find_majority_element([1, 2, 3, 4]))  # 输出 None


# 6
# def hasDuplicates(nums, k):
#     check_range = nums[:k+1]
#     seen = set()
#     for num in check_range:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False

# nums = [5, 6, 8, 2, 6, 4, 9]
# hasDuplicates(nums, 3) ➜ False  （前4个数没有重复）
# hasDuplicates(nums, 5) ➜ True   （6 出现两次）


# 7
# def divideList(nums):
#     from collections import Counter
#     counts = Counter(nums)
#     for count in counts.values():
#         if count % 2 != 0:
#             return False
#     return True

# divideList([3, 2, 3, 2, 2, 2]) ➜ True
# # 可以配对成：(2,2),(2,2),(3,3)

# divideList([1, 2, 3, 4]) ➜ False
# # 每个数字只出现1次，无法配对
