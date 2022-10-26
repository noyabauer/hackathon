from tkinter import *
from tkinter import ttk
# from hackathon.DataAccess import *
from hackathon.Const import *
from hackathon.Database import *

screen = Tk()
screen.title(TITLE)
screen.geometry(f"{WIDTH}x{HEIGHT}")
details_business = {
    "name": "",
    "area": "",
    "address": "",
    "category": ""
}
OPTIONS_ACCESSIBILITY = ["wheelchair", "vision impairment", "hearing impairment"]
OPTIONS_CATEGORY = ["Cinema / Theater", "Restaurant", "Store"]
costumer_choice = {
    "accessibility_type": None,
    "area": None,
    "category": None
}
OPTIONS_AREA = ["Center", "North", "South"]
OPTIONS_ANSWERS = ["Yes", "No"]
answers = {}
accessibility_business = {
    "wheelchair": True,
    "vision": True,
    "hearing": True
}
fitting_businesses = []
list_numbers = []


def center(scr=screen):
    """
    centers a tkinter window
    :param scr: the main window or Toplevel window to center
    """
    scr.update_idletasks()
    width = scr.winfo_width()
    frm_width = scr.winfo_rootx() - scr.winfo_x()
    win_width = width + 2 * frm_width
    height = scr.winfo_height()
    titlebar_height = scr.winfo_rooty() - scr.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = (scr.winfo_screenwidth() - win_width) // 2
    y = (scr.winfo_screenheight() - win_height) // 2
    scr.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    scr.deiconify()


def create_lst(length):
    for i in range(length):
        list_numbers.append(i + 1)
    print(list_numbers)


def create_dict(category1):
    num_of_questions = 0
    if category1 == "restaurant":
        num_of_questions = 9
    elif category1 == "store":
        num_of_questions = 8
    elif category1 == "cinema":
        num_of_questions = 10
    create_lst(num_of_questions)
    for i in range(num_of_questions):
        answers[i + 1] = list_numbers[i]
    print(answers)


def create_window_question_store():
    # region --------------------------------GLOBAL--------------------------------------
    global screen_isAccessible
    global answer1
    global answer2
    global answer3
    global answer4
    global answer5
    global answer6
    global answer7
    # endregion
    screen_isAccessible = Toplevel(screen)
    center()
    screen_isAccessible.title("Come check with us whether your business is accessible or not ! ")
    screen_isAccessible.geometry(f"{WIDTH + 100}x{HEIGHT}")
    center(screen_isAccessible)
    screen_isAccessible.configure(bg='light blue')

    create_dict(details_business["category"])

    answer1 = StringVar()
    answer2 = StringVar()
    answer3 = StringVar()
    answer4 = StringVar()
    answer5 = StringVar()
    answer6 = StringVar()
    answer7 = StringVar()

    Label(screen_isAccessible, text="Please answer the questions below and press Yes/No *", bg='light blue',
          font="calibri 8 bold").pack()
    Label(screen_isAccessible, text="Wheelchair Impairment:", bg='light blue',
          font="calibri 10 bold").place(x=10, y=0)

    # region ---------------------------------QUESTIONS------------------------------
    # question 1
    Label(screen_isAccessible, text=B_OWNER_QUESTION_STORE1_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=37, y=20)
    answer1 = StringVar(screen_isAccessible)
    answer1.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer1, *OPTIONS_ANSWERS)
    options.place(x=280, y=70, width=120, height=30)

    # question 2
    Label(screen_isAccessible, text=B_OWNER_QUESTION_STORE2_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=130, y=95)
    answer2 = StringVar(screen_isAccessible)
    answer2.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer2, *OPTIONS_ANSWERS)
    options.place(x=280, y=120, width=120, height=30)

    # question 3
    Label(screen_isAccessible, text=B_OWNER_QUESTION_STORE4_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=140, y=145)
    answer3 = StringVar(screen_isAccessible)
    answer3.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer3, *OPTIONS_ANSWERS)
    options.place(x=280, y=200, width=120, height=30)

    # question 4
    Label(screen_isAccessible, text=B_OWNER_QUESTION_STORE5_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=170, y=225)
    answer4 = StringVar(screen_isAccessible)
    answer4.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer4, *OPTIONS_ANSWERS)
    options.place(x=280, y=255, width=120, height=30)

    # question 5
    Label(screen_isAccessible, text=B_OWNER_QUESTION_STORE6_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=100, y=280)
    answer5 = StringVar(screen_isAccessible)
    answer5.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer5, *OPTIONS_ANSWERS)
    options.place(x=280, y=310, width=120, height=30)

    # question 6
    Label(screen_isAccessible, text=B_OWNER_QUESTION_STORE7_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=140, y=350)
    answer6 = StringVar(screen_isAccessible)
    answer6.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer6, *OPTIONS_ANSWERS)
    options.place(x=280, y=380, width=120, height=30)

    # question 7
    Label(screen_isAccessible, text="Wheelchair Impairment:", bg='light blue',
          font="calibri 10 bold").place(x=10, y=405)
    Label(screen_isAccessible, text=B_OWNER_QUESTION_STORE3_VISION, bg='light blue',
          font="calibri 15").place(x=90, y=420)
    answer7 = StringVar(screen_isAccessible)
    answer7.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer7, *OPTIONS_ANSWERS)
    options.place(x=280, y=470, width=120, height=30)
    # endregion
    submit1 = Button(screen_isAccessible, bg="light grey", fg="blue", text="Next", font="calibri 10", height=1,
                     width=15, command=next_page)
    submit1.place(x=570, y=470)
    screen_isAccessible.mainloop()


