from datetime import datetime
from random import randint
from flask_seeder import Seeder, Faker, generator

from app.repositories.models import Size, Beverage, Ingredient, Order, OrderDetail


# All seeders inherit from Seeder
class SizeSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create Size objects
        faker = Faker(
            cls=Size,
            init={
                "_id": generator.Sequence(start=1, end=5),
                "name": generator.String("(Small|Medium|Large|Familiar|Colossus)"),
                "price": generator.Integer(start=5, end=20)
            }
        )

        # Create 5 sizes
        for size in faker.create(5):
            self.db.session.add(size)


class IngredientSeeder(Seeder):

    def run(self):
        faker = Faker(
            cls=Ingredient,
            init={
                "_id": generator.Sequence(),
                "name": generator.String("(Cheese|Ham|Bacon|Chicken|Salami|Mushrooms|Sausage|Meat|Vegetables)"),
                "price": generator.Integer(start=1, end=2)
            }
        )
        for ingredient in faker.create(5):
            self.db.session.add(ingredient)


class BeverageSeeder(Seeder):

    def run(self):
        faker = Faker(
            cls=Beverage,
            init={
                "_id": generator.Sequence(),
                "name": generator.String("(Coke|Diet Coke|Water|Coffee|Juice)"),
                "price": generator.Integer(start=2, end=5)
            }
        )

        for ingredient in faker.create(5):
            self.db.session.add(ingredient)


class OrderSeeder(Seeder):

    def run(self):
        faker = Faker(
            cls=Order,
            init={
                "_id": generator.Sequence(start=1, end=100),
                "client_name": generator.String("(Fernando|Gabriela|Maria|Ana|Anthony|Luis)"),
                "client_dni": generator.String("(0984567000|0984567001|0984567002|0984567003|0984567004)"),
                "client_address": generator.String("(Address01|Address02|Address03|Address04|Address05)"),
                "client_phone": generator.String("09[0-9]{8}"),
                "date": datetime(year=2022, month=randint(1, 12), day=21),
                "total_price": generator.Integer(start=30, end=50),
                "size_id": generator.Integer(start=1, end=5)
            }
        )

        for order in faker.create(100):
            self.db.session.add(order)


class OrderDetailSeeder(Seeder):

    def run(self):
        faker = Faker(
            cls=OrderDetail,
            init={
                "_id": generator.Sequence(start=1, end=500),
                "ingredient_price": generator.Integer(start=1, end=5),
                "order_id": generator.Integer(start=1, end=100),
                "ingredient_id": generator.Integer(start=1, end=10),
                "beverage_price": generator.Integer(start=2, end=5),
                "beverage_id": generator.Integer(start=1, end=5),
            }
        )

        for order_detail in faker.create(500):
            self.db.session.add(order_detail)
