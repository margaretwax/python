# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_delivery(app):
    app.from_city_name(u"Москва", u"Москва, г. Москва")
    app.to_city_name(Group(u"Санкт-Петербург", u"Санкт-Петербург, г. Санкт-Петербург"))
    app.length("20")
    app.width("30")
    app.height("40")
    app.weight("50")

