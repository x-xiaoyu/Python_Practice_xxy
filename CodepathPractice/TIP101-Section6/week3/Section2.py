# # Problem Set Version 1

# # Problem 1: Sum of Strings
# # Write a function sum_of_number_strings() that takes in a list of strings nums.
# # Each string is a representations of integers. The function should return the sum of these strings as an integer.

# # 方法一：
# # def sum_of_number_strings(nums):
# #     return sum(map(int, nums))


# # nums = ["10", "20", "30"]
# # sum = sum_of_number_strings(nums)
# # print(sum)

# # 方法二：
# #     total = 0  # Initialize a variable to store the sum

# #     # Loop through each string in the list
# #     for num in nums:
# #         # Convert the string to an integer
# #         integer_value = int(num)

# #         # Add the integer to the total
# #         total += integer_value

# #         # Print the current number and the running total for better understanding
# #         print(f"Adding {integer_value}. Current total: {total}")

# #     # Return the final sum
# #     return total


# # Problem 2: Remove Duplicates
# # Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list.
# # The function returns the modified list.


# # def remove_duplicates(nums):
# #     return list(sorted(set(nums)))  # 先去重，再排序，确保有序


# # nums = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6]
# # print(remove_duplicates(nums))
# # # Output: no_dups = [1,2,3,4,5,6]


# # 方法二：
# # def remove_duplicates(nums):
# #     if not nums:
# #         return []

# #     result = [nums[0]]  # 先存第一个元素
# #     for i in range(1, len(nums)):
# #         if nums[i] != nums[i - 1]:  # 只存不同的元素
# #             result.append(nums[i])

# #     return result

# # 方法三：双指针
# # def remove_duplicates(nums):
# #     if not nums:
# #         return []

# #     slow = 0
# #     for fast in range(1, len(nums)):
# #         if nums[fast] != nums[slow]:
# #             slow += 1
# #             nums[slow] = nums[fast]

# #     return nums[:slow + 1]


# # Problem 3: Reverse Letters
# # Write a function reverse_only_letters() that takes in a string s as a parameter. The function reverses the order of the letters in the string and returns the new string.
# # Non-letter characters should remain in their original positions.
# def reverse_only_letters(s):
#     s = list(s)  # 字符串转列表（因为字符串是不可变的）
#     left, right = 0, len(s) - 1  # Define two pointers

#     while left < right:
#         if not s[left].isalpha():  # if left side is not character, skip
#             left += 1
#         elif not s[right].isalpha():  # if right side is not character, skip
#             right -= 1
#         else:
#             s[left], s[right] = s[right], s[left]  # swap
#             left += 1
#             right -= 1

#     return "".join(s)  # Convert list back to string


# # # 方法二：
# # def reverse_only_letters(s):
# #     # Step 1: Extract all letters from the string
# #     letters = [char for char in s if char.isalpha()]  # Get only letters
# #     letters.reverse()  # Reverse the letters list

# #     # Step 2: Build the new result by iterating through the original string
# #     result = []  # Store the new string
# #     letter_index = 0  # Keep track of where we are in the reversed letters list

# #     for char in s:
# #         if char.isalpha():  # If it's a letter, replace with the next reversed letter
# #             result.append(letters[letter_index])
# #             letter_index += 1  # Move to the next reversed letter
# #         else:
# #             result.append(char)  # Keep non-letter characters unchanged

# #     return "".join(result)  # Convert list back to string


# # Example Usage:
# # s = "a-bC-dEf-ghIj"
# # reversed_s = reverse_only_letters(s)
# # print(reversed_s)
# # Example Output: j-Ih-gfE-dCba


# # Problem 4: Longest Uniform Substring
# # Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring. A uniform substring consists of a single repeated character.


# # def longest_uniform_substring(s):
# #     pass


# # Example Usage:
# # s1 = "aabbbbCdAA"
# # l1 = longest_uniform_substring(s1)
# # print(l1)

# # s2 = "abcdef"
# # l2 = longest_uniform_substring(s2)
# # print(l2)
# # Example Output:
# # 4
# # 1


# # Problem 5: Teemo's Attack
# # In the game League of Legends, Teemo attacks his enemy Ashe with poison arrows. Write a function find_poisoned_duration() that takes in two parameters: time_series (the time at which Teemo's attacks hits Ashe) and time_duration (the duration of the poisoning effect). The function returns the total time that Ashe is in a poisoned condition.

# # time_series is a list of integers that represents the times at which Teemo attacks and makes Ashe poisoned for the exact time_duration.

# # If Teemo hits Ashe while she is still poisoned, the poison's duration starts over. For example, if Teemo attacks at times 1 and 4 for 3 seconds, the states at each time would be:

# # 1: attacked
# # 2: in poison state
# # 3: in poison state
# # 4: attacked, poison duration resets to 3
# # 5: in poison state
# # 6: in poison state
# # 7: in poison state
# # 8: in normal state
# # This means that the total time that Ashe is in a poisoned condition is 5.


# def find_poisoned_duration(time_series, duration):
#     pass


# # Example Usage:
# # time_series = [1,4,9]
# # damage = find_poisoned_duration(time_series, 3)
# # print(damage)
# # Example Output: 8

# # Problem 6: Sum Unique Elements
# # Write a function sum_of_unique_elements() that takes in two lists of integers, lst1 and lst2, as parameters and returns the sum of the elements that are unique in lst1.

# # An element is unique if:


# # it appears exactly once in lst1
# # it does not appear in lst2
# def sum_of_unique_elements(lst1, lst2):
#     pass


# # Example Usage:
# # lstA = [1, 2 ,3, 4]
# # lstB = [3, 4, 5, 6]
# # lstC = [7, 7, 7, 7]

# # sum1 = sum_of_unique_elements(lstA, lstB)
# # print(sum1)

# # sum2 = sum_of_unique_elements(lstC, lstB)
# # print(sum2)
# # Example Output

# # 3
# # 0
