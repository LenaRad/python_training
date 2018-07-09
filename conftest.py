# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture(scope='session')  # tests run in the same browser
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)  # browser closes
    return fixture