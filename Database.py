import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import webbrowser

cred = credentials.Certificate(
    '/Users/noyabauer/Desktop/mechina/hackathon/hackathon/hackathon-f082d-firebase-adminsdk-8xvjk-176383c3f5.json')

app = firebase_admin.initialize_app(cred)
db = firestore.client()


def add_to_database(name, category, area, address, wheelchair, vision, hearing, website):
    data = {
        u'name': name,
        u'category': category,
        u'area': area,
        u'address': address,
        u'wheelchair': wheelchair,
        u'vision': vision,
        u'hearing': hearing,
        u'website': website
    }

    db.collection(u'Business-owners').document(name).set(data)


def get_center_businesses():
    docs = db.collection(u'Business-owners').where(u'area', u'==', 'center').stream()

    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')


def get_north_businesses():
    docs = db.collection(u'Business-owners').where(u'area', u'==', 'north').stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')


def get_south_businesses():
    docs = db.collection(u'Business-owners').where(u'area', u'==', 'south').stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')


def get_wheelchair_businesses():
    docs = db.collection(u'Business-owners').where(u'wheelchair', u'==', True).stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')


def get_vision_businesses():
    docs = db.collection(u'Business-owners').where(u'vision', u'==', True).stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')


def get_hearing_businesses():
    docs = db.collection(u'Business-owners').where(u'hearing', u'==', True).stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')


def get_website(name):
    business_ref = db.collection(u'Business-owners').document(name)
    website=business_ref.get(field_paths={'website'}).to_dict().get('website')
    return website

def open_website(name):
    website=get_website(name)
    webbrowser.open(website)

name = input("enter name ")
category = input("enter category ")
area = input("enter area ")
address = input("enter address ")
wheelchair = True
vision = False
hearing = False
website = input("enter a link for your website ")
add_to_database(name, category, area, address, wheelchair, vision, hearing, website)
get_center_businesses()
get_north_businesses()
get_hearing_businesses()
open_website(name)