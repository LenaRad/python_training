# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname='new firstname', middlename='new middlename', lastname='new lastname',
                                   nickname='new nickname', title='new title', company='new company',
                                   address=' new address', home=' new home', mobile='new mobile', work='new work',
                                   fax='new fax', email='new email', email2='new email2', email3='new email3',
                                   homepage='new homepage', byear='2018', ayear='2018',
                                   address2='new address2', phone2='new phone2', notes='new notes'))
    app.session.logout()