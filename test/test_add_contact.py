# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname='firstname', middlename='middlename', lastname='lastname',
                                        nickname='nickname', title='title', company='company', address='address',
                                        home='home', mobile='mobile', work='work', fax='fax', email='email',
                                        email2='email2', email3='email3', homepage='homepage', byear='byear',
                                        ayear='ayear', address2='address2', phone2='phone2', notes='notes')
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(old_contact, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname='', middlename='', lastname='', nickname='', title='', company='',
                                        address='', home='', mobile='', work='', fax='', email='', email2='', email3='',
                                        homepage='', byear='', ayear='', address2='', phone2='', notes='')
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(old_contact, key=Contact.id_or_max)