from tkinter import *
from tkinter import ttk
# from hackathon.DataAccess import *
from hackathon.Const import *

screen = Tk()
screen.title(TITLE)
screen.geometry(f"{WIDTH}x{HEIGHT}")
details_business = {
    "name": "",
    "area": "",
    "address": "",
    "category": ""
}
OPTIONS_AREA = ["Center", "North", "South"]
answers = {}
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


# region -----------------------------------HANDLE PRESSES - cinema------------------------------------------------
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


# question 2
def yes_pressed_once2():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice2).place(x=200, y=125)


def yes_pressed_twice2():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once2).place(x=200, y=125)


def no_pressed_once2():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice2).place(x=360, y=125)


def no_pressed_twice2():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once2).place(x=360, y=125)


# question 3
def yes_pressed_once3():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice3).place(x=200, y=190)


def yes_pressed_twice3():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once3).place(x=200, y=190)


def no_pressed_once3():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice3).place(x=360, y=190)


def no_pressed_twice3():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once3).place(x=360, y=190)


# question 4
def yes_pressed_once4():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice4).place(x=200, y=245)


def yes_pressed_twice4():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once4).place(x=200, y=245)


def no_pressed_once4():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice4).place(x=360, y=245)


def no_pressed_twice4():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once4).place(x=360, y=245)


# question 5
def yes_pressed_once5():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice5).place(x=200, y=325)


def yes_pressed_twice5():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once5).place(x=200, y=325)


def no_pressed_once5():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice5).place(x=360, y=325)


def no_pressed_twice5():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once5).place(x=360, y=325)


# question 6
def yes_pressed_once6():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice6).place(x=200, y=380)


def yes_pressed_twice6():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once6).place(x=200, y=380)


def no_pressed_once6():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice6).place(x=360, y=380)


def no_pressed_twice6():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once6).place(x=360, y=380)


# question 7
def yes_pressed_once7():
    Button(screen_isAccessible, bg="dark green", fg="white", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_twice7).place(x=200, y=445)


def yes_pressed_twice7():
    Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10", height=1,
           width=15, command=yes_pressed_once7).place(x=200, y=445)


def no_pressed_once7():
    Button(screen_isAccessible, bg="red", fg="white", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_twice7).place(x=360, y=445)


def no_pressed_twice7():
    Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
           width=15, command=no_pressed_once2).place(x=360, y=445)


# endregion


def create_window_question():
    global screen_isAccessible
    screen_isAccessible = Toplevel(screen)
    center()
    screen_isAccessible.title("Come check with us whether your business is accessible or not ! ")
    screen_isAccessible.geometry(f"{WIDTH + 100}x{HEIGHT}")
    center(screen_isAccessible)
    screen_isAccessible.configure(bg='light blue')

    create_dict(details_business["category"])

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
    yes_btn2 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                      height=1, width=15, command=yes_pressed_once2)
    yes_btn2.place(x=200, y=125)
    no_btn2 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                     width=15, command=no_pressed_once2)
    no_btn2.place(x=360, y=125)

    # question 3
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA3_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=140, y=155)
    yes_btn3 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                      height=1, width=15, command=yes_pressed_once3)
    yes_btn3.place(x=200, y=190)
    no_btn3 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                     width=15, command=no_pressed_once3)
    no_btn3.place(x=360, y=190)

    # question 4
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA5_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=170, y=215)
    yes_btn4 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                      height=1, width=15, command=yes_pressed_once4)
    yes_btn4.place(x=200, y=245)
    no_btn4 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                     width=15, command=no_pressed_once4)
    no_btn4.place(x=360, y=245)

    # question 5
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA6_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=100, y=270)
    yes_btn5 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                      height=1, width=15, command=yes_pressed_once5)
    yes_btn5.place(x=200, y=325)
    no_btn5 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                     width=15, command=no_pressed_once5)
    no_btn5.place(x=360, y=325)

    # question 6
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA8_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=140, y=350)
    yes_btn6 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                      height=1, width=15, command=yes_pressed_once6)
    yes_btn6.place(x=200, y=380)
    no_btn6 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                     width=15, command=no_pressed_once6)
    no_btn6.place(x=360, y=380)

    # question 7
    Label(screen_isAccessible, text=B_OWNER_QUESTION_CINEMA9_WHEELCHAIR, bg='light blue',
          font="calibri 15").place(x=90, y=410)
    yes_btn7 = Button(screen_isAccessible, bg="light grey", fg="black", text="Yes", font="calibri 10",
                      height=1, width=15, command=yes_pressed_once7)
    yes_btn7.place(x=200, y=445)
    no_btn7 = Button(screen_isAccessible, bg="light grey", fg="black", text="No", font="calibri 10", height=1,
                     width=15, command=no_pressed_once7)
    no_btn7.place(x=360, y=445)

    submit1 = Button(screen_isAccessible, bg="light grey", fg="blue", text="Next", font="calibri 10", height=1,
                    width=15, command=next_page)
    submit1.place(x=570, y=470)
    screen_isAccessible.mainloop()


def next_page():
    pass


def restaurant_pressed1():
    Button(screen_owner, bg="dark blue", fg="white", text="Restaurant", font="calibri 15", height=1,
           width=15, command=restaurant_pressed2).place(x=40, y=400)
    details_business["category"] = "restaurant"


def restaurant_pressed2():
    Button(screen_owner, bg="light grey", fg="black", text="Restaurant", font="calibri 15", height=1,
           width=15, command=restaurant_pressed1).place(x=40, y=400)


def cinema_pressed1():
    Button(screen_owner, bg="dark blue", fg="white", text="Cinema", font="calibri 15", height=1,
           width=15, command=cinema_pressed2).place(x=230, y=400)
    details_business["category"] = "cinema"


def cinema_pressed2():
    Button(screen_owner, bg="light grey", fg="black", text="Cinema", font="calibri 15", height=1,
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
    cinema_btn = Button(screen_owner, bg="light grey", fg="black", text="Cinema", font="calibri 15", height=1,
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
    create_window_question()


def customer():
    global screen_customer
    screen_customer = Toplevel(screen)
    screen_customer.title("Customer")
    screen_customer.geometry(f"{WIDTH}x{HEIGHT}")
    center(screen_customer)
    screen_customer.configure(bg='light blue')
    question = Label(screen_customer, text="Hello Customer", bg="light blue", font=("arial italic", 18)).pack()


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
