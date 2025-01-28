import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://realtimeattendance-a12de-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "111":
        {
            "name": "Eranga Dilshan",
            "major": "Sciences",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "Good",
            "year": 2,
            "last_attendance_time": "2025-01-20 00:54:34"
        },
    "122":
        {
            "name": "Lasith Malinga",
            "major": "Sports",
            "starting_year": 2024,
            "total_attendance": 6,
            "standing": "Good",
            "year": 2,
            "last_attendance_time": "2025-01-07 00:54:34"
        },
    "123":
        {
            "name": "Anura Kumara",
            "major": "Politics",
            "starting_year": 2024,
            "total_attendance": 4,
            "standing": "Good",
            "year": 1,
            "last_attendance_time": "2024-11-11 00:54:34"
        },
    "124":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2024,
            "total_attendance":4,
            "standing": "Bad",
            "year": 1,
            "last_attendance_time": "2024-12-20 00:54:34"
        }
}
for key, value in data.items():
    ref.child(key).set(value)