# region -----------------------------------HANDLE PRESSES - cinema------------------------------------------------
# question 1
def yes_pressed_once1():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice1).place(x=200, y=80)
    answers["1"] = True


def yes_pressed_twice1():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once1).place(x=200, y=80)


def no_pressed_once1():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice1).place(x=360, y=80)
    answers["1"] = False


def no_pressed_twice1():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once1).place(x=360, y=80)


# question 2
def yes_pressed_once2():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice2).place(x=200, y=135)
    answers["2"] = True


def yes_pressed_twice2():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once2).place(x=200, y=135)


def no_pressed_once2():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice2).place(x=360, y=135)
    answers["2"] = False


def no_pressed_twice2():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once2).place(x=360, y=135)


# question 3
def yes_pressed_once3():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice3).place(x=200, y=200)
    answers["3"] = True


def yes_pressed_twice3():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once3).place(x=200, y=200)


def no_pressed_once3():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice3).place(x=360, y=200)
    answers["3"] = False


def no_pressed_twice3():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once3).place(x=360, y=200)


# question 4
def yes_pressed_once4():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice4).place(x=200, y=255)
    answers["4"] = True


def yes_pressed_twice4():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once4).place(x=200, y=255)


def no_pressed_once4():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice4).place(x=360, y=255)
    answers["4"] = False


def no_pressed_twice4():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once4).place(x=360, y=255)


# question 5
def yes_pressed_once5():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice5).place(x=200, y=335)
    answers["5"] = True


def yes_pressed_twice5():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once5).place(x=200, y=335)


def no_pressed_once5():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice5).place(x=360, y=335)
    answers["5"] = False


def no_pressed_twice5():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once5).place(x=360, y=335)


# question 6
def yes_pressed_once6():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice6).place(x=200, y=390)
    answers["6"] = True


def yes_pressed_twice6():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once6).place(x=200, y=390)


def no_pressed_once6():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice6).place(x=360, y=390)
    answers["6"] = False


def no_pressed_twice6():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once6).place(x=360, y=390)


# question 7
def yes_pressed_once7():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice7).place(x=200, y=455)
    answers["7"] = True


def yes_pressed_twice7():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once7).place(x=200, y=455)


def no_pressed_once7():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice7).place(x=360, y=455)
    answers["7"] = False


def no_pressed_twice7():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once2).place(x=360, y=455)


# question 8
def yes_pressed_once8():
    Button(screen_questions2, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice8).place(x=200, y=100)
    answers["8"] = True


def yes_pressed_twice8():
    Button(screen_questions2, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once8).place(x=200, y=100)


def no_pressed_once8():
    Button(screen_questions2, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice8).place(x=360, y=100)
    answers["8"] = False


def no_pressed_twice8():
    Button(screen_questions2, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once8).place(x=360, y=100)


# question 9
def yes_pressed_once9():
    Button(screen_questions2, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice9).place(x=200, y=190)
    answers["9"] = True


def yes_pressed_twice9():
    Button(screen_questions2, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once9).place(x=200, y=190)


def no_pressed_once9():
    Button(screen_questions2, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice9).place(x=360, y=190)
    answers["9"] = False


def no_pressed_twice9():
    Button(screen_questions2, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once9).place(x=360, y=190)


# endregion


