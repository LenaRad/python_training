# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture(scope='session')  # tests run in the same browser
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)  # logout and browser closes
    return fixture