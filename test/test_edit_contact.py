# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_firstname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname'))
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname='new firstname')
    contact.id = old_contact[0].id
    app.contact.edit_first(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact)  == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(old_contact, key=Contact.id_or_max)


# def test_edit_company_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname='firstname'))
#     old_contact = app.contact.get_contact_list()
#     app.contact.edit_first(Contact(company='new company'))
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact)  == len(new_contact)