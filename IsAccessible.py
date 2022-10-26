#
# answers = {}
# list_numbers = []
# category = "cinema"
#
#
# def create_lst(length):
#     for i in range(length):
#         list_numbers.append(i + 1)
#     print(list_numbers)
#
#
# def create_dict(category1):
#     num_of_questions = 0
#     if category1 == "restaurant":
#         num_of_questions = 9
#     elif category1 == "store":
#         num_of_questions = 8
#     elif category1 == "cinema":
#         num_of_questions = 10
#     create_lst(num_of_questions)
#     for i in range(num_of_questions):
#         answers[i + 1] = list_numbers[i]
#     print(answers)
#
#
# def yes_pressed_once1():
#     Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
#            width=15, command=yes_pressed_twice1).place(x=200, y=70)
#
#
# def yes_pressed_twice1():
#     Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
#            width=15, command=yes_pressed_once1).place(x=200, y=70)
#
#
# def no_pressed_once1():
#     Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
#            width=15, command=no_pressed_twice1).place(x=360, y=70)
#
#
# def no_pressed_twice1():
#     Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
#            width=15, command=no_pressed_once1).place(x=360, y=70)
#
#
# # question 2
# def yes_pressed_once2():
#     Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
#            width=15, command=yes_pressed_twice1).place(x=200, y=125)
#
#
# def yes_pressed_twice2():
#     Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
#            width=15, command=yes_pressed_once1).place(x=200, y=125)
#
#
# def no_pressed_once2():
#     Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
#            width=15, command=no_pressed_twice2).place(x=360, y=125)
#
#
# def no_pressed_twice2():
#     Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
#            width=15, command=no_pressed_once2).place(x=360, y=125)