def create_window_question_cinema():
    # region --------------------------------GLOBAL--------------------------------------
    global screen_isAccessible
    global answer1
    global answer2
    global answer3
    global answer4
    global answer5
    global answer6
    global answer7
    # endregion
    screen_isAccessible = Toplevel(screen)
    center()
    screen_isAccessible.title("Come check with us whether your business is accessible or not ! ")
    screen_isAccessible.geometry(f"{WIDTH + 100}x{HEIGHT}")
    center(screen_isAccessible)
    screen_isAccessible.configure(bg='light blue')

    create_dict(details_business["category"])

    answer1 = StringVar()
    answer2 = StringVar()
    answer3 = StringVar()
    answer4 = StringVar()
    answer5 = StringVar()
    answer6 = StringVar()
    answer7 = StringVar()

    Label(screen_isAccessible, text="Please answer the questions below and press Yes/No *", bg='light blue',
          font="calibri 8 bold").pack()
    Label(screen_isAccessible, text="Wheelchair Impairment:", bg='light blue',
          font="calibri 15 bold").place(x=10, y=0)

    # region ---------------------------------QUESTIONS------------------------------
    # question 1
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA1_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=37, y=25)
    answer1 = StringVar(screen_isAccessible)
    answer1.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer1, *OPTIONS_ANSWERS)
    options.place(x=280, y=80, width=120, height=30)

    # question 2
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA2_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=130, y=105)
    answer2 = StringVar(screen_isAccessible)
    answer2.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer2, *OPTIONS_ANSWERS)
    options.place(x=280, y=135, width=120, height=30)

    # question 3
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA3_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=140, y=165)
    answer3 = StringVar(screen_isAccessible)
    answer3.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer3, *OPTIONS_ANSWERS)
    options.place(x=280, y=200, width=120, height=30)

    # question 4
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA5_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=170, y=225)
    answer4 = StringVar(screen_isAccessible)
    answer4.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer4, *OPTIONS_ANSWERS)
    options.place(x=280, y=255, width=120, height=30)

    # question 5
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA6_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=100, y=280)
    answer5 = StringVar(screen_isAccessible)
    answer5.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer5, *OPTIONS_ANSWERS)
    options.place(x=280, y=335, width=120, height=30)

    # question 6
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA8_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=140, y=360)
    answer6 = StringVar(screen_isAccessible)
    answer6.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer6, *OPTIONS_ANSWERS)
    options.place(x=280, y=390, width=120, height=30)

    # question 7
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA9_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=90, y=420)
    answer7 = StringVar(screen_isAccessible)
    answer7.set("select option")  # default value
    options = OptionMenu(screen_isAccessible, answer7, *OPTIONS_ANSWERS)
    options.place(x=280, y=455, width=120, height=30)
    # endregion
    submit1 = Button(screen_isAccessible, bg="light grey", fg="blue", text="Next", font="calibri 10", height=1,
                     width=15, command=next_page)
    submit1.place(x=570, y=470)
    screen_isAccessible.mainloop()


def next_page():
    # region ---------------------------------GLOBAL--------------------------------------------
    global screen_isAccessible
    global screen_questions2
    global answer1
    global answer2
    global answer3
    global answer4
    global answer5
    global answer6
    global answer7
    global answer8
    global answer9
    # endregion
    if answer1.get() == "No" or answer2.get() == "No" or answer3.get() == "No" or answer4.get() == "No" or answer5.get() \
            == "No" or answer6.get() == "No" or answer7.get() == "No":
        accessibility_business["wheelchair"] = False
    screen_questions2 = Toplevel(screen_isAccessible)
    center()
    screen_questions2.title("Come check with us whether your business is accessible or not ! - Vision&Hearing")
    screen_questions2.geometry(f"{WIDTH + 100}x{HEIGHT}")
    center(screen_questions2)
    screen_questions2.configure(bg='light blue')

    # region --------------------------------QUESTIONS----------------------------------------
    # question 8
    Label(screen_questions2, text="Vision Impairment:", bg='light blue',
          font="calibri 15 bold").place(x=60, y=5)

    Label(screen_questions2, text=B_OWNER_QUESTION_CINEMA4_VISION, bg='light blue',
          font="calibri 15").place(x=60, y=40)
    answer8 = StringVar(screen_questions2)
    answer8.set("select option")  # default value
    options = OptionMenu(screen_questions2, answer8, *OPTIONS_ANSWERS)
    options.place(x=280, y=100, width=120, height=30)

    # question 9
    Label(screen_questions2, text="Hearing Impairment:", bg='light blue',
          font="calibri 15 bold").place(x=60, y=130)

    Label(screen_questions2, text=B_OWNER_QUESTION_CINEMA7_HEARING, bg='light blue',
          font="calibri 15").place(x=130, y=160)
    answer9 = StringVar(screen_questions2)
    answer9.set("select option")  # default value
    options = OptionMenu(screen_questions2, answer9, *OPTIONS_ANSWERS)
    options.place(x=280, y=190, width=120, height=30)
    # endregion
    submit2 = Button(screen_questions2, bg="light grey", fg="blue", text="Done", font="calibri 10", height=1,
                     width=15, command=done_cinema)
    submit2.place(x=570, y=470)

    screen_questions2.mainloop()


