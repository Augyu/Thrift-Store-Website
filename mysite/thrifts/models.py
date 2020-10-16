from django.db import models
from datetime import datetime
import uuid
# Create your models here.

class Product():
    
    def __init__(self, name, price, img, description, seller, date_posted):
        self.id = uuid.uuid4
        self.name = name
        self.price = price
        self.img = img
        self.description = description
        self.seller = seller
        self.date_posted = date_posted  

products = []

for i in range(1, 20):
    if i % 3 == 1:
        product = Product("Airpod pro",
            325,    
            "image/electronics_three.jpg",
            "I've only used this Airpod pro twice",
            "David", "2020/10/12 20:45")
    elif i % 3 == 2:
        product = Product("Amazon Alexa",
            25,
            "image/electronics_two.jpg",
            "Want to buy Google Home. Don't need this anymore.",
            "David",
            "2020/10/13 16:40")
    else:
        product = Product("Air Fryer",
            325,
            "image/electronics_one.jpg",
            "Moving out this area...",
            "Jeff",
            "2020/10/13")
    
    products.append(product)



