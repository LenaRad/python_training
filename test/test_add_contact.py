# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create(Contact(firstname='firstname', middlename='middlename', lastname='lastname',
                                        nickname='nickname', title='title', company='company', address='address',
                                        home='home', mobile='mobile', work='work', fax='fax', email='email',
                                        email2='email2', email3='email3', homepage='homepage', byear='byear',
                                        ayear='ayear', address2='address2', phone2='phone2', notes='notes'))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)


def test_add_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create(Contact(firstname='', middlename='', lastname='', nickname='', title='', company='',
                                        address='', home='', mobile='', work='', fax='', email='', email2='', email3='',
                                        homepage='', byear='', ayear='', address2='', phone2='', notes=''))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)