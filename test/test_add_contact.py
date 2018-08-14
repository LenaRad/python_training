# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contact = db.get_contact_list()
    app.contact.create(contact)
    new_contact = db.get_contact_list()
    assert len(old_contact) + 1 == app.contact.count()
    old_contact.append(contact)
    print("old contact :", sorted(old_contact, key=Contact.id_or_max))
    print("new contact :", sorted(new_contact, key=Contact.id_or_max))
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                    key=Contact.id_or_max)
