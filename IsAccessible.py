from hackathon.Gui import *

answers = {}
list_numbers = []
category = "cinema"


def create_lst(length):
    for i in range(length):
        list_numbers.append(i + 1)
    print(list_numbers)


def create_dict(category):
    num_of_questions = 0
    if category == "restaurant":
        num_of_questions = 9
    elif category == "store":
        num_of_questions = 8
    elif category == "cinema":
        num_of_questions = 10
    create_lst(num_of_questions)
    for i in range(num_of_questions):
        answers[i + 1] = list_numbers[i]
    print(answers)


def yes_pressed_once1():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice1).place(x=200, y=70)


def yes_pressed_twice1():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once1).place(x=200, y=70)


def no_pressed_once1():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice1).place(x=360, y=70)


def no_pressed_twice1():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once1).place(x=360, y=70)


center()
screen_isAccessible = Toplevel(screen)
screen_isAccessible.title("Come check with us whether your business is accessible or not !")
screen_isAccessible.geometry(f"{WIDTH + 100}x{HEIGHT}")
center(screen_isAccessible)
screen_isAccessible.configure(bg='light blue')

create_dict("cinema")

answer1 = StringVar()

Label(screen_isAccessible, text="Please answer the questions below and press Yes/No *", bg='light blue',
      font="calibri 10 bold").pack()

# question 1
Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA1_WHEELCHAIR, bg='light blue',
      font="calibri 15").place(x=37, y=15)
yes_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                  height=1, width=15, command=yes_pressed_once1)
yes_btn1.place(x=200, y=70)
no_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                 width=15, command=no_pressed_once1)
no_btn1.place(x=360, y=70)

# question 2
Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA2_WHEELCHAIR, bg='light blue',
      font="calibri 15").place(x=130, y=95)
yes_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                  height=1, width=15)
yes_btn1.place(x=200, y=125)
no_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                 width=15)
no_btn1.place(x=360, y=125)

# question 3
Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA3_WHEELCHAIR, bg='light blue',
      font="calibri 15").place(x=140, y=155)
yes_btn3 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                  height=1, width=15)
yes_btn3.place(x=200, y=190)
no_btn3 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                 width=15)
no_btn3.place(x=360, y=190)

# question 4
Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA5_WHEELCHAIR, bg='light blue',
      font="calibri 15").place(x=170, y=215)
yes_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                  height=1, width=15)
yes_btn1.place(x=200, y=245)
no_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                 width=15)
no_btn1.place(x=360, y=245)

# question 5
Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA6_WHEELCHAIR, bg='light blue',
      font="calibri 15").place(x=100, y=270)
yes_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                  height=1, width=15)
yes_btn1.place(x=200, y=325)
no_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                 width=15)
no_btn1.place(x=360, y=325)

# question 6
Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA8_WHEELCHAIR, bg='light blue',
      font="calibri 15").place(x=140, y=350)
yes_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                  height=1, width=15)
yes_btn1.place(x=200, y=380)
no_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                 width=15)
no_btn1.place(x=360, y=380)

# question 7
Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA9_WHEELCHAIR, bg='light blue',
      font="calibri 15").place(x=90, y=410)
yes_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                  height=1, width=15)
yes_btn1.place(x=200, y=445)
no_btn1 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                 width=15)
no_btn1.place(x=360, y=445)

screen_isAccessible.mainloop()
