import pytest


@pytest.fixture
def user_data():
    return {
        "name":"Bray",
        "job": "Albañil"
    }


def pytest_html_report_title( report ):
    report.title  = "API - REQURES PYTEST WITH REQUESTS"

