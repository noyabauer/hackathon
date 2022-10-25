from tkinter import *
from tkinter import ttk
from DataAccess import *
from Const import *

screen = Tk()
screen.title(TITLE)
screen.geometry(f"{WIDTH}x{HEIGHT}")


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


def owner():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Business Owner")
    screen1.geometry(f"{WIDTH}x{HEIGHT}")
    center(screen1)
    screen1.configure(bg='light blue')


def customer():
    print("customer")


# Add a canvas widget
center()
canvas = Canvas(screen, width=WIDTH, height=HEIGHT, bg="light blue")

img = PhotoImage(file=START_IMAGE, height=HEIGHT, width=WIDTH)
canvas.background = img
canvas.create_image(0, 0, anchor=NW, image=img)  # background image
screen.configure(bg='light blue')

# Create a button in canvas widget
business_owner_button = Button(screen, bg="dark blue", fg="white", text="Business Owner", font="calibri 17", height=2, width=20, command=owner).pack()

customer_butto = Button(screen, bg="dark blue", fg="white", text="Customer", font="calibri 17", height=2, width=20, command=customer).pack(pady=10)
canvas.pack()

screen.mainloop()
