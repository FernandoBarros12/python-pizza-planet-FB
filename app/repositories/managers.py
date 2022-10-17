import datetime
from typing import Any, List, Optional, Sequence

from sqlalchemy import extract, func, desc

from sqlalchemy.sql import text, column
import operator

from .models import Beverage, Ingredient, Order, OrderDetail, Size, db
from .serializers import (BeverageSerializer,
                          IngredientSerializer,
                          OrderSerializer,
                          SizeSerializer,
                          ma)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(
            cls.model._id.in_(set(ids))
        ).all() or []


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(
            cls.model._id.in_(set(ids))
        ).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls,
               order_data: dict,
               ingredients: List[Ingredient],
               beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all((OrderDetail(order_id=new_order._id,
                                         ingredient_id=ingredient._id,
                                         ingredient_price=ingredient.price)
                             for ingredient in ingredients))
        cls.session.add_all((OrderDetail(order_id=new_order._id,
                                         beverage_id=beverage._id,
                                         beverage_price=beverage.price)
                             for beverage in beverages))
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()


class ReportManager(BaseManager):
    serializer = OrderSerializer

    @classmethod
    def get__most_requested_ingredient(cls):
        query_ingredient = cls.session.query( (Ingredient.name).label('field'), func.count(OrderDetail.ingredient_id).label('value') ).join(Ingredient).group_by(Ingredient.name).order_by(desc('value')).limit(1)
        wanted_ingredient = query_ingredient[0].field
        times = query_ingredient[0].value
        return [wanted_ingredient, times]

    @classmethod
    def get_most_wealthy_month(cls):
        query_month = cls.session.query( extract('month', Order.date).label('field'), func.sum(Order.total_price).label('value')).group_by('field').order_by(desc('value')).limit(1)
        most_wealthy_month = datetime.date(2022, query_month[0].field, 21).strftime('%B')
        profit = query_month[0].value
        return [most_wealthy_month, profit]


    @classmethod
    def get_top_three_customers(cls):
        query_top_customers = cls.session.query( (Order.client_name).label('field'), func.count(Order.client_name).label('value') ).group_by('field').order_by(desc('value')).limit(3)
        result = []
        for customer in query_top_customers:
            result.append( (customer.field, customer.value) )
        return result

    @classmethod
    def get_report(cls):
        most_wanted_ingredient = cls.get__most_requested_ingredient()
        most_profitable_month = cls.get_most_wealthy_month()
        top_three_customers = cls.get_top_three_customers()
        return {"top_ingredient": most_wanted_ingredient,
                "top_month": most_profitable_month,
                "top_one": top_three_customers[0],
                "top_two": top_three_customers[1],
                "top_three": top_three_customers[2]
                }
