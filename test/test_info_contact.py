# -*- coding: utf-8 -*-
import re
from random import randrange


def test_random_emails_on_home_page(app):
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact_from_view_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.all_emails_from_pages == merge_emails_like_on_home_page(contact_from_edit_page)


def test_random_info_contact_on_home_page(app):
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact_from_view_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.firstname == contact_from_edit_page.firstname
    assert contact_from_view_page.lastname == contact_from_edit_page.lastname
    assert contact_from_view_page.address == contact_from_edit_page.address


def clear(s):
    return re.sub("[ () - ]", "", s)


def merge_emails_like_on_home_page(contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.email, contact.email2, contact.email3]))))