# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_delivery(app):
    app.from_and_to_the_city(from_city_name=u"Москва", to_city_name=u"Санкт-Петербург")
    app.parameters_of_the_good(Group(length="10", width="20", height="30", weight="40"))
    app.press_submit_button()
    app.result_page()


def test_one_delivery(app):
    app.from_and_to_the_city(from_city_name=u"Москва", to_city_name=u"Санкт-Петербург")
    app.parameters_of_the_good(Group(length="1", width="1", height="1", weight="1"))
    app.press_submit_button()
    app.result_page()