def done_cinema():
    # region ---------------------------------GLOBAL--------------------------------------------
    global screen_isAccessible
    global screen_questions2
    global answer1
    global answer2
    global answer3
    global answer4
    global answer5
    global answer6
    global answer7
    global answer8
    global answer9
    # endregion
    if answer8.get() == "No":
        accessibility_business["vision"] = False
    if answer9.get() == "No":
        accessibility_business["hearing"] = False
    print(accessibility_business)
    add_to_database(details_business["name"], details_business["category"], details_business["area"],
                    details_business["address"], accessibility_business["wheelchair"], accessibility_business["vision"],
                    accessibility_business["hearing"], "https://realpython.com/iterate-through-dictionary-python/")


def restaurant_pressed1():
    Button(screen_owner, bg="dark blue", fg="white", text="Restaurant", font="calibri 15", height=1,
           width=15, command=restaurant_pressed2).place(x=40, y=400)
    details_business["category"] = "restaurant"


def restaurant_pressed2():
    Button(screen_owner, bg="light grey", fg="black", text="Restaurant", font="calibri 15", height=1,
           width=15, command=restaurant_pressed1).place(x=40, y=400)


def cinema_pressed1():
    Button(screen_owner, bg="dark blue", fg="white", text="Cinema / Theater", font="calibri 15", height=1,
           width=15, command=cinema_pressed2).place(x=230, y=400)
    details_business["category"] = "cinema / theater"


def cinema_pressed2():
    Button(screen_owner, bg="light grey", fg="black", text="Cinema / Theater", font="calibri 15", height=1,
           width=15, command=cinema_pressed1).place(x=230, y=400)


def store_pressed1():
    Button(screen_owner, bg="dark blue", fg="white", text="Store", font="calibri 15", height=1,
           width=15, command=store_pressed2).place(x=410, y=400)
    details_business["category"] = "store"


def store_pressed2():
    Button(screen_owner, bg="light grey", fg="black", text="Store", font="calibri 15", height=1,
           width=15, command=store_pressed1).place(x=410, y=400)


def owner():
    global screen_owner
    global name_business
    global category
    global address
    global variable
    screen_owner = Toplevel(screen)
    screen_owner.title("Business Owner")
    screen_owner.geometry(f"{WIDTH}x{HEIGHT}")
    center(screen_owner)
    screen_owner.configure(bg='light blue')
    question = Label(screen_owner, text="Hello, Business Owner", bg="light blue", font=("arial italic", 18)).pack()

    name_business = StringVar()
    category = StringVar()
    address = StringVar()

    Label(screen_owner, text="Please enter details bellow: ", bg='light blue', font="calibri 15 bold").pack()
    Label(screen_owner, text="Name of your business *", bg='light blue', font="calibri 15").pack()
    name_entry = Entry(screen_owner, textvariable=name_business).place(width=200, height=30, x=190, y=100)

    Label(screen_owner, text="What category does your business refers to? *", bg='light blue', font="calibri 15").place(
        x=130, y=360)
    restaurant_btn = Button(screen_owner, bg="light grey", fg="black", text="Restaurant", font="calibri 15", height=1,
                            width=15, command=restaurant_pressed1)
    restaurant_btn.place(x=40, y=400)
    cinema_btn = Button(screen_owner, bg="light grey", fg="black", text="Cinema / Theater", font="calibri 15", height=1,
                        width=15, command=cinema_pressed1)
    cinema_btn.place(x=230, y=400)
    store_btn = Button(screen_owner, bg="light grey", fg="black", text="Store", font="calibri 15", height=1,
                       width=15, command=store_pressed1)
    store_btn.place(x=410, y=400)

    Label(screen_owner, text="The area of your business *", bg='light blue', font="calibri 15").place(
        x=180, y=160)
    variable = StringVar(screen_owner)
    variable.set("select option")  # default value
    options = OptionMenu(screen_owner, variable, *OPTIONS_AREA)
    options.place(x=230, y=200, width=120, height=30)

    Label(screen_owner, text="The address of your business *", bg='light blue', font="calibri 15").place(x=170, y=260)
    address_entry = Entry(screen_owner, textvariable=address).place(x=190, y=300, width=200, height=30)

    done_btn = Button(screen_owner, bg="light grey", fg="dark blue", text="Submit", font="calibri 15", height=1,
                      width=60, command=owner_done).place(x=0, y=460)


