# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_firstname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname'))
    app.contact.edit_first(Contact(firstname='new firstname'))


def test_edit_company_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname'))
    app.contact.edit_first(Contact(company='new company'))