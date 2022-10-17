import pytest

from app.controllers import ReportController


def test_get_report(app, create_orders):
    created_report, error = ReportController.get_report()
    pytest.assume(error is None)
    for param, value in created_report.items():
        pytest.assume(value == created_report[param])
        pytest.assume(created_report['top_ingredient'])
        pytest.assume(created_report['top_month'])
        pytest.assume(created_report['top_one'])
        pytest.assume(created_report['top_two'])
        pytest.assume(created_report['top_three'])
