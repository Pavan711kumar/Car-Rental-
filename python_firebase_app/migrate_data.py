import pyrebase
import json

firebaseConfig = {
  "apiKey": "AIzaSyADX7F1MwQ0Q51GL_OXvyEi5aQ178LZZCc",
  "authDomain": "car-rental-a80f5.firebaseapp.com",
  "databaseURL": "https://car-rental-a80f5-default-rtdb.firebaseio.com",
  "projectId": "car-rental-a80f5",
  "storageBucket": "car-rental-a80f5.firebasestorage.app",
  "messagingSenderId": "891001606405",
  "appId": "1:891001606405:web:d85af9d8344aa4370fe76c",
  "measurementId": "G-D36Y7TX4WC"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Initial seed data extracted from the SQL file
brands = {
    "1": {"BrandName": "Maruti", "CreationDate": "2024-05-01 16:24:34"},
    "2": {"BrandName": "BMW", "CreationDate": "2024-05-01 16:24:34"},
    "3": {"BrandName": "Audi", "CreationDate": "2024-05-01 16:24:34"},
    "4": {"BrandName": "Nissan", "CreationDate": "2024-05-01 16:24:34"},
    "5": {"BrandName": "Toyota", "CreationDate": "2024-05-01 16:24:34"},
    "7": {"BrandName": "Volkswagon", "CreationDate": "2024-05-01 16:24:34"}
}

vehicles = {
    "1": {
        "VehiclesTitle": "Maruti Suzuki Wagon R",
        "VehiclesBrand": "1",
        "VehiclesOverview": "Maruti Wagon R Latest Updates...",
        "PricePerDay": 500,
        "FuelType": "Petrol",
        "ModelYear": 2019,
        "SeatingCapacity": 5,
        "Vimage1": "rear-3-4-left-589823254_930x620.jpg",
        "AirConditioner": 1,
        "PowerDoorLocks": 1,
        "AntiLockBrakingSystem": 1
    },
    "2": {
        "VehiclesTitle": "BMW 5 Series",
        "VehiclesBrand": "2",
        "VehiclesOverview": "BMW 5 Series price starts at...",
        "PricePerDay": 1000,
        "FuelType": "Petrol",
        "ModelYear": 2018,
        "SeatingCapacity": 5,
        "Vimage1": "BMW-5-Series-Exterior-102005.jpg",
        "AirConditioner": 1,
        "PowerDoorLocks": 1,
        "AntiLockBrakingSystem": 1
    },
    "3": {
        "VehiclesTitle": "Audi Q8",
        "VehiclesBrand": "3",
        "VehiclesOverview": "As per ARAI, the mileage of Q8 is 0 kmpl...",
        "PricePerDay": 3000,
        "FuelType": "Petrol",
        "ModelYear": 2017,
        "SeatingCapacity": 5,
        "Vimage1": "audi-q8-front-view4.jpg",
        "AirConditioner": 1,
        "PowerDoorLocks": 1,
        "AntiLockBrakingSystem": 1
    }
}

pages = {
    "aboutus": {
        "PageName": "About Us",
        "detail": "We offer a varied fleet of cars, ranging from the compact. All our vehicles have air conditioning, power steering, electric windows."
    },
    "terms": {
        "PageName": "Terms and Conditions",
        "detail": "Welcome to our Car Rental Portal. By using our service, you agree to our terms."
    },
    "privacy": {
        "PageName": "Privacy Policy",
        "detail": "We respect your privacy. This policy outlines how we handle your data."
    }
}

if __name__ == '__main__':
    print("Migrating data to Firebase...")
    try:
        db.child("brands").set(brands)
        print("Brands migrated successfully.")
        
        db.child("vehicles").set(vehicles)
        print("Vehicles migrated successfully.")
        
        db.child("pages").set(pages)
        print("Pages migrated successfully.")
        
        print("Migration complete!")
    except Exception as e:
        print(f"Error during migration: {e}")