def owner_done():
    details_business["name"] = name_business.get()
    details_business["area"] = variable.get()
    details_business["address"] = address.get()
    print(details_business)
    if details_business["category"] == "cinema / theater":
        create_window_question_cinema()
    elif details_business["category"] == "store":
        create_window_question_store()
    elif details_business["category"] == "restaurant":
        pass
    add_to_database(details_business["name"], details_business["category"], details_business["area"],
                    details_business["address"], accessibility_business["wheelchair"], accessibility_business["vision"],
                    accessibility_business["hearing"], "https://realpython.com/iterate-through-dictionary-python/")
    print("done")


# region -----------------------------------CUSTOMER GUI---------------------------------------------
def customer():
    global screen_customer
    global variable1
    global variable2
    global variable3
    screen_customer = Toplevel(screen)
    screen_customer.title("Customer")
    screen_customer.geometry(f"{WIDTH}x{HEIGHT}")
    center(screen_customer)
    screen_customer.configure(bg='light blue')
    question = Label(screen_customer, text="Hello Customer", bg="light blue", font=("arial italic", 18)).pack()
    Label(screen_customer, text="choose type of accessibility: *", bg='light blue', font="calibri 20").place(
        x=150, y=50)
    variable1 = StringVar(screen_customer)
    variable1.set("select option")  # default value
    options = OptionMenu(screen_customer, variable1, *OPTIONS_ACCESSIBILITY)
    options.place(x=150, y=125, width=175, height=30)
    Label(screen_customer, text="choose area:*", bg='light blue', font="calibri 20").place(
        x=150, y=200)
    variable2 = StringVar(screen_customer)
    variable2.set("select option")  # default value
    options = OptionMenu(screen_customer, variable2, *OPTIONS_AREA)
    options.place(x=150, y=275, width=120, height=30)
    Label(screen_customer, text="choose place to go:*", bg='light blue', font="calibri 20").place(
        x=150, y=350)
    variable3 = StringVar(screen_customer)
    variable3.set("select option")  # default value
    options = OptionMenu(screen_customer, variable3, *OPTIONS_CATEGORY)
    options.place(x=150, y=425, width=175, height=30)
    submit1 = Button(screen_customer, bg="light grey", fg="blue", text="submit", font="calibri 10", height=1,
                     width=15, command=submit_costumer_choice)
    submit1.place(x=450, y=450)


def submit_costumer_choice():
    costumer_choice["accessibility_type"] = variable1.get()
    costumer_choice["area"] = variable2.get()
    costumer_choice["category"] = variable3.get()
    print(costumer_choice)
    get_business_by_costumer_choice(costumer_choice["area"], costumer_choice["category"])


def get_business_by_costumer_choice(area, category):
    docs = db.collection(u'Business-owners').where(u'area', u'==', area).where(u'category', u'==', category).stream()
    for doc in docs:
        busi = doc.to_dict()
        fitting_businesses.append(busi)
    print(fitting_businesses)
    businesses(fitting_businesses)


def businesses(fitting_businesses):
    global screen_business
    screen_business = Toplevel(screen)
    screen_business.title("list of businesses")
    screen_business.geometry(f"{WIDTH}x{HEIGHT}")
    center(screen_business)
    screen_business.configure(bg='light blue')
    Label(screen_business, text="list of businesses for you", bg="light blue", font=("arial italic", 18)).pack()
    x = int(150)
    y = int(100)
    for business in fitting_businesses:
        name = business["name"]
        create_button(name, x, y)
        x = 30
        y += 30


def create_button(text, x_coor, y_coor):
    global screen_business
    button = Button(screen_business, bg="light grey", fg="blue", text=text, font="calibri 10", height=1,
                    width=15, command=submit_costumer_choice)
    button.place(x=x_coor, y=y_coor)


# endregion

def main_start():
    # Add a canvas widget
    center()
    canvas = Canvas(screen, width=WIDTH, height=HEIGHT, bg="light blue")

    img = PhotoImage(file=START_IMAGE, height=HEIGHT, width=WIDTH)
    canvas.background = img
    canvas.create_image(0, 0, anchor=NW, image=img)  # background image
    screen.configure(bg='light blue')

    # Create a button in canvas widget
    business_owner_button = Button(screen, bg="dark blue", fg="white", text="Business Owner", font="calibri 17",
                                   height=2,
                                   width=20, command=owner).pack()

    customer_butto = Button(screen, bg="dark blue", fg="white", text="Customer", font="calibri 17", height=2, width=20,
                            command=customer).pack(pady=10)
    canvas.pack()

    screen.mainloop()


if __name__ == '__main__':
    main_start()
