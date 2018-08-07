# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_firstname_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname='new firstname'))
    app.session.logout()

def test_edit_company_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(company='new company'))
    app.session.logout()