from django.db import models
from datetime import datetime

class Product():
    
    def __init__(self, id, name, price, img, description, seller, date_posted, comments):
        self.id = id
        self.name = name
        self.price = price
        self.img = img
        self.description = description
        self.seller = seller
        self.date_posted = date_posted
        self.comments = comments
    
    def getProductById(self, id):
        if self.id == id:
            return True

# buyers leave comments to sellers base on their products
class Comment():

    def __init__(self, comment, buyer, seller, date_posted):
        self.comment = comment
        self.buyer = buyer
        self.seller = seller
        self.date_posted = date_posted

comment1 = Comment('David cleaned the product before he sold it.',
    'Jenny',
    'David',
    datetime(2020, 9, 10))
comment2 = Comment('I would loved to buy things from David again.',
    'Frank',
    'David',
    datetime(2020, 4, 5))
comment3 = Comment('David cleaned the product before he sold it.',
    'Sharon',
    'David',
    datetime(2019, 3, 2))
comment4 = Comment('Really cheap things!',
    'Tim',
    'David',
    datetime(2016, 12, 24))
comments = [comment1, comment2, comment3, comment4]

products = []
for i in range(1, 20):
    if i % 3 == 1:
        product = Product(i,
            "Airpod pro",
            325,    
            ["image/electronics_three.jpg"],
            "This is a 99% new latest Airpods pro. I've only used two times and they don't fit my ears. Still have 11 months warranty. Available Time: Everyeveninig from Monday to Friday",
            "David",
            datetime.now(),
            comments)
    elif i % 3 == 2:
        product = Product(i,
            "Amazon Alexa",
            25,
            ["image/electronics_two.jpg"],
            "Want to buy Google Home. Don't need this anymore.",
            "David",
            datetime(2020, 10, 10, 13, 10),
            comments)
    else:
        product = Product(i,
            "Air Fryer",
            325,
            ["image/electronics_one.jpg"],
            "Moving out this area...",
            "Jeff",
            datetime(2020, 10, 13),
            comments)
    
    products.append(product)



