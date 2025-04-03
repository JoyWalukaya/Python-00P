# Class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, storage_capacity):
        self.brand = brand
        self.model = model
        self.storage_capacity = storage_capacity

    # Method to make a call
    def make_call(self, phone_number):
        print(f"Calling {phone_number} from {self.brand} {self.model}...")

    # Method to store data
    def store_data(self, data):
        print(f"Storing {data} on {self.brand} {self.model}...")

# Creating an instance of Smartphone
my_phone = Smartphone("Apple", "iPhone 13", "128GB")

# Using the methods
my_phone.make_call("123-456-7890")
my_phone.store_data("Photos and Videos")

# Inheriting Smartphone class
class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage_capacity, camera_quality):
        super().__init__(brand, model, storage_capacity)  # Inheriting constructor
        self.camera_quality = camera_quality

    # Method to take photos
    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} camera quality...")

# Creating an instance of CameraPhone
camera_phone = CameraPhone("Samsung", "Galaxy S21", "256GB", "108MP")

# Using inherited and new methods
camera_phone.make_call("987-654-3210")
camera_phone.take_photo()
