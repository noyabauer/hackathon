import tkinter as tk
from DataAccess import *
from Const import *


screen = tk.Tk()


def center(screen):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    screen.update_idletasks()
    width = screen.winfo_width()
    frm_width = screen.winfo_rootx() - screen.winfo_x()
    win_width = width + 2 * frm_width
    height = screen.winfo_height()
    titlebar_height = screen.winfo_rooty() - screen.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = (screen.winfo_screenwidth() - win_width) // 2
    y = (screen.winfo_screenheight() - win_height) // 2
    screen.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    screen.deiconify()


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
    screen1 = tk.Toplevel(screen)
    screen1.title("Sign up")
    screen1.geometry("500x400")
    center(screen1)

    global username
    global password
    global password1
    global username_entry
    global password_entry
    global confirm_password_entry
    username = tk.StringVar()
    password = tk.StringVar()
    password1 = tk.StringVar()

    tk.Label(screen1, text="Please enter details bellow: ").pack()
    tk.Label(screen1, text="").pack()
    tk.Label(screen1, text="Username *").pack()
    username_entry = tk.Entry(screen1, textvariable=username)
    username_entry.pack()
    tk.Label(screen1, text="Password *").pack()
    password_entry = tk.Entry(screen1, textvariable=password, show="*")
    password_entry.pack()
    tk.Label(screen1, text="Confirm Password *").pack()
    confirm_password_entry = tk.Entry(screen1, textvariable=password1, show="*")
    confirm_password_entry.pack()
    success = tk.StringVar()
    lblSuccess = tk.Label(screen1, textvariable=success, fg="green", font=("calibri", 12)).pack()
    err = tk.StringVar()
    lblError = tk.Label(screen1, textvariable=err, fg="red", font=("calibri", 12)).pack()

    tk.Button(screen1, text="Sign up", width=10, height=1, command=register_user).pack()


def main():
    """The __init__ function in the Login class.
          creates the login screen """
    screen.title(TITLE)
    screen.geometry('{}x{}'.format(900, 800))  # the window
    center(screen)

    img = tk.PhotoImage(file=LOGO_IMAGE)
    screen.iconphoto(False, img)  # sets the icon

    canvas = tk.Canvas(screen, width=900, height=800)
    canvas.grid()

    img = tk.PhotoImage(file=START_IMAGE, height=800, width=900)
    canvas.background = img
    canvas.create_image(0, 0, anchor=tk.NW, image=img)  # background image

    # login button
    login_button = tk.Button(screen, bg="white", text="Login", height=2, width=15, command=login)
    login_button_window = canvas.create_window(300, 700, anchor=NW, window=login_button)

    # sign in button
    sign_in_button = tk.Button(screen, bg="white", text="Sign up", height=2, width=15, command=register)
    sign_in_button_window = canvas.create_window(500, 700, anchor=NW, window=sign_in_button)

    # Creating a photoimage object to use image
    # photo = tk.PhotoImage(file=SPEAKER_ON)

    # here, image option is used to
    # set image on button
    # audio_button = tk.Button(screen, text='Click Me !', image=photo, height=20, width=20, command=play_sound)
    # audio_button_window = canvas.create_window(10, 10, anchor=NW, window=audio_button)

    screen.mainloop()
