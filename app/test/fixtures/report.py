import pytest


@pytest.fixture
def report_uri():
    return '/report/'


@pytest.fixture
def created_report():
    return {'top_ingredient': ('Ham', 54),
            'top_month': ('March', 4000),
            "top_one": ('Julio', 40),
            "top_two": ('Sofia', 25),
            "top_three": ('Dany', 10)}
