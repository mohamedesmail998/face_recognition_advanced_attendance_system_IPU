import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://ittehd-privte-university-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Mohamed Esmail",
            "major": "IT",
            "starting_year": 2017,
            "total_attendance": 0,
            "standing": "G",
            "year": 5,
            "last_attendance_time": "2023-3-3 00:54:34"
        },
    "852741":
        {
            "name": "Raed mahmasa",
            "major": "IT",
            "starting_year": 2017,
            "total_attendance": 2,
            "standing": "B",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Mohamed mujahed",
            "major": "IT",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)