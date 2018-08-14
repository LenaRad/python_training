# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='firstname'))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    contact_edition = Contact(firstname="new name", lastname="new lastname")
    contact_edition.id = contact.id
    app.contact.edit_by_id(contact.id, contact_edition)
    new_contact = db.get_contact_list()
    assert len(old_contact)  == app.contact.count()
    old_contact.remove(contact)
    old_contact.append(contact_edition)
    print("old contact :", sorted(old_contact, key=Contact.id_or_max))
    print("new contact :", sorted(new_contact, key=Contact.id_or_max))
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)