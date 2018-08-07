# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_firstname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname'))
    old_contact = app.contact.get_contact_list()
    app.contact.edit_first(Contact(firstname='new firstname'))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact)  == len(new_contact)


def test_edit_company_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname'))
    old_contact = app.contact.get_contact_list()
    app.contact.edit_first(Contact(company='new company'))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact)  == len(new_contact)