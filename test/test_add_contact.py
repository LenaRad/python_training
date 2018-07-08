# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname='firstname', middlename='middlename', lastname='lastname',
                                        nickname='nickname', title='title', company='company', address='address',
                                        home='home', mobile='mobile', work='work', fax='fax', email='email',
                                        email2='email2', email3='email3', homepage='homepage', byear='byear',
                                        ayear='ayear', address2='address2', phone2='phone2', notes='notes'))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname='', middlename='', lastname='', nickname='', title='', company='',
                                        address='', home='', mobile='', work='', fax='', email='', email2='', email3='',
                                        homepage='', byear='', ayear='', address2='', phone2='', notes=''))
    app.logout()