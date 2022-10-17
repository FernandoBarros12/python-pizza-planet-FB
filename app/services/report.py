from app.common.http_methods import GET
from flask import Blueprint

from app.services.service_decorator import service_decorator

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
@service_decorator
def get_report():
    return ReportController.get_report()
