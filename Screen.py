from tkinter import *
from tkinter import ttk
from DataAccess import *
from Const import *

screen = Tk()


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


def register_user(success, err):
    """A function that registers a new user. The function uses the add_profile function from UserAccess."""
    global screen1
    username_info = username.get()
    password_info = password.get()
    confirm_password_info = password1.get()
    valid, errMessage = UserAccess.getInstance().add_profile(username_info, password_info, confirm_password_info)
    if valid:
        success.set("Sign up successfully")
        err.set("")
    else:
        success.set("")
        err.set(errMessage)


def register():
    """A function that creates the register window, all the buttons and labels. """
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Sign up")
    screen1.geometry("500x400")
    center()

    global username
    global password
    global password1
    global username_entry
    global password_entry
    global confirm_password_entry
    username = StringVar()
    password = StringVar()
    password1 = StringVar()

    Label(screen1, text="Please enter details bellow: ").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username *").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable=password, show="*")
    password_entry.pack()
    Label(screen1, text="Confirm Password *").pack()
    confirm_password_entry = Entry(screen1, textvariable=password1, show="*")
    confirm_password_entry.pack()
    success = StringVar()
    lblSuccess = Label(screen1, textvariable=success, fg="green", font=("calibri", 12)).pack()
    err = StringVar()
    lblError = Label(screen1, textvariable=err, fg="red", font=("calibri", 12)).pack()

    Button(screen1, text="Sign up", width=10, height=1, command=register_user).pack()


def login_verify(success, err):
    """ A function that verifies whether the user's details were true or nor using the
                   check_profile function from UserAccess class. """
    global screen1
    username1 = username_verify.get()
    password_user = password_verify.get()
    instance = UserAccess.getInstance()
    valid, errMessage = UserAccess.check_profile(instance, username1, password_user)
    if valid:
        success.set("Login successfully")
        err.set("")

    else:
        success.set("")
        err.set(errMessage)


def login():
    """A function that creates the login window, all the buttons and labels. """
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x400")
    center(screen2)
    Label(screen2, text="Please enter your details bellow to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username *").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify).pack()
    # username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password *").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show="*").pack()
    # password_entry1.pack()
    Label(screen2, text="").pack()

    success = StringVar()
    lblSuccess = Label(screen2, textvariable=success, fg="green", font=("calibri", 12)).pack()
    err = StringVar()
    lblError = Label(screen2, textvariable=err, fg="red", font=("calibri", 12)).pack()

    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main():
    """The __init__ function in the Login class.
          creates the login screen """
    screen.title(TITLE)
    screen.geometry('{}x{}'.format(WIDTH, HEIGHT))  # the window
    center(screen)

    canvas = Canvas(screen, width=WIDTH, height=HEIGHT)
    # canvas.grid()

    img = PhotoImage(file=START_IMAGE, height=HEIGHT, width=WIDTH)
    canvas.background = img
    canvas.create_image(0, 0, anchor=NW, image=img)  # background image

    # login button
    login_button = Button(screen, text="Customer", command=login)
    canvas.pack()
    # login_button = tk.Button(screen, bg="white", text="Login", height=2, width=15, command=login)
    login_button_window = canvas.create_window(300, 700, anchor=NW, window=login_button)

    # sign in button
    # sign_in_button = ttk.Button(screen, text="Sign up", command=register).pack()
    # sign_in_button_window = canvas.create_window(500, 700, anchor=tk.NW, window=sign_in_button)

    # Creating a photoimage object to use image
    # photo = tk.PhotoImage(file=SPEAKER_ON)

    # here, image option is used to
    # set image on button
    # audio_button = tk.Button(screen, text='Click Me !', image=photo, height=20, width=20, command=play_sound)
    # audio_button_window = canvas.create_window(10, 10, anchor=NW, window=audio_button)
    screen.mainloop()


main()
