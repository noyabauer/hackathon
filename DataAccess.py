from firebase import Firebase
import firebase_admin
from firebase_admin import credentials, firestore
from socket import *
import re


KEY_PATH = r"C:\Users\משתמש\hackathon\serviceAccountKey.json"


class UserAccess:
    config = \
        {
            "apiKey": "AIzaSyB7loFA3plqHNCOUtmjy1WPXmIQkmjFELU",
            "authDomain": "hackathon-f082d.firebaseapp.com",
            "databaseURL": "https://hackathon-f082d.firebaseio.com",
            "storageBucket": "hackathon-f082d.appspot.com",
            "serviceAccount": r"C:\Users\משתמש\hackathon\serviceAccountKey.json"
        }
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if UserAccess.__instance is None:
            UserAccess()
        return UserAccess.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if UserAccess.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            UserAccess.__instance = self
            firebase_obj = Firebase(self.config)  # connect to fire base by config
            # Gets a reference to the auth service
            self.auth = firebase_obj.auth()  # create an authentication connection to the firebase
            cred = credentials.Certificate(KEY_PATH)
            firebase_admin.initialize_app(cred)
            self.firestore_db = firestore.client()
            self.name = ''
