import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://realtimeattendance-644b5-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "210910":
        {
            "name": "Prajwal Bhosale",
            "subject": "Innovation Prototype",
            "starting_year": 2021,
            "total_attendance": 6,
            "batch": "A",
            "year": 2,
            "last_attendance": "2023-07-24 00:54:34"
        },
    "210911":
        {
            "name": "Sakshi Patil",
            "subject": "Web Technology",
            "starting_year": 2021,
            "total_attendance": 7,
            "batch": "C",
            "year": 2,
            "last_attendance": "2023-07-24 00:54:34"
        },
    "210912":
        {
            "name": "Kushal Ambi",
            "subject": "DBMS",
            "starting_year": 2021,
            "total_attendance": 8,
            "batch": "B",
            "year": 2,
            "last_attendance": "2023-07-24 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)