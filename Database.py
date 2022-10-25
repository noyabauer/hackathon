import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
cred = credentials.Certificate('/Users/noyabauer/Desktop/mechina/hackathon/hackathon/hackathon-f082d-firebase-adminsdk-8xvjk-176383c3f5.json')

app = firebase_admin.initialize_app(cred)
db = firestore.client()

def add_to_database(name,category,area,address,accessibility):
    data = {
        u'name': name,
        u'category': category,
        u'area': area,
        u'address': address,
        u'accessibility': accessibility
    }

    db.collection(u'Business-owners').document(name).set(data)


name= "mimi"
category = "restaurant"
area = "north"
address = "Ussishkin St 56, haifa"
accessibility= ["wheelchair"]
add_to_database(name,category,area,address,accessibility)
docs = db.collection(u'Business-owners').where(u'area', u'==', 'center').stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
