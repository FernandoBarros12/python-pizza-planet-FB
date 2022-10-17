import pytest


def test_get_report_service(client, report_uri, create_orders):
    response = client.get(report_uri)
    report = response.json

    pytest.assume(response.status.startswith('200'))
    pytest.assume(report['top_ingredient'])
    pytest.assume(report['top_month'])
    pytest.assume(report['top_one'])
    pytest.assume(report['top_two'])
    pytest.assume(report['top_three'])
