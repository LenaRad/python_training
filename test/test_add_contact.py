# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, data_contacts):
    contact = data_contacts
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == app.contact.count()
    old_contact.append(contact)
    print("old contact :", sorted(old_contact, key=Contact.id_or_max))
    print("new contact :", sorted(new_contact, key=Contact.id_or_max))
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
