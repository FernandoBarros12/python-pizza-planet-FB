from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from app.services.service_decorator import service_decorator

from ..controllers import SizeController

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
@service_decorator
def create_size():
    return SizeController.create(request.json)


@size.route('/', methods=PUT)
@service_decorator
def update_size():
    return SizeController.update(request.json)


@size.route('/id/<_id>', methods=GET)
@service_decorator
def get_size_by_id(_id: int):
    return SizeController.get_by_id(_id)


@size.route('/', methods=GET)
@service_decorator
def get_sizes():
    return SizeController.get_all()
