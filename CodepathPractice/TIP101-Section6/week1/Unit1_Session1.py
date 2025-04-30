# # Problem1 ————————————————————————————————————————————————————————
# Problem 1: Hello World!
# Given the following lines of code, work with your group members to place the lines in order and write and call your first Python function!

# def hello_world():
# Define your function body here
#     print("Hello world!")


# hello_world() # Calls the above function

# # Problem2 ————————————————————————————————————————————————————————
# The following function uses a variable, mood to print out "Today's mood: 😎". Copy this code to your Replit and update the mood variable to print out your mood for today.

# def todays_mood():
#     mood = "😎"
#     print("Today's mood: " + mood)

# todays_mood()

# Example Output: Today's mood: 🥱


# def todays_mood():
#     mood = "😊"
#     print("Today's mood: " + mood)


# todays_mood()

# # Problem 3 ————————————————————————————————————————————————————————
# The following function accepts one parameter menu. Copy this code to your Replit and add a function call so that "Lunch today is: 🍕" is printed to the console.

# def print_menu(menu):
#     print("Lunch today is: " + menu)
# Example Output: Lunch today is: 🍜

# def print_menu(menu):
#     print("Lunch today is: " + menu)

# print_menu("noodle")


# 4
# def sum(a, b):
#     return a + b

# print(2 * sum(13, 27))


# # 5
# def product(a, b):
#     return a * b
# print(product(2, 3))


# # 6
# def classify_age(age):
#     if age < 18:
#         print("child")
#     else:
#         print("adult")

# classify_age(50)
# classify_age(16)


# # 7
# def what_time_is_it(hour):
#     if hour == 2:
#         print("It is taco time 🌮")
#     elif hour == 12:
#         print("peanut butter jelly time 🥪")
#     else:
#         print("nap time 😴")

# what_time_is_it(2)
# what_time_is_it(12)
# what_time_is_it(100)


# # 8
# def blackjack(score):
#     if score == 21:
#         print("Blackjack!")
#     elif score > 21:
#         print("Bust!")
#     elif score >= 17 and score < 21:
#         print("Nice hand!")
#     else:
#         print("Hit me!")

# blackjack(21)
# blackjack(200)
# blackjack(19)
# blackjack(2)


# # 9
# def get_first(lst):
#     if not lst:
#         return None
#     else:
#         print(lst[0])

# get_first([3, 1, 6, 7, 5])


# # 10
# def get_last(lst):
#     if not lst:
#         return None
#     else:
#         print(lst[-1])


# get_last([3, 1, 6, 7, 5])


# # 11
# def counter(stop):
#     for i in range(1, stop + 1):
#         print(i)


# counter(4)


# # 12
# def sum_ten():
#     sum = 0
#     for i in range(1, 11):
#         sum += i
#     return sum

# print(sum_ten())


# 13
# def sum_positive_range(stop):
#     total = 0
#     for i in range(1, stop + 1):
#         total += i
#     return total

# print(sum_positive_range(6))


# 14
# def sum_range(start, stop):
#     total = 0
#     for i in range(start, stop + 1):
#         total += i
#     return total

# print(sum_range(3, 9))

# 15
# def print_negatives(lst):
#     if not lst:
#         return None
#     for i in range(len(lst)):
#         if lst[i] < 0:
#             print(lst[i])

# print_negatives([3, -2, 2, 1, -5])
