from app.common.http_methods import GET, POST
from flask import Blueprint, request

from app.services.service_decorator import service_decorator

from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
@service_decorator
def create_order():
    return OrderController.create(request.json)


@order.route('/id/<_id>', methods=GET)
@service_decorator
def get_order_by_id(_id: int):
    return OrderController.get_by_id(_id)


@order.route('/', methods=GET)
@service_decorator
def get_orders():
    return OrderController.get_all()
