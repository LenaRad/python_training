# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="New name", header='New header', footer='New footer'))
    app.session.logout()