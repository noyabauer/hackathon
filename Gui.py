from tkinter import *
from tkinter import ttk
from hackathon.DataAccess import *
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
    business_owner_button = Button(screen, bg="dark blue", fg="white", text="Business Owner", font="calibri 17", height=2,
                                   width=20, command=owner).pack()

    customer_butto = Button(screen, bg="dark blue", fg="white", text="Customer", font="calibri 17", height=2, width=20,
                            command=customer).pack(pady=10)
    canvas.pack()

    screen.mainloop()


if __name__ == '__main__':
    main_start()
