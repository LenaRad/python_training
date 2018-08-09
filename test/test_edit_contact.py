# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_edit_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname'))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname="new name", lastname="new lastname")
    contact.id = old_contact[index].id
    app.contact.edit_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact)  == app.contact.count()
    old_contact[index] = contact
    print("old contact :", sorted(old_contact, key=Contact.id_or_max))
    print("new contact :", sorted(new_contact, key=Contact.id_or_max))
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_edit_company_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname='firstname'))
#     old_contact = app.contact.get_contact_list()
#     app.contact.edit_first(Contact(company='new company'))
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact)  == len(new_contact)