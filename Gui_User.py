from tkinter import *
from hackathon.Const import *
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
fitting_businesses=[]

cred = credentials.Certificate(
    r'C:\Users\daphna.c\PycharmProjects\lia_hackathon\hackathon\hackathon-f082d-firebase-adminsdk-8xvjk-176383c3f5.json')

app = firebase_admin.initialize_app(cred)
db = firestore.client()

screen = Tk()
screen.title(TITLE)
screen.geometry(f"{WIDTH}x{HEIGHT}")
OPTIONS_ACCESSIBILITY=["wheelchair","vision impairment","hearing impairment"]
OPTIONS_AREA = ["Center", "North", "South"]
OPTIONS_CATEGORY= ["Cinema / Theater","Restaurant","Store"]
costumer_choice ={
    "accessibility_type":None,
    "area":None,
    "category":None
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
    costumer_choice["accessibility_type"]= variable1.get()
    costumer_choice["area"]=variable2.get()
    costumer_choice["category"]=variable3.get()
    print(costumer_choice)
    get_business_by_costumer_choice(costumer_choice["area"],costumer_choice["category"])
def get_business_by_costumer_choice(area,category):
    docs = db.collection(u'Business-owners').where(u'area', u'==', area).where(u'category', u'==', category).stream()
    for doc in docs:
        busi=doc.to_dict()
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
    x=int(150)
    y=int(100)
    for business in fitting_businesses:
        name=business["name"]
        create_button(name,x,y)
        x=30
        y+=30
def create_button(text,x_coor,y_coor):
    global screen_business
    button=Button(screen_business, bg="light grey", fg="blue", text=text, font="calibri 10", height=1,
           width=15, command=submit_costumer_choice)
    button.place(x=x_coor,y=y_coor)



def main_start():
    # Add a canvas widget
    center()
    canvas = Canvas(screen, width=WIDTH, height=HEIGHT, bg="light blue")

    img = PhotoImage(file=START_IMAGE, height=HEIGHT, width=WIDTH)
    canvas.background = img
    canvas.create_image(0, 0, anchor=NW, image=img)  # background image
    screen.configure(bg='light blue')

    # Create a button in canvas widget

    customer_button = Button(screen, bg="dark blue", fg="white", text="Customer", font="calibri 17", height=2, width=20,
                            command=customer).pack(pady=10)
    canvas.pack()

    screen.mainloop()


if __name__ == '__main__':
    main_start()