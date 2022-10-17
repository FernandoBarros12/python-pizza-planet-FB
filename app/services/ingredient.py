from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from app.services.service_decorator import service_decorator

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
@service_decorator
def create_ingredient():
    return IngredientController.create(request.json)


@ingredient.route('/', methods=PUT)
@service_decorator
def update_ingredient():
    return IngredientController.update(request.json)


@ingredient.route('/id/<_id>', methods=GET)
@service_decorator
def get_ingredient_by_id(_id: int):
    return IngredientController.get_by_id(_id)


@ingredient.route('/', methods=GET)
@service_decorator
def get_ingredients():
    return IngredientController.get_all()
