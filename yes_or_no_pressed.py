from tkinter import *
from hackathon.IsAccessible import *


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
